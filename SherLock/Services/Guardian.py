from Interfaces.IGuardian import IGuardian
import sys

class Guardian(IGuardian):
    """  Class for protection methods and generate exceptions  
        
        Open methods:
        Secure

        Interfaces:
        IGuardian
    """
    

    def __init__ (self, loger):
        """ Init Guardian object
       
        Keywords arguments:
        logger - logger for loggering sql requests

        """
        self.__loger = loger

    def Secure(self, func, *args):
        """ Executes function with some arguments and catch exception if it was thrown
       
        Keywords arguments:
        func - executing function
        *args - arguments for executing function

        return function result or closing script
        """
        result = 0

        try:
            result = func.__call__(*args)

        except Exception as e:
            self.__loger.Log(str(e))
            sys.exit(e)

        return result


    __loger = 0