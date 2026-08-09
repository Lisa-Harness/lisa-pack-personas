from pathlib import Path


def get_content_root() -> Path:
    return Path(__file__).parent