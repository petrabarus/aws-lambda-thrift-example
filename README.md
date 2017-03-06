# Thrift Implementation in AWS Lambda using Python and Serverless Framework

## Requirement
This example is being developed with this requirements:
- node v6.9.1
- python 2.7
- virtualenv 15.03

## Running
To run this example execute `make`

## Deploying
To deploy this example execute `make deploy`

## Structure
Important files:
- handler.py
  This is the lambda handler
- test.py
  Test client. Replace URL with the deployed API.
- service.thrift
  The thrift definition
- serverless.yml
  Serverless configuration
