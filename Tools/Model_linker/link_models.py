import os
import sys
import json
import platform
import shutil
import subprocess
import argparse
from pathlib import Path

# Optional: colored output
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    COLOR = True
except ImportError:
    COLOR = False
    class Fore: RED = GREEN = YELLOW = CYAN = MAGENTA = RESET = ''
    Style = type('Style', (), {'BRIGHT': '', 'RESET_ALL': ''})


CONFIG_FILE = "config_links.json"


def create_default_config(): # Creates a base config_links.json file to edit
    default_config = {
        "source_base": "D:/models",  # <-- CHANGE THIS TO YOUR MODELS DRIVE/FOLDER
        "comfyui_root": ".",            # Usually "." for portable setups
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
            # Add more like: "custom_nodes/AnotherNode/models": "some_folder"
        },
        "dry_run": False,
        "verbose": True
    }

    config_path = Path(CONFIG_FILE)
    config_path.write_text(json.dumps(default_config, indent=4), encoding='utf-8')

    print(f"{Fore.GREEN}[SUCCESS]{Style.RESET_ALL} Created {CONFIG_FILE}")
    print(f"\n{Fore.CYAN}Please edit the file now:{Style.RESET_ALL}")
    print(f"   • Set 'source_base' to your main models folder (e.g. D:/models or /home/user/models)")
    print(f"   • Adjust 'comfyui_root' only if ComfyUI is not in this folder")
    print(f"   • Add/remove folders as needed")
    print(f"\n{Fore.YELLOW}After editing, save the file and press Enter here to continue...{Style.RESET_ALL}")
    input()


def load_config():
    if not os.path.exists(CONFIG_FILE):
        print(f"{Fore.YELLOW}[INFO]{Style.RESET_ALL} Config file not found: {CONFIG_FILE}")
        create_default_config()

    try:
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            config = json.load(f)
        print(f"{Fore.GREEN}[INFO]{Style.RESET_ALL} Config loaded from {CONFIG_FILE}")
        return config
    except Exception as e:
        print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} Failed to load config: {e}")
        sys.exit(1)


def resolve_path(base, rel):
    return os.path.normpath(os.path.join(base, rel))


def create_link(source, dest, dry_run=False, verbose=True):
    system = platform.system()

    if dry_run:
        print(f"{Fore.MAGENTA}[DRY-RUN]{Style.RESET_ALL} Would link: {dest} → {source}")
        return True

    # Clean existing
    if os.path.exists(dest):
        if verbose:
            print(f"{Fore.YELLOW}[Cleaning]{Style.RESET_ALL} Removing: {dest}")
        try:
            if os.path.islink(dest):
                os.remove(dest)
            elif os.path.isdir(dest):
                shutil.rmtree(dest)
            else:
                print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} Blocking file (not folder/link): {dest}")
                return False
        except Exception as e:
            print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} Failed to clean {dest}: {e}")
            return False

    os.makedirs(os.path.dirname(dest), exist_ok=True)

    try:
        if system == "Windows":
            if verbose:
                print(f"{Fore.CYAN}[Linking]{Style.RESET_ALL} Junction: {dest}")
            result = subprocess.call(['mklink', '/J', dest, source], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            success = (result == 0)
        else:
            if verbose:
                print(f"{Fore.CYAN}[Linking]{Style.RESET_ALL} Symlink: {dest}")
            os.symlink(source, dest)
            success = True
    except Exception as e:
        print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} Link failed: {e}")
        success = False

    if success and verbose:
        print(f"{Fore.GREEN}[SUCCESS]{Style.RESET_ALL} {dest}")
    return success


