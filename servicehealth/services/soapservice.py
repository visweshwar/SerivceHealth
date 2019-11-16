from servicehealth.util.utils import Utils
import servicehealth.util.globalconstants as GC


class SoapService:
    env = None
    envConfig = None
    serviceConfig = None

    def __init__(self, environment):
        """
        This is the init function for setting up the class
        """
        print(f"The environment is {environment}")
        self.env = environment
        #self.envConfig = Utils.load_section_config(GC.ENVIRONMENTS_SECTION)
        self.serviceConfig = Utils.load_section_config(GC.SERVICES_SECTION)

    def post_wsdl(self):
        """
        TO add two numbers
        :return:
        """
        service = self.serviceConfig[GC.SERVICE_A]
        envdata = self.serviceConfig[GC.SERVICE_A][GC.ENVIRONMENTS_SECTION][self.env]
        data = {'intA': 1, 'intB': 2}
        response = Utils.soap_call(envdata,service, data)
        if response:
            for result in response.findall('.//role:AddResult', service["namespace"]):
                print(result.text)
