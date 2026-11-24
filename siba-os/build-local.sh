#!/bin/sh
# Build Siba OS on a Debian or Ubuntu machine (also works in WSL2 with enough disk).
# Needs about 20 GB free disk and internet access.
set -e

sudo apt-get update
sudo apt-get install -y live-build debootstrap xorriso squashfs-tools \
    grub-pc-bin grub-efi-amd64-bin mtools dosfstools syslinux isolinux \
    debian-archive-keyring curl gnupg

mkdir -p config/includes.chroot/usr/share/doc/siba-os
cp docs/USER_GUIDE.md BUILD_HISTORY.md config/includes.chroot/usr/share/doc/siba-os/

sudo ./auto/config
sudo ./auto/build

echo "Done. Your ISO is in this folder:"
ls -lh ./*.iso
