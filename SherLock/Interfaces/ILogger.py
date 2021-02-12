from abc import ABCMeta, abstractmethod


class ILoger(object):
    """  Class for loging exceptions and actions  
        
        Open methods:
        Logg
    """

    @abstractmethod
    def Log(self, text):
        """ Loging the text in the log file
       
        Keywords arguments:
        text - text wchich write in file

        """
        pass


