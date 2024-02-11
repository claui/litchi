"""
.. include:: ../README.md

## API Documentation
"""

# Re-export these symbols
# (This promotes them from litchi_downloader.api to litchi_downloader)
from litchi_downloader.api import hello as hello

__all__ = [
    # Tell pdoc to pick up all re-exported symbols
    'hello',

    # Modules that every subpackage should see
    # (This also exposes them to pdoc)
    'api',
    'settings',
]
