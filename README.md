# File Sorter by Extension

A simple Python script to organize files into folders based on their extensions.

## How it works

This script scans a folder and moves each file into a subfolder like `Documents`, `Videos`, `Images`, etc., depending on the file extension.

## Usage

```bash
# Run in the current folder
python filesort.py

# Run in a specific folder
python filesort.py /path/to/your/folder
```

## File categories

| Category        | Extensions                                              |
| --------------- | ------------------------------------------------------- |
| **Images**      | `.jpg`, `.jpeg`, `.png`, `.gif`, `.svg`, `.webp`        |
| **Videos**      | `.mp4`, `.mkv`, `.mov`, `.m4v`, `.aep`                  |
| **Audio**       | `.mp3`, `.wav`, `.m4a`                                  |
| **Documents**   | `.pdf`, `.doc`, `.docx`, `.ppt`, `.pptx`, `.txt`, `.md` |
| **Executables** | `.exe`, `.sh`, `.bat`, `.jar`, `.appimage`, `.apk`      |
| **Compressed**  | `.zip`, `.rar`, `.7z`, `.tar`, `.gz`, `.bz2`            |
| **Data**        | `.csv`, `.xls`, `.xlsx`, `.db`, `.sql`, `.sqlite`       |
| **Disk Images** | `.iso`, `.rom`, `.dvd`                                  |
| **Fonts**       | `.ttf`, `.otf`, `.ttc`                                  |
| **Others**      | Any unknown extension                                   |

## License

This project is licensed under the **MIT License**.
