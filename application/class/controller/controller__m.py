# controllers for viptela
"""Base API class and functions used by the API."""


import json
import requests
from requests.exceptions import ConnectionError
from . import constants, exceptions, utils

"""
https://sdwan-docs.cisco.com/Product_Documentation/Command_Reference/cvManage_REST_APIs/cvManage_REST_APIs_Overview/cvManage_Simple_Query

edited the file 2x :

"""


class cvManage(object):
    """
    Class for use with Viptela cvManage API.
    """

    def __init__(self, user, user_pass, cvManage_server, cvManage_server_port=8443,
                 verify=False, disable_warnings=False, timeout=constants.STANDARD_HTTP_TIMEOUT,
                 auto_login=True):
        """
        Init method for Viptela class
        :param user: API user name
        :param user_pass: API user password
        :param cvManage_server: cvManage server IP address or Hostname
        :param cvManage_server_port: cvManage API port
        :param verify: Verify HTTPs certificate verification
        :param disable_warnings: Disable console warnings if ssl cert invalid
        :param timeout: Timeout for request response
        :param auto_login: Automatically login to cvManage server
        """
        self.user = user
        self.user_pass = user_pass
        self.cvManage_server = cvManage_server
        self.cvManage_server_port = cvManage_server_port
        self.verify = verify
        self.timeout = timeout
        self.disable_warnings = disable_warnings

        if self.disable_warnings:
            requests.packages.urllib3.disable_warnings()

        self.auto_login = auto_login

        self.base_url = 'https://{0}:{1}/dataservice'.format(
            self.cvManage_server,
            self.cvManage_server_port
        )

    def simple_query(self):
        """
        https://sdwan-docs.cisco.com/Product_Documentation/Command_Reference/cvManage_REST_APIs/cvManage_REST_APIs_Overview/cvManage_Simple_Query
        """



            
            
