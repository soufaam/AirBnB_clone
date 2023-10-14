#!/usr/bin/python3
"""
init file to make moedels package
"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