def verify_links(config):
    source_base = os.path.abspath(config["source_base"])
    comfyui_root = os.path.abspath(config["comfyui_root"])

    print(f"\n{Fore.CYAN}VERIFYING LINKS{Style.RESET_ALL}")
    print(f"Source:  {source_base}")
    print(f"ComfyUI: {comfyui_root}\n")

    all_good = True
    checked = 0

    # Standard folders
    for folder in config["folders"]:
        source = resolve_path(source_base, folder)
        dest = resolve_path(comfyui_root, f"models/{folder}")
        checked += 1

        if not os.path.exists(source):
            print(f"{Fore.YELLOW}[MISSING SOURCE]{Style.RESET_ALL} {source}")
            all_good = False
            continue

        if not os.path.exists(dest):
            print(f"{Fore.RED}[BROKEN]{Style.RESET_ALL} Missing link: {dest}")
            all_good = False
        elif platform.system() == "Windows" and not os.path.isdir(dest):
            print(f"{Fore.RED}[INVALID]{Style.RESET_ALL} Not a junction: {dest}")
            all_good = False
        elif not os.path.islink(dest) and platform.system() != "Windows":
            print(f"{Fore.RED}[INVALID]{Style.RESET_ALL} Not a symlink: {dest}")
            all_good = False
        else:
            print(f"{Fore.GREEN}[OK]{Style.RESET_ALL} {dest}")

    # Special links
    for rel_dest, subfolder in config["special_links"].items():
        source = resolve_path(source_base, subfolder)
        dest = resolve_path(comfyui_root, rel_dest)
        checked += 1

        if not os.path.exists(source):
            print(f"{Fore.YELLOW}[MISSING SOURCE]{Style.RESET_ALL} {source}")
            all_good = False
            continue

        if not os.path.exists(dest):
            print(f"{Fore.RED}[BROKEN]{Style.RESET_ALL} Missing: {dest}")
            all_good = False
        else:
            print(f"{Fore.GREEN}[OK]{Style.RESET_ALL} {dest}")

    print(f"\n{Fore.CYAN}Verification complete: {checked} items checked.{Style.RESET_ALL}")
    if all_good:
        print(f"{Fore.GREEN}All links are valid!{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Some issues found. Run without --verify to repair.{Style.RESET_ALL}")


def main():
    parser = argparse.ArgumentParser(description="ComfyUI Portable Model Linker (Cross-Platform)")
    parser.add_argument("-v", "--verify", action="store_true", help="Verify existing links instead of creating")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be done without changes")
    args = parser.parse_args()

    config = load_config()

    # Override dry_run from CLI
    if args.dry_run:
        config["dry_run"] = True

    if args.verify:
        verify_links(config)
        input("\nPress Enter to exit...")
        return

    source_base = os.path.abspath(config["source_base"])
    comfyui_root = os.path.abspath(config["comfyui_root"])
    dry_run = config["dry_run"]
    verbose = config["verbose"]

    print("=========================================================")
    print("     COMFYUI PORTABLE MODEL LINKER (Cross-Platform)")
    print("=========================================================")

    if not os.path.exists(source_base):
        print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} Source directory not found: {source_base}")
        print("    Check your config_links.json")
        input("\nPress Enter to exit...")
        sys.exit(1)

    print(f"Source:      {source_base}")
    print(f"ComfyUI Root: {comfyui_root}")
    print(f"Platform:    {platform.system()}")
    print(f"Dry Run:     {dry_run}")
    print("---------------------------------------------------------\n")

    success_count = 0
    total = len(config["folders"]) + len(config["special_links"])

    abs_source_base = source_base
    abs_comfyui_root = comfyui_root

    # Standard folders
    for folder in config["folders"]:
        source = resolve_path(abs_source_base, folder)
        dest = resolve_path(abs_comfyui_root, f"models/{folder}")

        if not os.path.exists(source):
            if verbose:
                print(f"{Fore.YELLOW}[SKIP]{Style.RESET_ALL} Source missing: {source}")
            continue

        if create_link(source, dest, dry_run, verbose):
            success_count += 1

    # Special links
    for rel_dest, subfolder in config["special_links"].items():
        source = resolve_path(abs_source_base, subfolder)
        dest = resolve_path(abs_comfyui_root, rel_dest)

        if not os.path.exists(source):
            if verbose:
                print(f"{Fore.YELLOW}[SKIP]{Style.RESET_ALL} Source missing: {source}")
            continue

        if create_link(source, dest, dry_run, verbose):
            success_count += 1

    print("---------------------------------------------------------")
    if dry_run:
        print(f"{Fore.MAGENTA}[DRY-RUN COMPLETE]{Style.RESET_ALL} {success_count}/{total} links would be created.")
    else:
        print(f"{Fore.GREEN}[COMPLETE]{Style.RESET_ALL} {success_count}/{total} links created successfully.")
    print("=========================================================")

    if not dry_run:
        input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()
