import os
import shutil
import time


# --- Create unique filenames if same name exists ---
def get_unique_path(dest_path):
    folder, filename = os.path.split(dest_path)
    name, ext = os.path.splitext(filename)

    counter = 1
    new_path = dest_path

    while os.path.exists(new_path):
        new_filename = f"{name} ({counter}){ext}"
        new_path = os.path.join(folder, new_filename)
        counter += 1

    return new_path


# --- Move file safely ---
def move_files(file_path, destination_path):
    destination_folder = os.path.dirname(destination_path)

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Try moving 5 times
    for _ in range(5):
        try:
            # make unique name if needed
            destination_path = get_unique_path(destination_path)
            shutil.move(file_path, destination_path)
            print(f"Moved: {file_path} -> {destination_path}")
            break
        except PermissionError:
            time.sleep(0.5)
        except Exception as e:
            print(f"Error: {e}")
            break


# --- File categories ---
FILE_TYPES = {
    "Documents": [".pdf", ".docx", ".txt"],
    "Images": [".jpg", ".jpeg", ".png"],
    "Videos": [".mp4", ".mov"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"]
}


# --- Organize folder ---
def organize_folder(folder_path):
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        if os.path.isfile(file_path):
            ext = os.path.splitext(file_name)[1].lower()
            moved = False

            # Check matching file types
            for folder, extensions in FILE_TYPES.items():
                if ext in extensions:
                    destination = os.path.join(folder_path, folder, file_name)
                    move_files(file_path, destination)
                    moved = True
                    break

            if not moved:
                destination = os.path.join(folder_path, "others", file_name)
                move_files(file_path, destination)


if __name__ == "__main__":
    folder_to_organize = input("Enter folder path: ")
    organize_folder(folder_to_organize)





