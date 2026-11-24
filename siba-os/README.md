# Siba OS

A clean, minimal Linux system for coding and making software.
Base: Debian 12 with the Linux kernel. Desktop: slim GNOME with a bottom dock.

**Built by Sorokhaibam Nungsiba Singh.**
See [BUILD_HISTORY.md](BUILD_HISTORY.md) and [docs/USER_GUIDE.md](docs/USER_GUIDE.md).

## Build the ISO on GitHub (easiest)
1. Create a new GitHub repository and upload everything in this folder (keep the `.github` folder).
2. Open the **Actions** tab, choose **Build Siba OS ISO**, click **Run workflow**.
3. After about 45-90 minutes, download the `siba-os-iso` artifact from the finished run.
4. Write the ISO to USB with Rufus or balenaEtcher, or attach it to a VirtualBox VM to test.

## Build on your own machine
On Debian/Ubuntu (or WSL2): `sh build-local.sh`

## Layout
| Path | Purpose |
|---|---|
| `auto/config` | live-build settings (distro, boot, ISO name) |
| `config/package-lists/` | packages: base, desktop, developer tools |
| `config/hooks/live/` | VS Code install and OS identity |
| `config/includes.chroot/` | files copied into the OS: theme, wallpapers, welcome app |
| `docs/USER_GUIDE.md` | user guide shipped inside the OS |
| `.github/workflows/build-iso.yml` | cloud ISO build |
