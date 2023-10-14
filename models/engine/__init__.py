#!/bin/usr/python3
"""init for models"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
