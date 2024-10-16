#!/usr/bin/env python
import os  # Added this import
from PIL import Image

log = False

# Initialize the gfxfile content
gfxfile = "spriteTypes = {"

# Collect entry names from png files
entry_names = []
png_count = 0  # Initialize counter for PNG files

# Walk through the gfx/leaders directory
for folder in os.walk('./gfx/leaders/'):
    if folder[0] != ".":
        for orig_file_name in folder[2]:
            if ".png" in orig_file_name:
                png_count += 1  # Increment counter for each PNG file
                entry_name = orig_file_name[:len(orig_file_name)-4]
                entry_names.append(entry_name)
                if log: print(entry_name)
                folder_name = folder[0][2:]
                gfxfile += F"""
    spriteType = {{
        name = "GFX_{entry_name}"
        texturefile = "{folder_name}/{orig_file_name}"
    }}"""

# Add the total number of PNG files at the top of the file
header = f"# Total number of PNG files: {png_count}\n\n"
gfxfile = header + gfxfile + "\n\n}"

if log: print(gfxfile)

# Write to interface/FPW_Leaders.gfx
with open("interface/FPW_Leaders.gfx", "w") as file:
    file.truncate(0)
    file.write(gfxfile)