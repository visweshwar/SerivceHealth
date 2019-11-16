from servicehealth.util.utils import Utils
import servicehealth.util.globalconstants as GC
import requests
import logging

class RestService:
    env = None
    envConfig = None
    serviceConfig = None
    logger = None

    def __init__(self, environment):
        """
        This is the init function for setting up the class
        """
        self.logger = logging.getLogger('servicehealth.services.RestService')
        self.logger.debug(f"The environment is {environment}")
        self.env = environment
        self.serviceConfig = Utils.load_section_config(GC.SERVICES_SECTION)

    def get_data(self):
        """
        TO add two numbers
        :return:
        """
        envdata = self.serviceConfig[GC.SERVICE_B][GC.ENVIRONMENTS_SECTION][self.env]
        response = requests.get(envdata["url"])
        if response.ok:
            self.logger.info(f'Service Health OK: {response.status_code}')
        else:
            self.logger.error(f'Service Health Not OK: {response.status_code}')
