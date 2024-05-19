#!/usr/bin/python3
"""
Init module
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
