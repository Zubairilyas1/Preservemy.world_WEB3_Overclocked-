# simple pixel metadata check tool for 3D datasets
import os

print("--- PMW Dataset Pre-check Script Initialized ---")
# Check if a file exists
sample_path = "README.md"

if os.path.exists(sample_path):
    size_bytes = os.path.getsize(sample_path)
    print(f"Target file found: {sample_path}")
    print(f"File Size: {size_bytes / 1024:.2f} KB")
else:
    print("No target file found yet. Script loop executed cleanly.")
print("--- Check Complete ---")