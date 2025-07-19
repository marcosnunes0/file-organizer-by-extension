# 📁 File Organizer by Extension

![Python](https://img.shields.io/badge/Python-%3E%3D3.11-05122A?logo=python&style=flat) ![License](https://img.shields.io/badge/License-MIT-05122A?style=flat)

> A simple Python utility that automatically organizes files into folders by extension and creates compressed backups.

---

## 📝 Overview

**File Organizer by Extension** is a lightweight command‑line tool that helps you:

- 📂 **Categorize** files from any folder into subdirectories named after their extensions (e.g., `.csv` → `csv/`, `.py` → `py/`).

- 🔄 **Maintain backups** by compressing the organized folders into a ZIP archive for safekeeping.  

This script uses pure Python (`pathlib`, `shutil`) and requires no complex dependencies.

---

## ✨ Key Features

- **Automated Folder Creation**

  – Generates subfolders (`csv`, `html`, `json`, `pdf`, `py`, `txt`, `xlsx`) under an `organized/` directory.  

- **Extension‑Based Organization**

  – Scans source directory (`example_files/` by default) and copies each file to its corresponding folder.  

- **Backup Compression**

  – Creates a ZIP archive (`backups/Backup_Files.zip`) of the entire `organized/` directory.  

- **Customizable Mapping**

  – Easily extend `map_extensions` in `file_organizer.py` to include new extensions or rename targets.  

---

## 🛠️ Tech Stack

| Component         | Library / Module      |
|-------------------|-----------------------|
| File System I/O   | `pathlib`, `shutil`   |
| Compression       | `shutil.make_archive` |
| Command‑line      | Python 3.11            |

---

## 🚀 Installation & Setup

1. **Clone the repository**  
```bash
   git clone https://github.com/marcosnunes0/file-organizer-by-extension.git
   cd file-organizer-by-extension
```

2. **(Optional) Create a virtual environment**

 ```bash
    python3 -m venv venv
    source venv/bin/activate
```

3. **Install dependencies**

- No external packages required beyond the Python standard library.

## ▶️ Usage

1. **Place your files**

    – Copy all files you want to organize into the `example_files/` folder.

2. **Run the script**
    ```bash
    python file_organizer.py
    ```

    – This will:

    1. Create an `organized/` folder with subdirectories for each extension.

    2. Copy files from `example_files/` into their respective subfolders.

    3. Generate a ZIP backup in `backups/Backup_Files.zip`.

3. **Inspect results**

    – Organized files: `organized/<extension>/`

    – Backup archive: `backups/Backup_Files.zip`

## 📂 Example Directory Structure

```bash
.
├── backups/
│   └── Backup_Files.zip
├── example_files/
│   ├── sample1.csv
│   └── notes.txt
├── organized/
│   ├── csv/
│   │   └── sample1.csv
│   └── txt/
│       └── notes.txt
├── file_organizer.py
└── LICENSE
```

## ⚙️ Configuration

- **Source Folder**

    – Default: `example_files/`

    – Change by editing `path_to_folder_with_files` in `file_organizer.py`.

- **Organized Folder**

    – Default: `organized/`
    – Change via `destination_path` variable.

- **Extension Mapping**

    – Located in the map_extensions dictionary — add or modify key/value pairs to adjust folder names.

- **Backup Location & Name**

    – Configured by `backup_folder` and `backup_file_name` variables — customize ZIP path and filename.

## 📄 License

This project is licensed under the **MIT License**. See [LICENSE](https://github.com/marcosnunes0/file-organizer-by-extension/blob/main/LICENSE) for details.
