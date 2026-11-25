# Siba OS Build History

**Project:** Siba OS
**Builder:** Sorokhaibam Nungsiba Singh
**Base:** Debian 12 "Bookworm" with the Linux kernel (stock Debian kernel)
**Target hardware:** Intel Core i3-3220, 8 GB RAM, SSD (works on any 64-bit PC)

## Version 1.0 "Aurora" (2026-11-24)

Built by Sorokhaibam Nungsiba Singh.

- First release of Siba OS, a clean and minimal Linux system for coding and making software.
- Desktop: slim GNOME with a centered bottom dock, soft rounded windows, light/dark wallpapers, calm blue accent, Inter and JetBrains Mono fonts, Papirus icons.
- Pre-installed: VS Code, Neovim, Git, GitHub CLI, GCC/G++/Clang, CMake, Python 3, Node.js, Java, Go, Rust, SQLite, Podman, Firefox, VLC.
- Performance: zram compressed swap, trimmed package set, animations kept light for 2-core CPUs.
- Identity: custom `/etc/os-release`, welcome app (`siba-welcome`), system info tool (`siba-info`).
- Documentation: full user guide at `/usr/share/doc/siba-os/USER_GUIDE.md` and `docs/USER_GUIDE.md`.
- Build system: `live-build` project with a GitHub Actions workflow that produces the ISO.
- Boot animation (Plymouth theme "siba") and a classical startup chime (opening of J.S. Bach's Prelude in C major, public domain).
- App store (Software with Flatpak and Flathub), LibreOffice (Writer, Calc, Impress, Draw), and WhatsApp and Gmail as app windows.

## Planned
- Custom GTK/shell theme polish and a GRUB theme.
- Persistence option for USB, more language toolchains from the welcome app.
