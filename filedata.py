
"""Represents a file"""
class FileInfo:
    filename:str
    ext:str # File extension
    metadata:dict # File metadata as key-value pairs

    def get_artist(self):
        if self.metadata is None:
            return None
        return self.metadata.get("artist",None)
    
    def get_title(self):
        if self.metadata is None:
            return None
        return self.metadata.get("title",None)