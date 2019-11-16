from zeep import Client, Settings
import xml.etree.ElementTree as ET
import pathlib
import yaml
import servicehealth.util.globalconstants as GC
import logging

module_logger = logging.getLogger('servicehealth.util.Utils')

class Utils:



    @staticmethod
    def soap_call(envData,service, data):
        settings = Settings(strict=False, xml_huge_tree=True)
        client = Client(envData["url"], settings=settings)

        with client.settings(raw_response=True):
            response = client.service.Add(**data)
            if response.status_code == 200:
                root = ET.fromstring(response.content)
                return root
            else:
                module_logger.error(f'Response Code:{response.status_code}')

    @staticmethod
    def load_section_config(section):
        """
        This is to load the environment config.
        """
        data = None
        with open(pathlib.Path(__file__).parent / '..' / GC.CONFIG_FILE_NAME, 'r') as stream:
            try:
                data = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                module_logger.error(exc)
            module_logger.debug(data[section])
            return data[section]

