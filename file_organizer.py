from pathlib import Path
import shutil

def create_folders(base_path: Path, folder_names: list[str]) -> None:

    base_path.mkdir(parents=True, exist_ok=True)

    # Create subfolders
    for name in folder_names:
        full_path = base_path / name
        full_path.mkdir(exist_ok=True)

def organize_files_by_extension(path_to_folder_with_files: Path, path_to_organized_folder: Path) -> None:

    # Mapping extensions to predefined folders
    map_extensions = {
    'csv': 'csv',
    'html': 'html',
    'json': 'json',
    'pdf': 'pdf',
    'py': 'py',
    'txt': 'txt',
    'xlsx': 'xlsx',
    'xls': 'xlsx'
    }

    # Process each file in the source directory
    for file in path_to_folder_with_files.iterdir():
        if file.is_file():
            
            extension = file.suffix[1:].lower()

        target_folder = map_extensions.get(extension, extension)
        target_path = path_to_organized_folder / target_folder

        # Copy the file if the destination directory exists
        if target_path.exists() and target_path.is_dir():
            shutil.copy(str(file), str(target_path / file.name))
            print(f"Moved: {file.name} -> {target_folder}")

def create_compressed_backup(backup_folder, folder_to_be_compressed, backup_filename):
    backup_folder.mkdir(parents=True, exist_ok=True)
    shutil.make_archive(backup_filename, 'zip', folder_to_be_compressed)

if __name__ == "__main__":

    current_folder = Path(__file__).parent
    destination_path = current_folder / 'organized'
    folders = ['csv', 'html', 'json', 'pdf', 'py', 'txt', 'xlsx']
    path_to_folder_with_files = current_folder / 'example_files'
    backup_folder = current_folder / 'backups'
    backup_file_name = backup_folder / 'Backup_Files'
    folder_to_be_compressed = destination_path

    create_folders(destination_path, folders)
    organize_files_by_extension(path_to_folder_with_files, destination_path)
    create_compressed_backup(backup_folder, folder_to_be_compressed, backup_file_name)