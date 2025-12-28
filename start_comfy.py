import os
import subprocess
import json
from pathlib import Path

# Path to config file (next to the script)
CONFIG_FILE = Path(__file__).parent / "comfy_launcher_config.json"

# Default configuration
DEFAULT_CONFIG = {
    "global_output_directory": r"C:\AI\ComfyUI_outputs",  # Change this to your main folder
    "comfyui_path": ".",  # Folder where ComfyUI's main.py is located
    "modes": {
        "1": {
            "name": "Z-Image-Turbo (GGUF - Normal VRAM)",
            "flags": "--enable-manager",
            "subfolder": "Z_Turbo"
        },
        "2": {
            "name": "SDXL Lightning/Turbo (Low VRAM)",
            "flags": "--enable-manager --lowvram --force-fp16 --disable-smart-memory",
            "subfolder": "SDXL_Lightning"
        },
        "3": {
            "name": "Flux GGUF (Balanced)",
            "flags": "--enable-manager --force-fp16 --cuda-malloc",
            "subfolder": "Flux"
        },
        "4": {
            "name": "Default / High VRAM (No Subfolder)",
            "flags": "--enable-manager",
            "subfolder": ""
        }
    }
}

# Load or create config
if CONFIG_FILE.exists():
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        config = json.load(f)
else:
    config = DEFAULT_CONFIG
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4)
    print(f"Created default config at {CONFIG_FILE}")
    print("Please edit comfy_launcher_config.json to set your paths and modes.")

# Build menu
print("=== ComfyUI Modular Launcher ===\n")
print(f"Global Output Base: {config['global_output_directory']}\n")

for key, mode in config["modes"].items():
    sub = mode.get("subfolder", "").strip()
    final_output = config["global_output_directory"]
    if sub:
        final_output = os.path.join(final_output, sub)
    print(f"{key}: {mode['name']}")
    print(f"     → Saves to: {final_output}\n")

choice = input("Choose startup mode (or press Enter to quit): ").strip()

if not choice:
    print("Goodbye!")
elif choice in config["modes"]:
    mode = config["modes"][choice]
    
    # Build final output path
    base_output = config["global_output_directory"]
    subfolder = mode.get("subfolder", "").strip()
    final_output = os.path.join(base_output, subfolder) if subfolder else base_output
    
    # Create directory if needed
    os.makedirs(final_output, exist_ok=True)
    
    # Build command
    base_cmd = f'python main.py --output-directory "{final_output}"'
    full_cmd = f'{base_cmd} {mode["flags"]}'.strip()
    
    print(f"\nLaunching: {mode['name']}")
    print(f"Output: {final_output}")
    print(f"Command: {full_cmd}\n")
    
    os.chdir(config["comfyui_path"])
    subprocess.call(full_cmd, shell=True)
else:
    print("Invalid choice.")
