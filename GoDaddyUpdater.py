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
create_missing_records = os.environ.get('GODADDY_CREATE_MISSING_RECORDS', True)

userAccount = Account(api_key=key, api_secret=secret_key)
userClient = Client(userAccount)

publicIP = False
while not publicIP:
  publicIP = pif.get_public_ip()

for domain in domain_list:
  for a_record in a_record_list:
    print("Attemping update for: %s.%s" % (a_record, domain))
    try:
      records = userClient.get_records(domain, name=a_record, record_type='A')
      if len(records) == 0:
        print("No records returned for name.domain: %s.%s" % (a_record, domain))
        if create_missing_records:
          new_record =  {
                          "type": 'A',
                          "name": a_record,
                          "data": publicIP,
                          "ttl": 600,
                        }
          add_record_result = userClient.add_record(domain, new_record)
          if not add_record_result:
            print("ERROR - Unable to add missing A-record: %s.%s" % (a_record, domain))
          else:
            print("Successfully added missing A-Record: %s.%s" % (a_record, domain))
      for record in records:
        if publicIP != record["data"]:
          updateResult = userClient.update_record_ip(publicIP, domain, name=a_record, record_type='A')
          if updateResult is True:
            print('Update ended with no Exception. %s.%s now assigned IP %s'  %(a_record, domain, publicIP))
        else:
          print('No DNS update needed.')
    except:
      print(sys.exc_info()[1])
      sys.exit()


