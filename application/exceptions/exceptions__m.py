import os

"""
exception Exception
    All built-in, non-system-exiting exceptions are derived from this class. All user-defined exceptions should also be derived from this class.
"""

class cError(Exception):
    """Base class for other exceptions"""
    pass


class cLoginTimeoutError(Error):
    """Raised login to device times out"""
    pass


class cLoginCredentialsError(Error):
    """Raised when there is a problem with the user credentials"""
    pass
