#!/bin/sh
# Build Siba OS on a Debian or Ubuntu machine (also works in WSL2 with enough disk).
# Needs about 25 GB free disk and internet access.
set -e

sudo apt-get update
sudo apt-get install -y debootstrap xorriso squashfs-tools \
    grub-pc-bin grub-efi-amd64-bin mtools dosfstools syslinux isolinux \
    debian-archive-keyring curl gnupg wget

# Debian 12's live-build (newer than the one in Ubuntu 22.04)
wget -O /tmp/live-build.deb https://deb.debian.org/debian/pool/main/l/live-build/live-build_20230502_all.deb
sudo apt-get install -y /tmp/live-build.deb

chmod +x auto/config auto/build auto/clean config/hooks/live/*.hook.chroot config/includes.chroot/usr/local/bin/*

sudo ./auto/config
sudo ./auto/build

echo "Done. Your ISO is in this folder:"
ls -lh ./*.iso
