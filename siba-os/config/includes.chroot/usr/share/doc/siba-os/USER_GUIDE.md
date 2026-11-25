# Siba OS User Guide

Siba OS is a clean, fast Linux system for coding and making software.
Built by **Sorokhaibam Nungsiba Singh**.

---

## 1. Getting started

### Try it first (live mode)
1. Write the ISO to a USB stick with **Rufus** (Windows) or **balenaEtcher**. Use the default settings. If Rufus asks, choose "DD Image mode".
2. Plug the USB into the PC and restart. Press the boot menu key (usually **F12**, **F11**, **Esc** or **F8**) and pick the USB stick.
3. Choose **Live system** in the boot menu. You land on the desktop without changing your disk.

Live mode forgets changes when you restart. To keep your work, install the system or save files to another drive.

### Test in a virtual machine
In VirtualBox, create a Debian (64-bit) VM with 3 GB RAM, 2 CPUs, a 25 GB disk, and EFI enabled. Attach the ISO and start it.

### Install to disk
1. Restart and choose **Install** (graphical installer) from the boot menu.
2. Follow the steps: language, keyboard, user name, password, disk.
3. **Warning:** installing to a whole disk erases it. Back up your data first. To keep Windows, choose manual partitioning and use free space only.

Live login user is `siba` and the password is `live` (change it after install with `passwd`).

---

## 2. The desktop

- **Dock (bottom):** your favorite apps. It hides on its own when a window is near; move the pointer to the bottom edge to show it. Right-click an app icon to pin or unpin it.
- **Top bar:** Activities, clock, network, volume, power. Click the clock for the calendar and notifications.
- **Search:** press the **Super (Windows) key** and type an app or file name.
- **Windows:** drag a window to the left or right edge to tile it. **Super + Up** maximizes.
- **Workspaces:** Super key, then use the strip on the right to add desktops. **Ctrl + Alt + Left/Right** switches.
- **Light/dark mode:** Settings, Appearance.
- **Wallpaper:** Settings, Background.

### Useful shortcuts
| Keys | What it does |
|---|---|
| Super | Open search and overview |
| Super + A | Show all apps |
| Alt + Tab | Switch windows |
| Ctrl + Alt + T | Open terminal |
| Super + Left / Right | Tile window |
| Super + Up | Maximize |
| Print Screen | Screenshot |

---

## 3. Coding on Siba OS

### Editors
- **VS Code:** `code` or the dock icon. Install extensions from the built-in Extensions panel (Python, C/C++, Rust Analyzer, Go, GitLens).
- **Neovim:** `nvim` in the terminal.
- **Text Editor:** a simple GNOME editor for quick edits.

### Languages ready to use
| Language | Check | Notes |
|---|---|---|
| Python 3 | `python3 --version` | Use `python3 -m venv .venv` for projects |
| C / C++ | `gcc --version`, `clang --version` | Build with `make` or `cmake` |
| Node.js | `node --version`, `npm --version` | Use `npm init` to start a project |
| Java | `java --version` | OpenJDK |
| Go | `go version` | |
| Rust | `rustc --version`, `cargo new app` | |

### Python virtual environment
```
mkdir myapp && cd myapp
python3 -m venv .venv
source .venv/bin/activate
pip install requests
```

### Git and GitHub
```
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
gh auth login
git clone https://github.com/user/repo.git
```

### Containers (Podman, Docker-compatible)
```
podman run --rm hello-world
podman ps
```
Podman works without a background service and uses less memory. Most `docker` commands work if you replace `docker` with `podman`.

### Databases
`sqlite3 mydb.sqlite` opens a local database. `psql` (PostgreSQL client) is installed; run the server in a Podman container.

---

## 4. Terminal quick reference

| Command | Meaning |
|---|---|
| `ll` | List files with details |
| `cd folder` | Enter a folder |
| `cd ..` | Go up one folder |
| `mkdir name` | Make a folder |
| `rg text` | Fast search inside files |
| `fdfind name` | Fast file search |
| `htop` | Watch CPU and memory |
| `siba-info` | Show Siba OS system summary |
| `sudo apt update && sudo apt upgrade` | Update the system |
| `sudo apt install name` | Install a program |
| `sudo apt remove name` | Remove a program |

---

## 5. Network, apps and updates

- **Wi-Fi:** top bar, network icon, pick a network. If your Wi-Fi card is not found, check that the firmware packages installed (`sudo apt install firmware-iwlwifi firmware-realtek`).
- **Install apps:** run `sudo apt install <name>`, or use Flatpak if you add it (`sudo apt install flatpak`).
- **Updates:** `sudo apt update && sudo apt upgrade`.

---

## 6. Performance tips (for 2-core / 8 GB machines)

- Keep fewer browser tabs open; Firefox and VS Code are the biggest memory users.
- Compressed swap (zram) is enabled, so the system stays responsive near full memory.
- Check usage with `htop` or the System Monitor app.
- Turn off animations if needed: Settings, Accessibility, Reduce Animation.
- Close VS Code extensions you do not use.

---

## 7. Troubleshooting

| Problem | Try this |
|---|---|
| USB does not boot | Re-flash in DD mode. Turn off Secure Boot in BIOS or use the boot menu key. |
| Black screen after boot | Pick the "safe graphics" entry in the boot menu (add `nomodeset`). |
| No Wi-Fi | Use a cable, run `sudo apt install firmware-iwlwifi firmware-realtek`, reboot. |
| No sound | Open Settings, Sound, check the output device. Restart with `systemctl --user restart pipewire`. |
| Forgot password | Boot live USB, mount the disk, and use `chroot` with `passwd`. |
| Screen too small in VM | Install VirtualBox Guest Additions or use a higher video memory. |

---

## 8. About

- **System:** Siba OS 1.0 "Aurora"
- **Base:** Debian 12 with the Linux kernel
- **Built by:** Sorokhaibam Nungsiba Singh
- **Build history:** see `BUILD_HISTORY.md`
- Run `siba-info` for a live summary of your machine.

---

## 9. Startup sound
Siba OS plays a short classical chime (the opening of Bach's Prelude in C major, public domain) when the desktop loads.
To turn it off: open **Startup Applications** (or Tweaks, Startup Applications) and remove **Siba Startup Sound**, or delete `~/.config/autostart/siba-startup-sound.desktop`.

---

## 10. Apps, office and messaging
- **Software (app store):** open **Software** from the dock to find and install apps. It uses Flathub and the Debian repositories. You need an internet connection.
- **LibreOffice:** Writer (documents), Calc (spreadsheets), Impress (presentations) and Draw. They open and save Microsoft Office files (`.docx`, `.xlsx`, `.pptx`) and PDFs.
- **WhatsApp:** opens WhatsApp Web in its own window. On first use, link it to your phone by scanning the QR code in WhatsApp, under Linked devices.
- **Gmail:** opens Gmail in its own window. Sign in with your Google account.
- WhatsApp and Gmail need an internet connection and use Chromium for their windows. Firefox stays your main browser.
