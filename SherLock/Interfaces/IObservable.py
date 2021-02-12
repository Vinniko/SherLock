from abc import ABCMeta, abstractmethod

class IObservable(object):
    """  Class for implementing Observable pattern  
        
        Open methods:
        RegisterObserver
        RemoveObserver
        NotifyObservers
    """
    
    @abstractmethod
    def RegisterObserver(self, observer):
        """ Registration of the new observer
       
        Keywords arguments:
        observer - object, wchich realization IObserver

        """
        pass

    @abstractmethod
    def RemoveObserver(self, observer):
        """ Removing of the certain observer
       
        Keywords arguments:
        observer - observer, wcich will be removed 

        """
        pass

    @abstractmethod
    def NotifyObservers(self, data):
        """ Notifying observers """
        pass


