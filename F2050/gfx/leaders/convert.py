#!/usr/bin/env python
import os
from PIL import Image
import sys

def convert_images(directory):
    # Counter for converted files
    converted_count = 0
    found_files = 0
    
    print(f"Searching in directory: {os.path.abspath(directory)}")
    
    # Walk through all directories and subdirectories
    for root, dirs, files in os.walk(directory):
        print(f"Checking directory: {root}")
        for file in files:
            # Check if file is .dds or .tga
            if file.lower().endswith(('.dds', '.tga')):
                found_files += 1
                file_path = os.path.join(root, file)
                print(f"Found file: {file_path}")
                
                try:
                    # Create the new filename with .png extension
                    png_path = os.path.splitext(file_path)[0] + '.png'
                    
                    # Open and convert the image
                    print(f"Attempting to convert {file}")
                    with Image.open(file_path) as img:
                        # Convert to RGB if necessary
                        if img.mode != 'RGB':
                            img = img.convert('RGB')
                        
                        # Save as PNG
                        img.save(png_path, 'PNG')
                    
                    # Delete the original file
                    os.remove(file_path)
                    
                    converted_count += 1
                    print(f"Successfully converted: {file}")
                    
                except Exception as e:
                    print(f"Error converting {file}: {str(e)}")
    
    return converted_count, found_files

def main():
    # Use current directory if no argument is provided
    directory = sys.argv[1] if len(sys.argv) > 1 else '.'
    
    print(f"Starting conversion in directory: {os.path.abspath(directory)}")
    print("This will convert all .dds and .tga files to .png and delete the originals.")
    
    # Confirm with user
    response = input("Do you want to continue? (y/n): ")
    if response.lower() != 'y':
        print("Operation cancelled.")
        return
    
    # Perform conversion
    converted, found = convert_images(directory)
    
    print(f"\nConversion complete!")
    print(f"Files found: {found}")
    print(f"Files successfully converted: {converted}")

if __name__ == "__main__":
    main()