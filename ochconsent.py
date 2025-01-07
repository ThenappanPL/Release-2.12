import requests
import random
from fastapi.responses import JSONResponse

store_url = 'https://tp_spec.deta.dev/api/v1/random_stores'
nos_url = 'https://tp_spec.deta.dev/api/v1/random_string_numbers'
personal_url = 'https://tp_spec.deta.dev/api/v1/random_personal'
address_url = 'https://tp_spec.deta.dev/api/v1/random_address'
contact_url = 'https://tp_spec.deta.dev/api/v1/random_contact'
headers = {'Content-Type': 'application/json','x-api-key': '7ah5W8NQ.228oD7coJ9j8oh8LWMgNZy-m9vsVvfcey'}

def get_consent_data():
  systemstore_response = requests.get(store_url,headers=headers).json()
  SystemId = systemstore_response['specsaver_store']['uk_store_no']
  customerno_response = requests.get(nos_url,headers=headers).json()
  ExternalId = customerno_response['random_numbers']['ExternalId']
  ECommExtID = customerno_response['random_numbers']['ECommExtID']
  personal_response = requests.get(personal_url,headers=headers).json()
  Title = personal_response['personal']['random_title']
  FirstName = personal_response['personal']['random_names']['first_name']
  LastName = personal_response['personal']['random_names']['last_name']
  DateofBirth = personal_response['personal']['random_dates']['dob_format1']
  ConsentDatetime = personal_response['personal']['random_datetime']
  Gender = personal_response['personal']['random_gender']['en_gender']
  Status = personal_response['personal']['random_status']['status_desc']
  address_response = requests.get(address_url,headers=headers).json()
  StreetAddressLine1 = address_response['contrywise_address']['UK_address']['addressline1']
  Town = address_response['contrywise_address']['UK_address']['city']
  District = address_response['contrywise_address']['UK_address']['county']
  Country = address_response['contrywise_address']['UK_address']['country']
  Postcode = address_response['contrywise_address']['UK_address']['postcode']
  contact_response = requests.get(contact_url,headers=headers).json()
  email = contact_response['email_random']['email_random_format1']
  homephone = contact_response['contrywise_random_phoneno']['uk_homephone_number']
  workphone = contact_response['contrywise_random_phoneno']['uk_homephone_number']
  mobile = contact_response['contrywise_random_phoneno']['uk_mobile_number']
  socates_och_consent_request = [
                {
                    "consent":{
                    "store_country_code":"GB",
                    "submitted_time": ConsentDatetime,
                    "permissions":[
                {
                    "type":"Consent - Data",
                    "value": "Y",
                    "date_time": ConsentDatetime,
                    "method":"Read to Customer",
                    "user": ECommExtID,
                    "appropriate_person":{
                    "role":"Not Applicable",
                    "title":"Not Applicable",
                    "first_name":"Not Applicable",
                    "last_name":"Not Applicable"
                }
                },
                {
                    "type":"Service - Email",
                    "value": random.choice(['Y','N']),
                    "date_time": ConsentDatetime,
                    "method":"Read to Customer",
                    "user": ECommExtID,
                    "appropriate_person":{
                    "role":"Not Applicable",
                    "title":"Not Applicable",
                    "first_name":"Not Applicable",
                    "last_name":"Not Applicable"
                }
                },
                {
                    "type":"Service - Post",
                    "value": random.choice(['Y','N']),
                    "date_time": ConsentDatetime,
                    "method":"Read to Customer",
                    "user":  ECommExtID,
                    "appropriate_person":{
                    "role":"Not Applicable",
                    "title":"Not Applicable",
                    "first_name":"Not Applicable",
                    "last_name":"Not Applicable"
                }
                },
                {
                    "type":"Service - SMS",
                    "value": random.choice(['Y','N']),
                    "date_time": ConsentDatetime,
                    "method":"Read to Customer",
                    "user": ECommExtID,
                    "appropriate_person":{
                    "role":"Not Applicable",
                    "title":"Not Applicable",
                    "first_name":"Not Applicable",
                    "last_name":"Not Applicable"
                }
                },
                {
                    "type":"Service - Telephone",
                    "value": random.choice(['Y','N']),
                    "date_time": ConsentDatetime,
                    "method":"Read to Customer",
                    "user": ECommExtID,
                    "appropriate_person":{
                    "role":"Not Applicable",
                    "title":"Not Applicable",
                    "first_name":"Not Applicable",
                    "last_name":"Not Applicable"
                }
                },
                {
                    "type":"Service Marketing - Email",
                    "value": random.choice(['Y','N']),
                    "date_time": ConsentDatetime,
                    "method":"Read to Customer",
                    "user": ECommExtID,
                    "appropriate_person":{
                    "role":"Not Applicable",
                    "title":"Not Applicable",
                    "first_name":"Not Applicable",
                    "last_name":"Not Applicable"
                }
                },
                {
                    "type":"Service Marketing - Post",
                    "value": random.choice(['Y','N']),
                    "date_time": ConsentDatetime,
                    "method":"Read to Customer",
                    "user": ECommExtID,
                    "appropriate_person":{
                    "role":"Not Applicable",
                    "title":"Not Applicable",
                    "first_name":"Not Applicable",
                    "last_name":"Not Applicable"
                }
                },
                {
                    "type":"Service Marketing - SMS",
                    "value": random.choice(['Y','N']),
                    "date_time": ConsentDatetime,
                    "method":"Read to Customer",
                    "user": ECommExtID,
                    "appropriate_person":{
                    "role":"Not Applicable",
                    "title":"Not Applicable",
                    "first_name":"Not Applicable",
                    "last_name":"Not Applicable"
                }
                },
                {
                    "type":"Service Marketing - Telephone",
                    "value": random.choice(['Y','N']),
                    "date_time": ConsentDatetime,
                    "method":"Read to Customer",
                    "user": ECommExtID,
                    "appropriate_person":{
                    "role":"Not Applicable",
                    "title":"Not Applicable",
                    "first_name":"Not Applicable",
                    "last_name":"Not Applicable"
                }
                },
                {
                    "type":"Promotional - Email",
                    "value": random.choice(['Y','N']),
                    "date_time": ConsentDatetime,
                    "method":"Read to Customer",
                    "user": ECommExtID,
                    "appropriate_person":{
                    "role":"Not Applicable",
                    "title":"Not Applicable",
                    "first_name":"Not Applicable",
                    "last_name":"Not Applicable"
                }
                },
                {
                    "type":"Promotional - Post",
                    "value": random.choice(['Y','N']),
                    "date_time": ConsentDatetime,
                    "method":"Read to Customer",
                    "user": ECommExtID,
                    "appropriate_person":{
                    "role":"Not Applicable",
                    "title":"Not Applicable",
                    "first_name":"Not Applicable",
                    "last_name":"Not Applicable"
                }
                },
                {
                    "type":"Promotional - SMS",
                    "value": random.choice(['Y','N']),
                    "date_time": ConsentDatetime,
                    "method":"Read to Customer",
                    "user": ECommExtID,
                    "appropriate_person":{
                    "role":"Not Applicable",
                    "title":"Not Applicable",
                    "first_name":"Not Applicable",
                    "last_name":"Not Applicable"
                }
                },
                {
                    "type":"Promotional - Telephone",
                    "value": random.choice(['Y','N']),
                    "date_time": ConsentDatetime,
                    "method":"Read to Customer",
                    "user": ECommExtID,
                    "appropriate_person":{
                    "role":"Not Applicable",
                    "title":"Not Applicable",
                    "first_name":"Not Applicable",
                    "last_name":"Not Applicable"
                }
                }
                ],
                    "customer_number": ExternalId,
                    "store_number": SystemId,
                    "source_system":"Socrates"
                },
                    "status": Status,
                    "date_of_birth": DateofBirth,
                    "title": Title,
                    "first_name": FirstName,
                    "last_name": LastName,
                    "gender": Gender,
                    "county": District,
                    "country": Country,
                    "city": Town,
                    "district": District,
                    "mobile": mobile,
                    "home_phone": homephone,
                    "work_phone": workphone,
                    "email": email,
                    "address_line_1": StreetAddressLine1,
                    "postcode": Postcode
                }
                    ] 
  return JSONResponse(content=socates_och_consent_request)
# print(get_consent_data())