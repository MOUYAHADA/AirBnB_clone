#!/usr/bin/python3
"""
Init module
"""
from models.engine.file_storage import FileStorage
import models

storage = FileStorage()
storage.reload()
