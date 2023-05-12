import os
import sys
from time import sleep
from rich.console import Console

console = Console()
tasks = [f"hex {n}" for n in range(1, 5)]

with console.status("[bold green]Working on tasks...") as status:
    while tasks:
        hex_ = tasks.pop(0)
        sleep(0.9)
        console.log(f"{hex_} complete")


FILE_TYPES = {
    ".zip": b"\x50\x4B\x03\x04",
    ".rar": b"\x52\x61\x72\x21\x1A\x07\x00",
    ".png": b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A\x00\x00\x00\x0D\x49\x48\x44\x52",
    ".jpg": b"\xFF\xD8\xFF\xe0\x00\x10\x4a\x46\x49\x46\x00\x01\x01\x00\x00\x01",
    ".jpeg": b"\xFF\xD8\xFF",
    ".mp3": b"\xFF\xFB",
    ".mp4": b"\x00\x00\x00\x18\x66\x74\x79\x70",
    ".pdf": b"\x25\x50\x44\x46\x2D",
    ".doc": b"\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1",
    ".docx": b"\x50\x4B\x03\x04\x14\x00\x06\x00",
    ".xls": b"\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1",
    ".xlsx": b"\x50\x4B\x03\x04\x14\x00\x06\x00",
    ".ppt": b"\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1",
    ".pptx": b"\x50\x4B\x03\x04\x14\x00\x06\x00",
    ".gif": b"\x47\x49\x46\x38\x39\x61",
    ".tif": b"\x49\x49\x2A\x00",
    ".tiff": b"\x49\x49\x2A\x00",
    ".bmp": b"\x42\x4D",
    ".avi": b"\x52\x49\x46\x46\x28\x00\x00\x00\x41\x56\x49\x20",
    ".wav": b"\x52\x49\x46\x46\x24\x08\x00\x00\x57\x41\x56\x45",
    ".mov": b"\x00\x00\x00\x20\x6D\x6F\x6F\x76",
}

def fix_header(file_path, output_file):
    """Fix the header of a file based on its extension"""
    file_ext = os.path.splitext(file_path)[1].lower()
    if file_ext in FILE_TYPES:
        header = FILE_TYPES[file_ext]
        with open(file_path, "rb") as f:
            data = f.read()
        if data.startswith(header):
            print(f"Header of {file_path} already correct.")
        else:
            with open(output_file, "wb") as f:
                f.write(header + data[len(header):])
            print(f"Header of {file_path} fixed and saved to {output_file}.")
    else:
        print(f"File extension {file_ext} not supported.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python FIXH.py input_file output_file")
    else:
        fix_header(sys.argv[1], sys.argv[2])
