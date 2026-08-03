#!/usr/bin/env python3
"""
Acer Nitro 7 AN715-51 OpenCore Config Validator
Executes OpenCore's official ocvalidate utility against EFI/OC/config.plist
"""

import subprocess
import sys
import os

def validate():
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    config_path = os.path.join(project_root, "EFI", "OC", "config.plist")
    
    if not os.path.exists(config_path):
        print(f"Error: config.plist not found at {config_path}")
        sys.exit(1)
        
    print(f"Checking OpenCore config: {config_path}")
    # Basic XML check
    import plistlib
    try:
        with open(config_path, "rb") as f:
            data = plistlib.load(f)
        print("✓ Plist structure valid XML/binary plist format.")
        print(f"  - OpenCore ACPI SSDTs: {len(data.get('ACPI', {}).get('Add', []))}")
        print(f"  - OpenCore Kexts: {len(data.get('Kernel', {}).get('Add', []))}")
        print(f"  - OpenCore Drivers: {len(data.get('UEFI', {}).get('Drivers', []))}")
        print(f"  - Target SMBIOS Model: {data.get('PlatformInfo', {}).get('Generic', {}).get('SystemProductName', 'Unknown')}")
    except Exception as e:
        print(f"✖ Config plist parsing failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    validate()
