# Acer Nitro 7 (AN715-51) OpenCore 1.0.0 Hackintosh

[![macOS Sequoia](https://img.shields.io/badge/macOS-Sequoia%20(15.x)%20%7C%20Sonoma%20(14.x)-black?logo=apple)](https://www.apple.com/macos/)
[![OpenCore](https://img.shields.io/badge/OpenCore-1.0.0%20RELEASE-blue)](https://github.com/acidanthera/OpenCorePkg)
[![Status](https://img.shields.io/badge/Status-Fully%20Optimized-brightgreen)](#system-specifications-)
[![Branch](https://img.shields.io/badge/Legacy%20Branch-prev__fork-orange)](#git-branches-)

Fully personalized, audited, and optimized **OpenCore 1.0.0** EFI configuration tailored specifically for the **Acer Nitro 7 AN715-51** laptop (Intel 9th Gen Coffee Lake Refresh i7-9750H), updated for **macOS Sequoia (15.x)** and **macOS Sonoma (14.x)**.

---

## Git Branches 🌿

- `master` (Current): Up-to-date **OpenCore 1.0.0** EFI for **macOS Sequoia (15.x) & Sonoma (14.x)** tailored for Intel Core i7-9750H, Intel AC 9560, ALC255, and ELAN I2C Trackpad.
- `prev_fork`: Clean backup branch containing the original 2020 OpenCore 0.5.9 / macOS Catalina 10.15.5 repository state prior to restructuring.

---

## System Specifications 💻

| Component | Status | Model / Details | Kext / Patch |
| :--- | :---: | :--- | :--- |
| **Model** | ✅ | Acer Nitro 7 AN715-51 | - |
| **CPU** | ✅ | Intel Core i7-9750H @ 2.60GHz (6C / 12T) | `SSDT-PLUG.aml` |
| **Chipset** | ✅ | Intel HM370 Chipset LPC Controller | `SSDT-SBUS-MCHC.aml` |
| **iGPU** | ✅ | Intel UHD Graphics 630 (1536 MB) | `WhateverGreen.kext` (`AAPL,ig-platform-id` = `0900A53E`) |
| **dGPU** | 🚫 | NVIDIA GeForce GTX 1660 Ti (6GB GDDR6) | Disabled via `SSDT-DDGPU.aml` & `-wegnoegpu` |
| **Audio** | ✅ | Realtek High Definition Audio ALC255 | `AppleALC.kext` (`alcid=29`) |
| **Wi-Fi** | ✅ | Intel Wireless-AC 9560 160MHz | `AirportItlwm.kext` / `itlwm.kext` |
| **Bluetooth** | ✅ | Intel Wireless Bluetooth | `IntelBluetoothFirmware.kext`, `IntelBTPatcher.kext`, `BlueToolFixup.kext` |
| **Ethernet** | ✅ | Killer E2500 Gigabit Ethernet | `RealtekRTL8111.kext` |
| **Trackpad** | ✅ | ELAN I2C Precision Trackpad (ELAN0504) | `VoodooI2C.kext` + `VoodooI2CHID.kext` + `VoodooI2CELAN.kext` |
| **Keyboard** | ✅ | Standard PS/2 Keyboard + Fn Hotkeys | `VoodooPS2Controller.kext` + `BrightnessKeys.kext` + `SSDT-BKeyQ11Q12-Acer.aml` |
| **Storage** | ✅ | Dual WDC PC SN520 NVMe SSDs | Native NVMe support |
| **Power Mgmt** | ✅ | CPU Power Management & Sleep/Wake | `SSDT-EC.aml`, `SSDT-PLUG.aml`, `SSDT-GPRW.aml` |

---

## Features & Functional Status ✨

- [x] **OpenCore 1.0.0** native UEFI bootloader setup for **macOS Sequoia (15.x) & Sonoma (14.x)**
- [x] **Graphics Acceleration**: Intel UHD 630 with Metal 3 support and smooth rendering
- [x] **Battery Life & Power Management**: CPU frequency scaling & native X86PlatformPlugin
- [x] **dGPU Disablement**: Discrete GTX 1660 Ti fully powered off (saving ~15W power and preventing heat)
- [x] **Audio**: Speaker, Headphone Jack, and Internal Microphone supported via ALC255 (`layout-id` 29)
- [x] **Intel Wi-Fi & Bluetooth**: Native macOS network integration via AirportItlwm & BlueToolFixup
- [x] **I2C Precision Trackpad**: Multi-touch gestures, smooth scrolling, and palm rejection
- [x] **Display Brightness**: Native brightness slider and keyboard Fn keys (`BrightnessKeys.kext`)
- [x] **Sleep & Wake**: Stable sleep/wake cycle with instant wake bug fixed (`SSDT-GPRW.aml`)
- [x] **USB Mapping**: Custom USB port map via `USBToolBox.kext` + `UTBMap.kext`

---

## Repository Structure 📂

```
Acer-Nitro-7-AN715-51-Hackintosh/
├── EFI/                        # Main Production EFI Folder (OpenCore 1.0.0)
│   ├── BOOT/
│   │   └── BOOTx64.efi
│   └── OC/
│       ├── ACPI/               # Tailored compiled SSDTs (EC, PLUG, PNLF, DDGPU, XOSI, GPRW, etc.)
│       ├── Drivers/            # OpenRuntime, HfsPlus, ResetNvramEntry
│       ├── Kexts/              # Modern 2024-2026 release kexts
│       ├── Tools/              # OpenShell.efi, CleanNvram.efi
│       ├── config.plist        # Fully validated OpenCore 1.0.0 config
│       └── config.plist.old_catalina  # Backup of original 2020 Catalina config
├── my_hackintosh/              # Local Workspace & Specifications
│   ├── hardware_specs/         # Dumped device specs, screenshots & SMBIOS backups
│   ├── acpi_dumps/             # DSDT dumps & SSDTTime results
│   ├── bios_mods/              # Insyde 1.29 unlocked BIOS mod documentation
│   ├── reference_docs/        # Dortania & OC-Little guides
│   └── tools_and_sources/      # GenSMBIOS, OpenCore binaries, kext sources
└── README.md
```

---

## Recommended BIOS Settings ⚙️

### Security & Boot Options
* **SATA Mode**: `AHCI` (Crucial: Do not use Intel RST/RAID)
* **Secure Boot**: `Disabled`
* **Fast Boot**: `Disabled`
* **VT-d**: `Disabled` (or keep enabled if `DisableIoMapper` is `True` in config)
* **DVMT Pre-Allocated**: `64MB` (or `32MB` with stolenmem framebuffer patch)

### If using Unlocked Insyde 1.29 BIOS (Optional Mod):
* **Advanced Tab**: Unlocked for temperature throttling adjustment and advanced power states.
* **FPRR (Flash Protection)**: Disabled for ACPI/Flash mods.

---

## Installation & Post-Install Instructions 🚀

### 1. Preparing the USB Flash Drive
1. Create a **macOS Sequoia (15.x) or Sonoma (14.x)** installer USB formatted as `GUID Partition Map` and `Mac OS Extended (Journaled)`.
2. Mount the USB's EFI partition.
3. Copy the root `EFI` folder from this repository directly to the USB's EFI partition.

### 2. SMBIOS & Backup Management
- The old SMBIOS values from the original Catalina repo are backed up in `my_hackintosh/hardware_specs/old_smbios_backup.txt`.
- A fresh, unique `MacBookPro16,1` SMBIOS set has been generated and pre-injected into `EFI/OC/config.plist` (`Serial: C02F7TZ0MD6N`, `MLB: C02106303GUN9PR1H`, `SystemUUID: E6F2F893-DAE9-4267-9AA4-E66AF9710255`).

### 3. OpenCore Config Validation
Verify the integrity of `config.plist` at any time using the included `ocvalidate` tool:
```bash
./my_hackintosh/tools_and_sources/OpenCore-1.0.0-RELEASE/Utilities/ocvalidate/ocvalidate.linux EFI/OC/config.plist
```

---

## Credits & Acknowledgements 📚

- [Acidanthera](https://github.com/acidanthera) for OpenCorePkg, Lilu, VirtualSMC, WhateverGreen, AppleALC, and Brcm/Intel drivers.
- [OpenIntelWireless](https://github.com/OpenIntelWireless) for `AirportItlwm` and `IntelBluetoothFirmware`.
- [VoodooI2C](https://github.com/VoodooI2C/VoodooI2C) team for I2C trackpad drivers.
- [CorpNewt](https://github.com/corpnewt) for `SSDTTime`, `GenSMBIOS`, and `ProperTree`.
- [Dortania](https://dortania.github.io/OpenCore-Install-Guide/) for the definitive OpenCore installation guides.

---

## License 📜
This project is licensed under the [MIT License](LICENSE).