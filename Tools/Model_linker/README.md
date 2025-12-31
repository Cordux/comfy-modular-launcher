# ComfyUI Model Linker (Cross-Platform)

A simple, user-friendly tool to create and manage symbolic links (or junctions on Windows) for your ComfyUI models. Perfect for **portable setups** and **low-VRAM warriors** who keep their large model files on a separate drive or folder.

This script lets you point all standard ComfyUI model folders (checkpoints, LoRAs, ControlNet, etc.) to a central storage location — saving precious space on your main drive while keeping everything working seamlessly.

### Features
- **Cross-platform**: Works on Windows, Linux, and macOS
- **No admin/root required** (uses junctions on Windows, symlinks on *nix)
- Automatic config creation on first run
- Dry-run mode
- Verify mode to check existing links
- Colored output (via `colorama`)
- Special support for nodes like AnimateDiff
- Fully configurable via `config_links.json`

### Requirements
- Python 3.7+ (already included in ComfyUI portable embeds)
- Optional: `colorama` for colored output
  ```bash
  pip install colorama
  ```

### Quick Start
1. Download `link_models.py` from this repository.
2. Place `link_models.py` in your ComfyUI root folder (same level as `main.py` or your launcher).

3. Run it for the first time:
   ```bash
   python link_models.py
   ```

   - If `config_links.json` doesn't exist, it will be created automatically.
   - The script will pause and ask you to **edit the config** (open it in any text editor).
   - Edit `source_base` → full path to your central models folder (e.g., `D:/AI/models` on Windows or `/home/user/AI/models` on Linux).

4. Save the config and press **Enter** in the terminal — the script will create all links.
5. Optionally, copy the example `config_links.json` to `config_links.json` and edit it.

### Usage

```bash
python link_models.py          # Normal mode: create/repair links
python link_models.py --dry-run   # See what would happen without changes
python link_models.py --verify    # Check if all links are valid
python link_models.py -v          # Short for --verify
```
<details>
  <summary><b>Example config_links.json</b></summary>


  ```json
  {
    "source_base": "D:/AI/models",
    "comfyui_root": ".",
    "folders": [
      "checkpoints",
      "loras",
      "vae",
      "controlnet",
      "unet",
      "upscale_models",
      "ipadapter",
      "insightface",
      "clip",
      "text_encoders",
      "facerestore_models",
      "clip_vision",
      "audioldm-l-full",
      "RMBG"
    ],
    "special_links": {
      "custom_nodes/ComfyUI-AnimateDiff-Evolved/models": "animatediff_models"
    },
    "dry_run": false,
    "verbose": true
  }
  ```
</details>

- Add more entries to `special_links` for other custom nodes that have their own model folders.
- Change `comfyui_root` only if running the script from outside the ComfyUI folder.

### Troubleshooting
- If links fail on Windows: Make sure you're running the script from a folder you have full write access to.
- Missing models? Run with `--verify` to see what's broken.

### Why This Helps Portable & Low-VRAM Setups
- Keep hundreds of GB of models on a big external HDD/SSD
- ComfyUI folder stays small and portable (fits on a fast but small NVMe)
- Move your entire ComfyUI folder anywhere — just run the linker again

### Part of the ComfyUI Modular Launcher Ecosystem
This tool pairs perfectly with **[ComfyUI-Modular-Launcher](https://github.com/Cordux/comfy-modular-launcher)** Shameless advertising.👍

Happy generating! 🚀

---

Made with ❤️ (and occasional Grok nagging) by **Cordux**
*Vibecoding is good. Low-VRAM life is better.*
