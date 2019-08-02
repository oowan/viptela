# controllers for viptela
"""Base API class and functions used by the API."""

import os
import json
import requests
from requests.exceptions import ConnectionError
#from . import constants, exceptions, utils

"""
https://sdwan-docs.cisco.com/Product_Documentation/Command_Reference/cvManage_REST_APIs/cvManage_REST_APIs_Overview/cvManage_Simple_Query
"""

class cvManage:

    def __init__(self, msgs
                 , user
                 , user_pass
                 , cvManage_server
                 , cvManage_server_port=8443
                 , verify=False
                 , disable_warnings=False
                 , timeout=constants.STANDARD_HTTP_TIMEOUT
                 , auto_login=True):
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
        self.set_msgs(msgs)
        __msgs = None  # ~ private variable

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


        #def __init__(self, msgs=True):
        #    self.set_msgs(msgs)

        __msgs = None  # ~ private variable

    def set_msgs(self, z_msgs):
        self.__msgs = z_msgs

    def get_msgs(self):
        return self.__msgs

    def information_about_cvManage_class(self):
        if self.__msgs == True:
            print("List some Advantages of cvManage : \n")
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
    res = cvManage(msgs=True)
    res.information_about_cvManage_class()


if __name__ == '__main__':
    main()



