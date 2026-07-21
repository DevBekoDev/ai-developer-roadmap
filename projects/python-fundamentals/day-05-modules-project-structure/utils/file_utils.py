from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[4]
DATA_FOLDER = REPOSITORY_ROOT / "data"


def get_data_file(filename: str) -> Path:
    """Return the path to a file inside the repository data folder."""
    return DATA_FOLDER / filename