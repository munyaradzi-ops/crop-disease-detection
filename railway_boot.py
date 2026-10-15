import os
import subprocess
import sys

print("🔄 Running Railway pre-boot script to clear stuck cache dependencies...")

try:
    # 1. Force uninstall the broken standard graphical package
    print("🧹 Purging old graphical opencv-python references...")
    subprocess.run([sys.executable, "-m", "pip", "uninstall", "opencv-python", "-y"], check=True)
    
    # 2. Force reinstall the pure headless container-safe variant
    print("📦 Injecting headless cloud-optimized dependencies...")
    subprocess.run([sys.executable, "-m", "pip", "install", "opencv-python-headless"], check=True)
    
    print("✅ Pre-boot dependency alignment completed successfully!")
except Exception as e:
    print(f"⚠️ Pre-boot warning: {e} (Continuing execution...)")
