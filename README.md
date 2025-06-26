# Illustrator XML Variable Maker

A simple GUI tool to convert Excel (`.xlsx`) data into Adobe Illustrator-compatible XML variable files.

## Features

- 🧾 Import Excel spreadsheets using `openpyxl`
- 🎨 Generate XML variable files for Illustrator automation
- 🖼️ User-friendly GUI using `tkinter`
- 📦 Single-file executable for Windows (via PyInstaller)

## Installation

You can install it locally using [uv](https://github.com/astral-sh/uv) or `pip`:

```bash
uv pip install -e .
# or
pip install -e .
```

## Requirements

- Python 3.10 or higher
- `openpyxl`
- `tkinter` (bundled with Python on Windows)

## Running the App

```bash
python main.py
```

Alternatively, if you want to run directly from the GUI module:

```bash
python ui/app.py
```

## Building Executable

You can create a standalone Windows `.exe` using:

```bash
pyinstaller --onefile --noconsole ui/app.py --name illustrator_xml_gui
```

The output will be located in the `dist/` folder.

## Folder Structure

```
illustrator_xml_variable_maker/
├── .github/workflows/        # GitHub Actions for CI/CD
├── src/
│   └── core/
│       ├── converter.py
│       └── file_utils.py
├── ui/
│   └── app.py                # Entry point for GUI
├── main.py                   # Alternate entry point
├── pyproject.toml
└── README.md
```

## Versioning

This project uses Git tags for versioning. The executable version is automatically synced from the latest Git tag.

## License

[MIT](LICENSE)
