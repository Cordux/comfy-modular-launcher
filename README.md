# ComfyUI Modular Launcher

A simple, user-friendly Python launcher for ComfyUI that lets you switch between different startup modes (e.g., low-VRAM, GGUF models, Lightning, etc.) with one click.

Perfect for users with limited VRAM (6–12GB) who frequently switch between models like:
- Z-Image-Turbo GGUF
- SDXL Lightning/Turbo
- Flux GGUF
- Normal/high-VRAM workflows

## Features
- One global output folder — set it once
- Optional per-mode subfolders (e.g., `\Z_Turbo`, `\SDXL_Lightning`)
- Fully configurable via `comfy_launcher_config.json` — no code editing needed
- Auto-creates output folders
- Clean menu with clear output paths

## How to Use
1. Place `start_comfy.py` in your ComfyUI root folder (where `main.py` is).
2. Run `start_comfy.py` (double-click or via terminal).
3. First run creates `comfy_launcher_config.json` — edit it to set your paths and modes.
4. Choose a mode and launch!

## Customization
Edit `comfy_launcher_config.json`:
- Change `global_output_directory` once
- Add/remove modes and subfolders
- Modify flags as needed

## Credit
Created by Cordux with help from Grok (xAI).  
Feel free to fork, improve, and share — just keep the credit! 😄

Made for the low-VRAM warriors pushing ComfyUI to its limits in 2025.
