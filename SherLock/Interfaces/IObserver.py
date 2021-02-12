from abc import ABCMeta, abstractmethod

class IObserver(object): 
    """  Class for implementing Observable pattern  
        
        Open methods:
        Update
    """

    
    @abstractmethod
    def Update(self, object):
        """ Updating some information when method is called
       
        Keywords arguments:
        object - information, wchich replaces old information

        """
        pass




