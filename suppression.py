import requests
from fastapi.responses import PlainTextResponse
import random

store_url = 'https://tp_spec.deta.dev/api/v1/random_stores'
nos_url = 'https://tp_spec.deta.dev/api/v1/random_string_numbers'
personal_url = 'https://tp_spec.deta.dev/api/v1/random_personal'
contact_url = 'https://tp_spec.deta.dev/api/v1/random_contact'
headers = {'Content-Type': 'application/json','x-api-key': '7ah5W8NQ.228oD7coJ9j8oh8LWMgNZy-m9vsVvfcey'}
suppression_request ='CRN|EPOS_NUMBER|COMMUNICATION_ADDRESS|CLEANSE_CODE|CLEANSE_DATE\n'
# suppression_code = random.choice(['S0','S1','S2','S3'])

def get_suppression_data():
 suppression_request1 = []
 for i in range(2):
   systemstore_response = requests.get(store_url,headers=headers).json()
   customerno_response = requests.get(nos_url,headers=headers).json()
   contact_response = requests.get(contact_url,headers=headers).json()
   personal_response = requests.get(personal_url,headers=headers).json()
   suppression_request1 += [f"""{customerno_response['random_numbers']['ExternalId']}|{systemstore_response['specsaver_store']['uk_store_no']}|{contact_response['contrywise_random_phoneno']['uk_mobile_number']}|{random.choice(['S0','S1','S2','S3'])}|{personal_response['personal']['random_dates']['dob_format1']}"""]
 combined_request = '\n'.join(suppression_request1)
 return PlainTextResponse(content=(suppression_request+combined_request))