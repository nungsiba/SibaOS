# Siba OS startup chime: opening of J.S. Bach, Prelude in C major (BWV 846, public domain),
# synthesized as a soft plucked-string sound with light reverb.
import numpy as np, wave
SR = 44100
def midi(n): return 440.0 * 2 ** ((n - 69) / 12)
C4, D4, E4, F4, G4, A4, B3 = 60, 62, 64, 65, 67, 69, 59
def bar(bass, n2, n3, n4, n5):
    return [bass, n2, n3, n4, n5, n3, n4, n5]
notes = []
notes += bar(C4, E4, G4, C4 + 12, E4 + 12)
notes += bar(C4, D4, A4, D4 + 12, F4 + 12)
notes += bar(B3, D4, G4, D4 + 12, F4 + 12)
notes += bar(C4, E4, G4, C4 + 12, E4 + 12)
step = 0.125
total = len(notes) * step + 4.0
buf = np.zeros(int(SR * total))
def pluck(f, dur=2.6):
    t = np.arange(int(SR * dur)) / SR
    s = np.zeros_like(t)
    for h, a in [(1, 1.0), (2, 0.42), (3, 0.22), (4, 0.12), (5, 0.07)]:
        s += a * np.sin(2 * np.pi * f * h * t) * np.exp(-t * (1.6 + 0.9 * h))
    s *= np.minimum(1, t / 0.006)
    return s
for i, n in enumerate(notes):
    start = int(i * step * SR)
    w = pluck(midi(n)) * (0.55 if i % 8 else 0.7)
    buf[start:start + len(w)] += w[:len(buf) - start]
# final held chord: C3 G3 C4 E4 G4 C5
t0 = int(len(notes) * step * SR)
for k, n in enumerate([48, 55, 60, 64, 67, 72]):
    w = pluck(midi(n), 3.8) * 0.5
    off = t0 + int(k * 0.05 * SR)
    buf[off:off + len(w)] += w[:len(buf) - off]
# light reverb
rng = np.random.default_rng(7)
ir_len = int(SR * 1.4)
ir = rng.standard_normal(ir_len) * np.exp(-np.arange(ir_len) / (SR * 0.35))
ir[0] = 0
from scipy.signal import fftconvolve
wet = fftconvolve(buf, ir)[:len(buf)]
wet /= np.max(np.abs(wet)) + 1e-9
dry = buf / (np.max(np.abs(buf)) + 1e-9)
mix = 0.82 * dry + 0.22 * wet
# slight stereo width via tiny delay
L = mix
R = np.concatenate([np.zeros(int(SR * 0.012)), mix])[:len(mix)]
st = np.stack([L, R], 1)
fade = np.ones(len(st)); fl = int(SR * 0.8); fade[-fl:] = np.linspace(1, 0, fl)
st *= fade[:, None]
st = st / np.max(np.abs(st)) * 0.8
pcm = (st * 32767).astype('<i2')
with wave.open('siba-startup.wav', 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
print('seconds', round(total, 2))
