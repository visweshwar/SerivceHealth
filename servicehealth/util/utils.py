from zeep import Client, Settings
import xml.etree.ElementTree as ET
import pathlib
import yaml
import servicehealth.util.globalconstants as GC


class Utils:

    @staticmethod
    def soap_call(envData,service, data):
        settings = Settings(strict=False, xml_huge_tree=True)
        client = Client(envData["url"], settings=settings)

        with client.settings(raw_response=True):
            response = client.service.Add(**data)
            if response.status_code == 200:
                print(service)
                root = ET.fromstring(response.content)
                return root
            else:
                print(f'Response Code:{response.status_code}')

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
                print(exc)
            print(data[section])
            return data[section]

