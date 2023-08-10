import os
import tkinter as tk
from tkinter import filedialog

def create_files_with_content(template_folder, base_folder, destination_folder=""):
    for item in os.listdir(template_folder):
        item_path = os.path.join(template_folder, item)
        relative_item_path = os.path.relpath(item_path, template_folder)

        if os.path.isdir(item_path):
            if item != "files_templates":
                create_files_with_content(item_path, base_folder, os.path.join(destination_folder, item))
        else:
            if item.endswith("-template.txt"):
                new_filename = os.path.splitext(item)[0].replace("-template", "").replace("template.txt", "")
                if "-" in new_filename:  # If the filename contains hyphen
                    new_filename = new_filename.replace("-", ".")
                elif "_" in new_filename:  # If the filename contains underscore
                    new_filename = new_filename.replace("_", ".")
                else:
                    new_filename += "__keep_folder.empty"  # Assuming .php for files without hyphen or underscore

                destination_path = os.path.join(base_folder, destination_folder)
                if not os.path.exists(destination_path):
                    os.makedirs(destination_path)

                new_file_path = os.path.join(destination_path, new_filename)

                with open(item_path, 'r') as template_file:
                    content = template_file.read()

                with open(new_file_path, 'w') as new_file:
                    new_file.write(content)
                    print(f"Created file: {new_file_path}")

def remove_empty_files(base_folder):
    for root, _, files in os.walk(base_folder):
        for file in files:
            full_path = os.path.join(root, file)
            if file == "__keep_folder.empty":
                os.remove(full_path)

def main():
    root = tk.Tk()
    root.withdraw()

    destination_path = filedialog.askdirectory(title="Select Destination Folder")

    if not destination_path:
        print("No destination folder selected. Exiting.")
        return

    project_name = input("Enter the name of the project folder: ")
    base_folder = os.path.join(destination_path, project_name)
    
    if not os.path.exists(base_folder):
        os.makedirs(base_folder)

    templates_folder = "files_templates"

    create_files_with_content(templates_folder, base_folder)
    remove_empty_files(base_folder)

if __name__ == "__main__":
    main()
