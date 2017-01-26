from fasSetup import fasSetup
from fasShow import fasShow
from fasTeardown import fasTeardown
from lib.SSH import SSH
from Parsing import Parsing
from robot.api import logger
from lib.log import setup_logger
from robot.libraries.BuiltIn import BuiltIn
import logging

class FAS(fasSetup, fasShow, fasTeardown, Parsing):
	"""
    FAS class will inherit fasSetup, fasShow and fasTeardown classes to
    access all the methods for configuring FAS.
    """


	def __init__(self):
		"""Contructor."""
		self.sshclient = None
		self.log = None

	def connect(self, ip, username, password):
		"""
        Connect to the FAS.

        param ip: FAS cluster management IP
        type: string

        param username: FAS Cluster management username
        type: string

        param password: FAS Clusgter management password
        type: string
        """
		self.sshclient = SSH(ip, username=username, password=password)
		self.sshclient.connect()
		self.set_logger()
		logger.console("FAS connection to %s is established" %ip)
		fasSetup.__init__(self, self.sshclient, self.log)
		fasShow.__init__(self, self.sshclient, self.log)
		fasTeardown.__init__(self, self.sshclient, self.log)

	def set_logger(self):
		"""
		Set Logger
		"""
		tcname = BuiltIn().get_variable_value("${TEST NAME}")
		tcname = tcname + ".log"
		logger.console("tc: %s" %tcname)
		self.log = setup_logger(tcname)

	def close(self):
		"""
		Closs tha Established FAS connection
		"""
		self.sshclient.close()
		logger.console("FAS connection is closed")
		self.log.handlers[0].close()