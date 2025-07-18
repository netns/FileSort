import sys
from pathlib import Path

USAGE = """
Usage:
    python3 filesort.py [path_to_directory]

If no path is provided, the current working directory is used.

Options:
    -h, --help      Show this help message.
"""

CATEGORIES = {
    # fmt: off
    "Executables": {".apk", ".exe", ".jar", ".bat", ".bin", ".appimage", ".sh", ".dll"},
    "Audios": {".mp3", ".m4a", ".wav"},
    "Videos": {".mkv", ".aep", ".mp4", ".m4v", ".mov"},
    "Images": {".jpeg", ".jpg", ".png", ".svg", ".gif", ".webp"},
    "Documents": {".doc", ".docx", ".odt", ".tex", ".txt", ".md", ".pptx", ".ppt", ".pdf", ".ods", ".log"},
    "Data": {".db", ".sqlite", ".sql", ".odb", ".xlsx", ".xls", ".dat", ".csv"},
    "Compresseds": {".7z", ".deb", ".gz", ".pkg",".rar", ".rpm", ".gz", ".bz2", ".tar", ".zip"},
    "DiskImages" : {".iso", ".rom", ".dvd"},
    "Fonts" : {".ttf", ".otf", ".ttc"}
    # fmt: on
}

EXTENSIONS = {
    extension: category
    for category, extensions in CATEGORIES.items()
    for extension in extensions
}


def sort_files(dir: Path) -> None:
    for item in dir.iterdir():
        if item.is_file():
            suffix = item.suffix.lower()
            category = EXTENSIONS.get(suffix, "Others")
            new_dir = dir / category
            new_dir.mkdir(exist_ok=True)
            try:
                item.rename(str(new_dir / item.name))
                print(f"Moved: {item.name} --> {category}")
            except PermissionError:
                print(f"Permission denied: could not move the file {file}")
            except Exception as e:
                print(f"Error while moving '{item.name}': {e}")


def cli():
    if len(sys.argv) < 2:
        path = Path.cwd()

    if sys.argv[1] in ["-h", "--help"]:
        print(USAGE)
        sys.exit(0)

    else:
        path = Path(sys.argv[1])
        if not path.is_dir():
            print(f"Error: {path} is not a valid directory")
            sys.exit(1)

    print(f"Organizing files in: {path}")
    sort_files(path)


if __name__ == "__main__":
    cli()
