import os
import sys

"""
exception Exception
    All built-in, non-system-exiting exceptions are derived from this class. 
    All user-defined exceptions should also be derived from this class.
    
    Python 3's exception hierarchy :
    
    BaseException
        Exception
            ArithmeticError
                FloatingPointError
                OverflowError
                ZeroDivisionError
            AssertionError
            AttributeError
            BufferError
            EOFError
            ImportError
            LookupError
                IndexError
                KeyError
            MemoryError
            NameError
                UnboundLocalError
            OSError
                BlockingIOError
                ChildProcessError
                ConnectionError
                    BrokenPipeError
                    ConnectionAbortedError
                    ConnectionRefusedError
                    ConnectionResetError
                FileExistsError
                FileNotFoundError
                InterruptedError
                IsADirectoryError
                NotADirectoryError
                PermissionError
                ProcessLookupError
                TimeoutError
            ReferenceError
            RuntimeError
                NotImplementedError
            StopIteration
            SyntaxError
                IndentationError
                    TabError
            SystemError
            TypeError
            ValueError
                UnicodeError
                    UnicodeDecodeError
                    UnicodeEncodeError
                    UnicodeTranslateError
            Warning
                BytesWarning
                DeprecationWarning
                FutureWarning
                ImportWarning
                PendingDeprecationWarning
                ResourceWarning
                RuntimeWarning
                SyntaxWarning
                UnicodeWarning
                UserWarning
        GeneratorExit
        KeyboardInterrupt
        SystemExit
            
"""

class cError(Exception):
    """Base class for other exceptions"""
    pass


class cLoginTimeoutError(OSError):
    """Raised login to device times out"""
    pass

class cLoginCredentialsError(OSError):
    """Raised when there is a problem with the user credentials"""
    pass


class cExceptions:

    def __init__(self, msgs=True):
        self.set_msgs(msgs)

    __msgs = None  # ~ private variable   ( those are best !! )
    def set_msgs(self, z_msgs):
        self.__msgs = z_msgs
    def get_msgs(self):
        return self.__msgs
    def information_about_cExceptions_class(self):
        if self.__msgs == True:
            print( "List some Advantages of cExceptions : \n"
                   "\tCentralized for the Exceptions" )
            self.pwd_of_this_class()
        elif not self.__msgs == True:
            pass

    def pwd_of_this_class(self):
        PWD = os.path.realpath(os.path.dirname(__file__))
        print("e.g. this file's location : " + PWD)
        return PWD


# ============================================================
# ==
# ============================================================
def main():

    res = cExceptions(msgs=True)
    res.information_about_cExceptions_class()

if __name__ == '__main__':
    main()

