#!/usr/bin/env python3

# Full package imports
import sys

import pif
from godaddypy import Client, Account

import os

key = os.environ['GODADDY_KEY']
secret_key = os.environ['GODADDY_SECRET']
domain_list = os.environ['GODADDY_DOMAIN_LIST'].split(',')
a_record_list = os.environ['GODADDY_A_RECORD_LIST'].split(',')

userAccount = Account(api_key=key, api_secret=secret_key)
userClient = Client(userAccount)
publicIP = pif.get_public_ip('ident.me')

for domain in domain_list:
  for a_record in a_record_list:
    print("Attemping update for: %s.%s" % (a_record, domain))
    try:
      records = userClient.get_records(domain, name=a_record, record_type='A')
      if len(records) == 0:
        print("No records returned for name.domain: %s.%s" % (a_record, domain))
      for record in records:
        if publicIP != record["data"]:
          updateResult = userClient.update_record_ip(publicIP, domain, name=a_record, record_type='A')
          if updateResult is True:
            print('Update ended with no Exception.')
        else:
          print('No DNS update needed.')
    except:
      print(sys.exc_info()[1])
      sys.exit()


