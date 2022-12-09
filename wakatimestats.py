import hashlib
import os
import sys
import datetime
import time
import json
from rauth import OAuth2Service
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

# driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
found = False
crash = False

if sys.version_info[0] == 3:
    raw_input = input

service = OAuth2Service(
    client_id="H6B1FCsjNVUEMSdJfhjWQeTy",  # your App ID from https://wakatime.com/apps
    client_secret="sec_7lyWZ5qbfggG9JhvGZErrBtYmI3gXBXi2NnmSacphNM6LVm7UEmfxErdzoni8xN09xX1PGv3a96ctYkA",  # your App Secret from https://wakatime.com/apps
    name='wakatime',
    authorize_url='https://wakatime.com/oauth/authorize',
    access_token_url='https://wakatime.com/oauth/token',
    base_url='https://wakatime.com/api/v1/')

redirect_uri = 'https://wakatime.com/oauth/test'
state = hashlib.sha1(os.urandom(40)).hexdigest()
params = {'scope': 'email,read_logged_time',
        'response_type': 'code',
        'state': state,
        'redirect_uri': redirect_uri}

# url = service.get_authorize_url(**params)
# driver.get(url)
# while found == False:
#     if driver.current_url[:31] == "https://wakatime.com/oauth/test":
#         found = True
#     else:
#         pass
# code = driver.current_url[37:121]
# driver.quit()

# Make sure returned state has not changed for security reasons, and exchange
# code for an Access Token.
headers = {'Accept': 'application/x-www-form-urlencoded'}
print('Getting an access token...')
# session = service.get_auth_session(headers=headers,
#                                 data={'code': code,
#                                         'grant_type': 'authorization_code',
#                                         'redirect_uri': redirect_uri})

print('Getting current user from API...')
# user = session.get('users/current').json()
# print('Authenticated via OAuth as {0}'.format(user['data']['email']))
print("Getting user's coding stats from API...")
today = datetime.date.today()
time = today - datetime.timedelta(days = 6)
print(time)