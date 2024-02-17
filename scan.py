import os
import glob
import enum

"""Scans for existing music files"""
class Scanner:

    # Directory levels. Set to -1 if not present. Highest level is 0.
    artist_level = 0 # Which folder level contains artist names
    album_level = 1 # Which folder level contains album names
    title_level = -1 # Which folder level contains titles

    class Loc(enum): # Used to configure settings below
        Filename = 0, # Get info from filename (files must be named correctly)
        Metadata = 1, # Get info from file metadata (files must be annotated with metadata)
        Foldername = 2, # Get info from the title level (must be present and enabled above)
    
    artist_location = Loc.Filename # Where to get artist info
    title_location = Loc.Metadata # Where to get file title

    max_depth = max(1, artist_level, album_level, title_level) # maximum depth to check for files

    def __init__(self) -> None:
        pass

    def scan(self):
        cur_path=os.path.curdir
        dir_made = self.traverse(cur_path, 0)
        print(dir_made)
        
    def traverse(self, dir_path:str, depth:int) -> list:
        if depth > self.max_depth:
            return
        for root, dirs, files in os.walk(dir_path):
            for dir in dirs:
                self.traverse(os.path.join(dir_path, dir), depth+1)
                
            for file in files:



    def handle_file():
        