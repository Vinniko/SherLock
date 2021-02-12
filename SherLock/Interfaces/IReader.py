from abc import ABCMeta, abstractmethod

class IReader(object):
    """  Class for reading information  
        
     Open methods:
     Read
    """
    
    @abstractmethod
    def Read(self):
        """ Reading information """
        pass


