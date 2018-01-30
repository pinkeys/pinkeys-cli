"""PINKEYS-cli"""

import logging
import sys
import json
import begin
import requests


logger = logging.getLogger('PinKeys_log')
logger.setLevel(logging.DEBUG)

@begin.start(auto_convert=True)
def main(user: 'The www.pinkey.com username'=' ',
         key_type: 'Type of public key to extract'='ssh',
         key_file: 'Output file to write the public key'=' '):
    '''Entry point retrieve public key from the pinkeys.com'''

    attempts = 3
    while user.strip() == '':
        print('Username is required to proceed.')
        user = input('Enter pinkey username to lookup: ')
        attempts -= 1
        if attempts == 0:
            exit(0)

    request_url = str.format(u'https://www.pinkeys.com/api/v1.0/users/{0}/{1}',
                             user,
                             key_type)
    logger.debug('Requesting key from URL: ' + request_url)
    pinkey_response = requests.get(request_url)
    logger.debug('Status code: ' + str(pinkey_response.status_code))
    logger.debug('Respose test: ' + pinkey_response.text)

    if pinkey_response.status_code == 200:
        payload = json.loads(pinkey_response.text)
        for user in payload['user']:
            if user['type'] != key_type:
                continue

            if key_file.strip() != '':  # Print the output to a file
                with (open(key_file, 'w')) as writer:
                    writer.write(user['value'])
            else:  # Otherwise print to screen
                print(user['value'])

    else:
        # print(u'Server Error:' + str(pinkey_response.status_code) + '\n')
        sys.stderr.write(u'Unable to get the public key requested.\n')
