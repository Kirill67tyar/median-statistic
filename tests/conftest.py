from pathlib import Path

import pytest


@pytest.fixture
def write_csv():
    def _write_csv(path: Path, content: str) -> Path:
        path.write_text(content, encoding="utf-8")
        return path

    return _write_csv