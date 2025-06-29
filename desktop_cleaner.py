import os
import shutil

def clean_folder(path):
    file_types = {
        'Images': ['.png', '.jpg', '.jpeg', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.doc', '.ppt'],
        'Videos': ['.mp4', '.mov', '.avi'],
        'Musics':['.mp3','.wave'],
        'Archives': ['.zip', '.rar'],
        'Graphics': ['.cdr', '.ai']
    }

    for file in os.listdir(path):
        full_path = os.path.join(path, file)
        if os.path.isfile(full_path):
            ext = os.path.splitext(file)[1].lower()
            for folder, extensions in file_types.items():
                if ext in extensions:
                    target_dir = os.path.join(path, folder)
                    os.makedirs(target_dir, exist_ok=True)
                    shutil.move(full_path, os.path.join(target_dir, file))
                    break
    print("Folder cleaned and organized successfully.")

if __name__ == "__main__":
    folder_path = input("Enter path to the folder you want to organize: ")
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        clean_folder(folder_path)
    else:
        print("The provided path is invalid.")
