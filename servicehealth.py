import argparse
import logging

from servicehealth.services.soapservice import SoapService
from servicehealth.services.restservice import RestService

parser = argparse.ArgumentParser()
parser.add_argument('--environment', help='Add the environment eg. prod,dev')
parser.add_argument('--loglevel', help='Provide log levels  INFO or DEBUG, TRACE not supported')
logger = logging.getLogger("servicehealth")

args = parser.parse_args()
env = str(args.environment).lower()

def test_soap():
    soap = SoapService(env)
    soap.post_wsdl()


def test_rest():
    rest = RestService(env)
    rest.get_data()

def configure_logging():
    # process env variable.
    logarg = str(args.loglevel).upper()
    loglevel =  getattr(logging,logarg) if logarg is not None else logging.INFO

    #Console logging
    console = logging.StreamHandler()
    console.setLevel(loglevel)

    #File Logging
    file = logging.FileHandler(filename='myapp.log',mode='a')
    logging.basicConfig(level=loglevel,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        handlers=[file,
                                  console])


configure_logging()
test_soap()
test_rest()
