from servicehealth.util.utils import Utils
import servicehealth.util.globalconstants as GC
import requests

class RestService:
    env = None
    envConfig = None
    serviceConfig = None

    def __init__(self, environment):
        """
        This is the init function for setting up the class
        """
        print(f"The environment is {environment}")
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
            print("Service Health OK: " ,response.status_code)
        else:
            print("Service Health Not OK: " ,response.status_code)
