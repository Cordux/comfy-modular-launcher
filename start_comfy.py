import os
import subprocess
import json
import platform
from pathlib import Path
import psutil

def kill_comfyui_python():
    print("🔍 Checking for running ComfyUI Python processes...")

    found = False
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            cmd = proc.info['cmdline'] or []
            if len(cmd) == 0:
                continue

            # Hoppa över vår egen process
            if proc.pid == os.getpid():
                continue

            # Leta efter python som kör main.py i ComfyUI
            if ("python" in proc.info['name'].lower() or "python" in " ".join(cmd).lower()) and "main.py" in cmd:
                found = True
                print(f"⚠️ Found running ComfyUI instance (PID {proc.pid}) — terminating...")
                proc.terminate()
                try:
                    proc.wait(timeout=5)
                except psutil.TimeoutExpired:
                    proc.kill()

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    if not found:
        print("✔️ No existing ComfyUI Python processes running.")

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
        
        # Kill existing ComfyUI python processes
        kill_comfyui_python()

        full_cmd = f'python main.py --output-directory "{final_output}" {mode["flags"]}'.strip()

        print(f"\nLaunching: {mode['name']}...")
        os.chdir(config["comfyui_path"])
        subprocess.call(full_cmd, shell=True)
        break # Exit launcher once ComfyUI is closed

    else:
        input("\nInvalid choice! Press Enter to try again...") # Pause so user can read the error
