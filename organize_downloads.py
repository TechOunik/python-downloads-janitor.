#!/usr/bin/env python3
import os
import shutil
from pathlib import Path

def organize_downloads():
    print("=========================================")
    print("     INITIATING DOWNLOADS CLEANUP        ")
    print("=========================================")

    # Pathlib's 'home()' is the most reliable way to find the user profile 
    # regardless of the Operating System (Windows, Linux, or Mac).
    downloads_path = Path.home() / "Downloads"

    # Define the "Triage" categories and their associated extensions
    file_categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp"],
        "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".csv", ".xlsx"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov"],
        "Music": [".mp3", ".wav", ".aac"],
        "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
        "Software_and_Scripts": [".deb", ".py", ".sh", ".bin", ".AppImage", ".exe", ".msi"]
    }

    if not downloads_path.exists():
        print(f"❌ Error: Could not find the Downloads folder at {downloads_path}")
        return

    print(f"📂 Scanning target directory: {downloads_path}\n")
    moved_count = 0

    # Iterate through the directory
    for file_path in downloads_path.iterdir():
        
       # Step 1: Only triage FILES. We ignore folders so we don't move a folder into itself!
        if file_path.is_file():
            
            # Grab the extension and force it to lowercase (no hiding from the Janitor)
            file_ext = file_path.suffix.lower()
            moved = False
            
            # Triage: Check the dictionary to see which 'VIP Lounge' this file belongs to
            for folder_name, extensions in file_categories.items():
                if file_ext in extensions:
                    dest_folder = downloads_path / folder_name
                    
                    # If the lounge doesn't exist, we build it on the fly
                    dest_folder.mkdir(exist_ok=True)
                    
                    # The muscle: Move the file to its new home
                    shutil.move(str(file_path), str(dest_folder / file_path.name))
                    print(f"✅ Moved: {file_path.name}  ➡️  {folder_name}/")
                    moved_count += 1
                    moved = True
                    break
            
            # If the file extension is a mystery, send it to 'Others' for quarantine
            if not moved and file_ext != "":
                others_folder = downloads_path / "Others"
                others_folder.mkdir(exist_ok=True)
                shutil.move(str(file_path), str(others_folder / file_path.name))
                print(f"📦 Moved: {file_path.name}  ➡️  Others/")
                moved_count += 1
                
    print("\n=========================================")
    print(f"✨ CLEANUP COMPLETE! Successfully organized {moved_count} files. ✨")
    print("Your workspace is now ready for deep work.")
    print("=========================================")

if __name__ == "__main__":
    organize_downloads()
