import argparse

from servicehealth.services.soapservice import SoapService
from servicehealth.services.restservice import RestService

parser = argparse.ArgumentParser()
parser.add_argument('--environment', help='Add the environment eg. prod,dev')

args = parser.parse_args()
print(args)

env = str(args.environment).lower()
print(f'The environment is {env}')


def test_soap():
    soap = SoapService(env)
    soap.post_wsdl()


def test_rest():
    rest = RestService(env)
    rest.post_wsdl()


test_soap()
test_rest()
