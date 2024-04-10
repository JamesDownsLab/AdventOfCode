from pathlib import Path

def load_input_to_list(filename: Path) -> list[str]:
    with open(filename, 'r') as f:
        lines: list[str] = f.readlines()
    return lines
