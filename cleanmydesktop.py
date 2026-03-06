# The Downloads Organizer 
import os
import shutil

print("=========================================")
print(" INITIATING DOWNLOADS CLEANUP ")
print("=========================================")

# This dynamically grabs the exact path to your Downloads folder
downloads_path = os.path.expanduser("~/Downloads")

# We define a dictionary to map folder names to their matching file extensions
file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".csv", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
    "Software_and_Scripts": [".deb", ".py", ".sh", ".bin", ".AppImage"]
}

print(f"Scanning target directory: {downloads_path}\n")
moved_count = 0

# Loop through every item in your Downloads folder
for filename in os.listdir(downloads_path):
    file_path = os.path.join(downloads_path, filename)
    
    # We only want to move files, NOT existing folders
    if os.path.isfile(file_path):
        
        # Extract the file extension (e.g., '.pdf') and make it lowercase
        file_ext = os.path.splitext(filename)[1].lower()
        moved = False
        
        # Check our dictionary to see where this file belongs
        for folder_name, extensions in file_categories.items():
            if file_ext in extensions:
                
                # Create the category folder if it doesn't exist yet
                dest_folder = os.path.join(downloads_path, folder_name)
                if not os.path.exists(dest_folder):
                    os.mkdir(dest_folder)
                
                # Move the file!
                shutil.move(file_path, os.path.join(dest_folder, filename))
                print(f"✅ Moved: {filename}  ➡️  {folder_name}/")
                moved_count += 1
                moved = True
                break # Stop searching categories once we found a match
                
        # If the file extension wasn't in our dictionary, put it in an 'Others' folder
        if not moved and file_ext != "":
            dest_folder = os.path.join(downloads_path, "Others")
            if not os.path.exists(dest_folder):
                os.mkdir(dest_folder)
            shutil.move(file_path, os.path.join(dest_folder, filename))
            print(f"📦 Moved: {filename}  ➡️  Others/")
            moved_count += 1

print("\n=========================================")
print(f"✨ CLEANUP COMPLETE! Successfully organized {moved_count} files. ✨")
print("Open your Downloads folder and admire your work!")
