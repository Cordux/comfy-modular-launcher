![ComfyUI](https://img.shields.io/badge/ComfyUI-Modular-blue)
![GPU](https://img.shields.io/badge/GPU-RTX%203050%206GB-green)
![RAM](https://img.shields.io/badge/RAM-32GB-red)

# Modular ComfyUI Workflows  
A collection of my personal, modular [ComfyUI](https://github.com/comfyanonymous/ComfyUI) workflows — designed to show that you **don’t** need a high‑end GPU to be able to use Image generation tools.

The goal of this repository is to demonstrate how far you can push ComfyUI using a clean, structured, subgraph‑based system that runs smoothly even on low‑VRAM hardware.

---

## 🖥️ Hardware Used
These workflows are tested on:

- **NVIDIA RTX 3050 (6GB VRAM)**
- **32 GB RAM**

If you have similar or slightly better hardware, everything here should run without issues.

---
## 🙏 Special Thanks
A huge thanks to **[rgthree](https://github.com/rgthree/rgthree-comfy)** for creating some of the most essential quality‑of‑life tools in the ComfyUI ecosystem.  
Without Fast Groups Muter, reroutes, and the overall design philosophy behind his extensions, this modular workflow would not have been possible.

---
## 🚀 How to Use
Download the workflow JSON files and load them directly into ComfyUI.

If you’re using the latest version with the built‑in Manager, it will show which extensions are required and can install most of them automatically.
Some extensions still need to be installed manually.

---
## 📦 What’s Included
- Modular ComfyUI workflows
- Subgraph‑based architecture
- Low‑VRAM friendly Subgraphs
- Example images and workflow diagrams

---
## 🧩 My Main Workflow
This is my primary modular workflow.  
Every major feature is isolated into its own **subgraph**, and everything is controlled through a **Fast Groups Muter** for instant toggling.

<img width="1596" height="905" alt="image" src="https://github.com/Cordux/comfy-modular-launcher/blob/main/workflows/My%20Work%20Flow.png" />

<details>
<summary><strong>Subgraphs included</strong></summary>

- AuraPonyV7  
- LoRA Info  
- Pony SDXL  
- Stable Diff 3  
- Flux 1 Schnell And Dev  
- Convert SD 1.5 to Pony  
- Stable Diff 1.5  
- Testing  
- IP Adapter  
- Pony  
- Resize  
- SDXL NSFW  
- SDXL  
- Refiner  
- Split Image Creation  
- TangoFlux (Music)  
- Face Swap  
- Z-Image-Turbo  
- InPainting  
- Wan 2.1 Image2Video  
- Wan 2.1 Text2Video  

</details>

---

## ⚙️ Working Flow
A simplified version of the main workflow, used for quick testing and generation.  
Includes video tools, image tools, and multiple generation backends.

<img width="1436" height="860" alt="image" src="https://github.com/Cordux/comfy-modular-launcher/blob/main/workflows/Working%20flow.png" />

<details>
<summary><strong>Subgraphs included</strong></summary>

### Video
- Wan 2.1 Image2Video  
- Wan 2.1 Text2Video  
- Wan2.2 5B  

### Tools
- LoRA Info  
- Notes  
- SDXL LoRA to SD  
- Upscale Batch  

### Image Tools
- IPAdvance (IPA)  
- Inpainting  

### Image Generation
- SDXL Lightning  
- NoobAI‑XL  
- SD 1.5  
- Flux  

</details>

---

## 🔧 Why Modular?
By splitting everything into subgraphs and controlling them with a muter, I can:

- switch between SDXL, Flux, IPA, Inpainting, Wan video, etc.  
- avoid rebuilding workflows  
- keep VRAM usage low  
- test features independently  

This makes the system flexible, fast, and easy to maintain.

---
## 📝 Notes
All workflows are built with stability and low VRAM usage in mind.
Feel free to explore, modify, or extend them — if you want to build your own modular setup.

---

## 🤝 Credits
Thanks to the ComfyUI community and all extension creators who make this level of modularity possible.
