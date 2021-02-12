from abc import ABCMeta, abstractmethod

class IGuardian(object):
    """  Class for protection methods and generate exceptions  
        
        Open methods:
        Secure
    """

    def Secure(self, func, *args):
        """ Executes function with some arguments and catch exception if it was thrown
       
        Keywords arguments:
        func - executing function
        *args - arguments for executing function

        """
        pass


