#!/usr/bin/python3
"""Executes each time when the 'models' package is imported"""
from models.file_storage import FileStorage


storage = FileStorage()
storage.reload()
