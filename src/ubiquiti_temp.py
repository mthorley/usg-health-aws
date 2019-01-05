import requests
import json
import boto3
import sys
import os

headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
}

class Config:
  pass

def authenticate(config):
    # Login
    login_url = config.base_url + "/login"
    payload = "{\n   \"username\" : \"" + config.username + "\",\n   \"password\" : \"" + config.pwd + "\"\n}"
    r1 = requests.request("POST", login_url, data=payload, headers=headers, verify=False)
    if r1.status_code != 200:
        raise Exception('Login failed ', r1.status_code, 'for user', config.username)
    return r1

# Cloudwatch logstream 
def log(devices):
    i = 0
    for d in devices['data']:
        if devices['data'][i]['model'] == 'US24P250':
            # For US24P250
            print "US24P250:general_temperature", devices['data'][i]['general_temperature']
            print "US24P250:fan_level", devices['data'][i]['fan_level']
            
        if devices['data'][i]['model'] == 'UGW4':
            # For UGW4
            print "USGW:board_cpu_temperature", devices['data'][i]['system-stats']['temps']['Board (CPU)']
            print "USGW:board_phy_temperature", devices['data'][i]['system-stats']['temps']['Board (PHY)']
            print "USGW:phys_temperature", devices['data'][i]['system-stats']['temps']['PHY']
            print "USGW:cpu_temperature", devices['data'][i]['system-stats']['temps']['CPU']
        i = i + 1

def _internal(config):
    # Login
    r1 = authenticate(config)

    # Get device info (including temperatures)
    payload = ""
    devices_url = config.base_url + "/s/default/stat/device"
    r2 = requests.request("GET", devices_url, data=payload, headers=headers, verify=False, cookies=r1.cookies)
    if r2.status_code != 200:
        raise Exception('Failed to get device information')

    devices = json.loads(r2.text)
    log(devices)
    
def main(argv):
    print "_main"
    # get config from args
    config = Config()
    config.username = sys.argv[1]   # auditor
    config.pwd = sys.argv[2]        # pwd
    config.base_url = sys.argv[3]   # https://192.168.1.8:8443/api

    _internal(config)

def lambda_handler(event, context):
    print "lambda"
    # get config from env
    config = Config()
    config.username = os.environ['username']
    config.pwd = os.environ['pwd']
    config.base_url = os.environ['base_url']

    _internal(config)

    return {
        'statusCode': 200,
        'body': json.dumps('Done')
    }

if __name__== "__main__":
    main(sys.argv[1:])
