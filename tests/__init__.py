import sys
import os
from pathlib import Path

# Add stuff to sys.path
# Since this isn't exactly a module this needs to be done so that imports
# work.
sys.path.extend(
    [
        os.fspath(Path(__file__).parent.parent / "tools"),
        os.fspath(Path(__file__).parent.parent),
    ]
)
