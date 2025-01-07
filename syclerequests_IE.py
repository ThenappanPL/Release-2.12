# from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
from fastapi.responses import Response,JSONResponse
import requests
import time
import random

headers = {'Content-Type': 'application/json','x-api-key': '7ah5W8NQ.228oD7coJ9j8oh8LWMgNZy-m9vsVvfcey'}
out = {}
urls = []
CONNECTIONS = 100
TIMEOUT = 5

with open("resources/url_list.txt") as reader:
    for url in reader:
        urls.append(url.strip())

def load_url(url, timeout):
    ans = requests.get(url, timeout=timeout,headers=headers).json()
    return ans

print("Running threaded:")
threaded_start = time.time()
def get_sycle_ie_data():
  with concurrent.futures.ThreadPoolExecutor(max_workers=CONNECTIONS) as executor:
    future_to_url = {executor.submit(load_url, url, TIMEOUT): url for url in urls}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
            out.update(data)
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
  sycle_request = f"""<ListOfSiebelMessages>
          <SiebelMessage>
            <SystemId>Sycle_IE</SystemId>
            <ExternalId>{out['random_numbers']['ExternalId']}</ExternalId>
            <ListOfSsOCHCustomer>
                <Contact>
                    <Title>{out['personal']['random_title']}</Title>
                    <FirstName>{out['personal']['random_names']['fake_first_name']}</FirstName>
                    <LastName>{out['personal']['random_names']['fake_last_name']}</LastName>
                    <DateofBirth>{out['personal']['random_dates']['dob_format3']}</DateofBirth>
                    <Gender>{out['personal']['random_gender']['en_gender']}</Gender>
                    <Status>Active</Status>
                    <StatusDate>{out['personal']['random_dates']['StatusDate']}</StatusDate>
                    <ListOfPostalAddress>
                        <PostalAddress>
                            <IsPrimary>N</IsPrimary>
                            <AddressType>Sycle Home</AddressType>
                            <StreetAddressLine1>{out['contrywise_address']['ROI_address']['addressline1']}</StreetAddressLine1>
                        <!---   <StreetAddressLine2>1 Blackness Avenue</StreetAddressLine2> -->
                            <Town>{out['contrywise_address']['ROI_address']['city']}</Town>
                        <!---   <District>Whitele Avenue</District> -->
                            <County>{out['contrywise_address']['ROI_address']['county']}</County>
                            <Country>{out['contrywise_address']['ROI_address']['country']}</Country>
                            <Postcode>{out['contrywise_address']['ROI_address']['postcode']}</Postcode>
                        </PostalAddress>
                    </ListOfPostalAddress>
                    <ListOfCommunicationAddress>
                        <CommunicationAddress>
                          <ExternalId>Phone2_{out['random_numbers']['ExternalId']}</ExternalId>
                          <Type>Phone</Type>
                          <SubType>Sycle Telephone 2</SubType>
                          <Address>{out['contrywise_random_phoneno']['ie_homephone_number']}</Address>
                          <ActiveFlag>Y</ActiveFlag>
                        </CommunicationAddress>
                        <CommunicationAddress>
                          <ExternalId>Phone1_{out['random_numbers']['ExternalId']}</ExternalId>
                          <Type>Phone</Type>
                          <SubType>Sycle Telephone 1</SubType>
                          <Address>{out['contrywise_random_phoneno']['ie_mobile_number']}</Address>
                          <ActiveFlag>Y</ActiveFlag>
                        </CommunicationAddress>
                        <CommunicationAddress>
                          <ExternalId>Phone3_{out['random_numbers']['ExternalId']}</ExternalId>
                          <Type>Phone</Type>
                          <SubType>Sycle Telephone 3</SubType>
                          <Address>{out['contrywise_random_phoneno']['ie_homephone_number']}</Address>
                          <ActiveFlag>Y</ActiveFlag>
                        </CommunicationAddress>
                        <CommunicationAddress>
                           <ExternalId>Email_{out['random_numbers']['ExternalId']}</ExternalId>
                           <Type>Email</Type>
                           <SubType>Sycle Email</SubType>
                           <Address>{out['email_random']['email_random_format1']}</Address>
                           <ActiveFlag>Y</ActiveFlag>
                        </CommunicationAddress>
                    </ListOfCommunicationAddress>
                </Contact>
            </ListOfSsOCHCustomer>
          </SiebelMessage>
      </ListOfSiebelMessages>"""
  return Response(content=sycle_request, media_type="application/xml")

def get_sycle_consent_ie_data():
    sycle_och_consent_request = [
                {
                    "consent":{
                    "store_country_code":"IE",
                    "submitted_time": out['personal']['random_datetime'],
                    "permissions":[
                {
                    "type":"Consent - Data",
                    "value": "Y",
                    "date_time": out['personal']['random_datetime'],
                    "method":"Read to Customer",
                    "user": out['random_numbers']['ECommExtID'],
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
                    "date_time": out['personal']['random_datetime'],
                    "method":"Read to Customer",
                    "user": out['random_numbers']['ECommExtID'],
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
                    "date_time": out['personal']['random_datetime'],
                    "method":"Read to Customer",
                    "user":  out['random_numbers']['ECommExtID'],
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
                    "date_time": out['personal']['random_datetime'],
                    "method":"Read to Customer",
                    "user": out['random_numbers']['ECommExtID'],
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
                    "date_time": out['personal']['random_datetime'],
                    "method":"Read to Customer",
                    "user": out['random_numbers']['ECommExtID'],
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
                    "date_time": out['personal']['random_datetime'],
                    "method":"Read to Customer",
                    "user": out['random_numbers']['ECommExtID'],
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
                    "date_time": out['personal']['random_datetime'],
                    "method":"Read to Customer",
                    "user": out['random_numbers']['ECommExtID'],
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
                    "date_time": out['personal']['random_datetime'],
                    "method":"Read to Customer",
                    "user": out['random_numbers']['ECommExtID'],
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
                    "date_time": out['personal']['random_datetime'],
                    "method":"Read to Customer",
                    "user": out['random_numbers']['ECommExtID'],
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
                    "date_time": out['personal']['random_datetime'],
                    "method":"Read to Customer",
                    "user": out['random_numbers']['ECommExtID'],
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
                    "date_time": out['personal']['random_datetime'],
                    "method":"Read to Customer",
                    "user": out['random_numbers']['ECommExtID'],
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
                    "date_time": out['personal']['random_datetime'],
                    "method":"Read to Customer",
                    "user": out['random_numbers']['ECommExtID'],
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
                    "date_time": out['personal']['random_datetime'],
                    "method":"Read to Customer",
                    "user": out['random_numbers']['ECommExtID'],
                    "appropriate_person":{
                    "role":"Not Applicable",
                    "title":"Not Applicable",
                    "first_name":"Not Applicable",
                    "last_name":"Not Applicable"
                }
                }
                ],
                    "customer_number": out['random_numbers']['ExternalId'],
                    "store_number": 8149,
                    "source_system":"Sycle"
                },
                    "date_of_birth": out['personal']['random_dates']['dob_format1'],
                    "first_name": out['personal']['random_names']['fake_first_name'],
                    "last_name": out['personal']['random_names']['fake_last_name']
                }
                    ] 
    return JSONResponse(content=sycle_och_consent_request)