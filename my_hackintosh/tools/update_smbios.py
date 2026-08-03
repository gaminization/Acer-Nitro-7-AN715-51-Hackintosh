#!/usr/bin/env python3
"""
Acer Nitro 7 AN715-51 SMBIOS Updater
Injects fresh MacBookPro16,1 SMBIOS serials into EFI/OC/config.plist
"""

import os
import plistlib
import sys

def update_smbios(serial, mlb, uuid, rom="3CthvfF1"):
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    config_path = os.path.join(project_root, "EFI", "OC", "config.plist")
    
    with open(config_path, "rb") as f:
        config = plistlib.load(f)

    generic = config["PlatformInfo"]["Generic"]
    generic["SystemProductName"] = "MacBookPro16,1"
    generic["SystemSerialNumber"] = serial
    generic["MLB"] = mlb
    generic["SystemUUID"] = uuid
    
    if isinstance(rom, str):
        generic["ROM"] = rom.encode("utf-8") if len(rom) == 6 else bytes.fromhex("3C7468766646")

    with open(config_path, "wb") as f:
        plistlib.dump(config, f)
        
    print(f"✓ Injected SMBIOS MacBookPro16,1 successfully:")
    print(f"  - Serial: {serial}")
    print(f"  - Board Serial (MLB): {mlb}")
    print(f"  - UUID: {uuid}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python3 update_smbios.py <Serial> <MLB> <UUID> [ROM_HEX]")
        sys.exit(1)
    update_smbios(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else "3C7468766646")
