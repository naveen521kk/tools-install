from pathlib import Path
import tomli

DATA_DIR = Path(__file__).parent.parent / "data"

def get_data(tool_name: str):
    """Get the data from the file."""
    with open(DATA_DIR / f"{tool_name}.toml", "rb") as f:
        return tomli.load(f)
