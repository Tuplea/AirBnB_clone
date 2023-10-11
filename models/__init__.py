#!/usr/bin/python3
"""init model to reload the objects from file when program starts"""


from models.engine.file_storage import FileStorage

storage = FileStorage()

storage.reload()
