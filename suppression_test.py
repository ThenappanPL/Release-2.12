import requests
from fastapi.responses import PlainTextResponse
from concurrent.futures import ThreadPoolExecutor
import random
from timer import timer

store_url = 'https://tp_spec.deta.dev/api/v1/random_stores'
nos_url = 'https://tp_spec.deta.dev/api/v1/random_string_numbers'
personal_url = 'https://tp_spec.deta.dev/api/v1/random_personal'
contact_url = 'https://tp_spec.deta.dev/api/v1/random_contact'
headers = {'Content-Type': 'application/json'}
suppression_request ='CRN|EPOS_NUMBER|COMMUNICATION_ADDRESS|CLEANSE_CODE|CLEANSE_DATE\n'
# suppression_code = random.choice(['S0','S1','S2','S3'])

def fetch():
  suppression_request1 = []
  with requests.Session() as session:
   for i in range(6):
    session.headers.update({'x-api-key': '7ah5W8NQ.228oD7coJ9j8oh8LWMgNZy-m9vsVvfcey'})
    with session.get(store_url) as response:
        store_no = (response.json()['specsaver_store']['uk_store_no'])
    with session.get(nos_url) as response:
        customer_no = (response.json()['random_numbers']['ExternalId'])
    with session.get(contact_url) as response:
        contact_no = (response.json()['contrywise_random_phoneno']['uk_mobile_number'])
    with session.get(personal_url) as response:
        cleanse_date = (response.json()['personal']['random_dates']['dob_format1'])
    suppression_request1 += [f"""{customer_no}|{store_no}|{contact_no}|{random.choice(['S0','S1','S2','S3'])}|{cleanse_date}"""]
  combined_request = '\n'.join(suppression_request1)
    # return(combined_request)
  return PlainTextResponse(content=(suppression_request+combined_request))
# print(fetch(session=requests.Session(),store_url='https://tp_spec.deta.dev/api/v1/random_stores'))

# @timer(1, 1)
# def get_supp():
#     with ThreadPoolExecutor(max_workers=25) as executor:
#         with requests.Session() as session:
#           session.headers.update({'x-api-key': '7ah5W8NQ.228oD7coJ9j8oh8LWMgNZy-m9vsVvfcey'})
#         # with requests.Session.post(url=url_post,headers=headers_post) as session:
#           # executor.submit(fetch, [session] * 6 , [store_url] * 6 )
#           executor.map(fetch, [session] * 4, [store_url] * 4)
#           # print(executor.map(fetch, [session] * 6, [store_url] * 6))
#           executor.shutdown(wait=True)
# print(get_supp())

                    
    

# def get_suppression_data():
#  suppression_request1 = []
#  for i in range(1):
#    systemstore_response = requests.get(store_url,headers=headers).json()
#    customerno_response = requests.get(nos_url,headers=headers).json()
#    contact_response = requests.get(contact_url,headers=headers).json()
#    personal_response = requests.get(personal_url,headers=headers).json()
#    suppression_request1 += [f"""{customerno_response['random_numbers']['ExternalId']}|{systemstore_response['specsaver_store']['uk_store_no']}|{contact_response['contrywise_random_phoneno']['uk_mobile_number']}|{random.choice(['S0','S1','S2','S3'])}|{personal_response['personal']['random_dates']['dob_format1']}"""]
#  combined_request = '\n'.join(suppression_request1)
#  return PlainTextResponse(content=(suppression_request+combined_request))