# ComfyUI Modular Launcher
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue) [![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

A simple, user-friendly Python launcher for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that lets you switch between different startup modes (e.g., low-VRAM, GGUF models, Lightning, etc.) with one click.

Perfect for users with limited VRAM (6–12GB) who frequently switch between models like:
- Z-Image-Turbo GGUF
- SDXL Lightning/Turbo
- Flux GGUF
- Normal/high-VRAM workflows

## ⚠️ Disclaimer & Safety
- **Path Awareness:** This script handles file and folder creation. Ensure your `global_output_directory` is set to a location where you have write permissions (avoiding protected system folders).
- **Arguments/Flags:** The flags provided in the example are suggestions. Since this script passes commands directly to `main.py`, ensure you are using flags compatible with your specific ComfyUI version and hardware.
- **ComfyUI-Manager:** Some modes include the `--enable-manager` flag. Ensure you have the [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager) custom node installed if you plan to use it.
- **Use at your own risk:** While this script is a simple launcher, the author is not responsible for any data loss or system instability caused by incorrect configuration or hardware strain.

<details>
  <summary><h3>Screenshots</h3></summary>
  <b>Personal</b>:<br>
  <img width="561" height="427" alt="image" src="https://github.com/user-attachments/assets/9cc8ab43-382d-4fa3-a7b8-e0841ed17915" /><br>
  <b>Default</b><br>
  <img width="580" height="349" alt="image" src="https://github.com/user-attachments/assets/7c749ae9-dc52-40f9-b761-7abce3546e3e" />


</details>


## Features
- One global output folder — set it once
- Optional per-mode subfolders (e.g., `\Z_Turbo`, `\SDXL_Lightning`)
- Fully configurable via `comfy_launcher_config.json` — no code editing needed
- Auto-creates output folders
- Clean menu with clear output paths
- Smart Menu: Automatically clears the terminal for a clean UI and stays open if you make a typo.
- Quick Exit: Built-in Q option to exit the launcher instantly.

## Requirements
- **Python 3.10+**
- **ComfyUI** ([Github installation](https://github.com/comfyanonymous/ComfyUI) or [installation](https://www.comfy.org/download]))
- No additional pip dependencies required (uses built-in Python libraries).

## How to Use
1. Place `start_comfy.py` in your ComfyUI root folder (where `main.py` is).
    <details>
        <summary><b>Placement</b></summary>
      
        ComfyUI/
        ├── main.py
        ├── start_comfy.py  <-- Place it here!
        ├── comfy_launcher_config.json (generated after first run)
        ├── models/
        └── custom_nodes/
    </details>
2. Run `start_comfy.py` (double-click) or:
    <details>
    <summary><b>Run in the terminal</b></summary>

    ```bash
    # Navigate to your folder
    cd path-to-your-comfyUI-folder
    # Launch the script
    python start_comfy.py
    ```
    </details>
3. First run creates `comfy_launcher_config.json` — edit it to set your paths and modes.
4. Choose a mode and launch!

## Customization
Edit `comfy_launcher_config.json`:
- Change `global_output_directory` once
- Add/remove modes and subfolders
- Modify flags as needed
- Easy to change numbers to names, Just change the key (The number) to name in the `comfy_launcher_config.json` file

<details>
<summary><b>Click to see Example Config</b></summary>

```json
{
  "global_output_directory": "C:/AI_Generations/ComfyUI_Outputs",
  "comfyui_path": ".",
  "modes": {
    "1": {
      "name": "Z-Image-Turbo (Low VRAM)",
      "flags": "--enable-manager --lowvram --fp8_e4m3fn-text-enc",
      "subfolder": "Z_Turbo"
    },
    "2": {
      "name": "Flux GGUF (Balanced)",
      "flags": "--enable-manager --force-fp16 --cuda-malloc",
      "subfolder": "Flux"
    },
    "3": {
      "name": "Standard SDXL",
      "flags": "--enable-manager",
      "subfolder": ""
    }
  }
}

```

</details>
<details>
  <summary><b>Click to see Example Names</b></summary>
  
  ```json
{
  "global_output_directory": "C:/AI_Generations/ComfyUI_Outputs",
  "comfyui_path": ".",
  "modes": {
    "z-image": {
      "name": "Z-Image-Turbo (Low VRAM)",
      "flags": "--enable-manager --lowvram --fp8_e4m3fn-text-enc",
      "subfolder": "Z_Turbo"
    },
    "Flux": {
      "name": "Flux GGUF (Balanced)",
      "flags": "--enable-manager --force-fp16 --cuda-malloc",
      "subfolder": "Flux"
    },
    "sdxl": {
      "name": "Standard SDXL",
      "flags": "--enable-manager",
      "subfolder": ""
    }
  }
}

```
</details>

## Troubleshooting

* **"Python is not recognized..."**
* Make sure Python is added to your system's **PATH**. You can fix this by re-running the Python installer and checking "Add Python to PATH."


* **"Script can't find `main.py`"**
* Ensure `start_comfy.py` is in the same folder as ComfyUI's `main.py`.


* **"Permissions Errors"**
* If your `global_output_directory` requires Admin rights, try running the script as Administrator or change the path to a user folder.

## Contributing
Contributions are welcome! If you have ideas for new features, better default flags for specific models, or bug fixes:

1. **Fork** the project.
2. Create your **Feature Branch** (`git checkout -b feature/AmazingFeature`).
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`).
4. **Push** to the branch (`git push origin feature/AmazingFeature`).
5. Open a **Pull Request**.

### Planned Roadmap
- [ ] Support for environment variable toggles.
- [ ] Auto-update check for the launcher script.
- [ ] Presets for Flux.1 dev/schnell modes.

## Credit

Created by Cordux with help from Grok (xAI).

Feel free to fork, improve, and share — just keep the credit! 😄

Made for the low-VRAM warriors pushing ComfyUI to its limits in 2025.
