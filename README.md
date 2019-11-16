# Background
This Project fulfills the following aspects

* Use a WSDL and make a SOAP Call and Validate health
    * Parse XML SOAP Response
    * Handle Namespaces in Response
* Make a REST Call and validate Health
* Read a YAML config File and parse it
* Dockerize the project and run it with arguments

# Requirements

* Python3 environment
* (Optional) Docker for running it as a docker image

# Local

## Build
You can run the following command to build the application locally

`pip install -r /requirements.txt`

## Run

You can run the application by passing a command line argument

`python3 servicehealth.py --environment prod`

# Docker

## Build
Build the docker image 
`docker build -t servicehealth .`

## Run
Run the docker image with a command line argument
`docker run servicehealth --environment prod`

