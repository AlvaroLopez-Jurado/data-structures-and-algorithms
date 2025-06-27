import os
import shutil

def generate_tree(startpath):
    tree_lines = []

    def walk_dir(current_path, prefix=""):
        entries = sorted(os.listdir(current_path))
        entries = [e for e in entries if e != '__pycache__']
        entries_count = len(entries)

        for index, entry in enumerate(entries):
            path = os.path.join(current_path, entry)
            connector = "└── " if index == entries_count - 1 else "├── "
            tree_lines.append(f"{prefix}{connector}{entry}/" if os.path.isdir(path) else f"{prefix}{connector}{entry}")

            if os.path.isdir(path):
                extension = "    " if index == entries_count - 1 else "│   "
                walk_dir(path, prefix + extension)

    base_name = os.path.basename(os.path.abspath(startpath))
    tree_lines.append(f"{base_name}/")
    walk_dir(startpath)

    return "\n".join(tree_lines)

def delete_pycache_folders(startpath="."):
    """
    Recursively deletes all __pycache__ folders from the given directory.
    
    Args:
        startpath (str): The root directory to start the search from.
    """
    for root, dirs, files in os.walk(startpath):
        for dir_name in dirs:
            if dir_name == "__pycache__":
                pycache_path = os.path.join(root, dir_name)
                shutil.rmtree(pycache_path)
                print(f"Deleted: {pycache_path}")

if __name__ == "__main__":
    tree_output = generate_tree(".")
    with open("file.md", "w", encoding="utf-8") as f:
        f.write("```text\n")
        f.write(tree_output)
        f.write("\n```")
    delete_pycache_folders()