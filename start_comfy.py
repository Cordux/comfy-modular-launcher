import os
import subprocess
import json
import platform
from pathlib import Path

# Path to config file (next to the script)
CONFIG_FILE = Path(__file__).parent / "comfy_launcher_config.json"

# Default configuration
DEFAULT_CONFIG = {
    "global_output_directory": r"output",
    "comfyui_path": ".",
    "modes": {
        "1": {"name": "Z-Image-Turbo (GGUF)", "flags": "--enable-manager", "subfolder": "Z_Turbo"},
        "2": {"name": "SDXL Lightning/Turbo (Low VRAM)", "flags": "--enable-manager --lowvram --force-fp16 --disable-smart-memory", "subfolder": "SDXL_Lightning"},
        "3": {"name": "Flux GGUF (Balanced)", "flags": "--enable-manager --force-fp16 --cuda-malloc", "subfolder": "Flux"},
        "4": {"name": "Default / High VRAM", "flags": "--enable-manager", "subfolder": ""},
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

# Main loop
while True:
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print("=== ComfyUI Modular Launcher ===")
    print(f"Global Output Folder: {config['global_output_directory']}\n")

    for key, mode in config["modes"].items():
        sub = mode.get("subfolder", "")
        print(f"{key}: {mode['name']}")
        print(f"    → Subfolder: {sub if sub else '[Global Root]'}\n")

    print("Q: Quit Launcher")
    choice = input("\nChoose a mode (e.g 1) or Q to quit: ").strip().lower()

    if choice == 'q':
        print("\nExiting...")
        break

    elif choice in config["modes"]:
        mode = config["modes"][choice]
        final_output = os.path.join(config["global_output_directory"], mode.get("subfolder", ""))
        os.makedirs(final_output, exist_ok=True)

        full_cmd = f'python main.py --output-directory "{final_output}" {mode["flags"]}'.strip()

        print(f"\nLaunching: {mode['name']}...")
        os.chdir(config["comfyui_path"])
        subprocess.call(full_cmd, shell=True)
        break # Exit launcher once ComfyUI is closed

    else:
        input("\nInvalid choice! Press Enter to try again...") # Pause so user can read the error
