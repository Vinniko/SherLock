from Interfaces.IReader import IReader

class FileReader(IReader):
    """ Read in files class """
    
    def __init__(self):
        pass

    def Read(self, path):
        with(open(path, 'r')) as file:
            return file.read()

   


