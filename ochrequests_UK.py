# from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
from fastapi.responses import Response,JSONResponse
from datetime import datetime, timedelta
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
def get_socrates_uk_data():
  with concurrent.futures.ThreadPoolExecutor(max_workers=CONNECTIONS) as executor:
    future_to_url = {executor.submit(load_url, url, TIMEOUT): url for url in urls}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
            out.update(data)
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
  och_request = f"""<SiebelMessage>
            <SystemId>{out['specsaver_store']['uk_store_no']}</SystemId>
            <ExternalId>{out['random_numbers']['ExternalId']}</ExternalId>
            <ListOfSsOCHCustomer>
                <Contact>
                    <Title>{out['personal']['random_title']}</Title>
                    <FirstName>{out['personal']['random_names']['fake_first_name']}</FirstName>
                    <LastName>{out['personal']['random_names']['fake_last_name']}</LastName>
                    <DateofBirth>{out['personal']['random_dates']['dob_format3']}</DateofBirth>
                    <Gender>{out['personal']['random_gender']['en_gender']}</Gender>
                    <RegistrationDate>{out['personal']['random_dates']['RegistrationDate']}</RegistrationDate>
                    <PreferredCommunicationMethod>{out['personal']['random_comm_status']['comm_method_desc']}</PreferredCommunicationMethod>
                    <Status>Active</Status>
                    <StatusDate>{out['personal']['random_dates']['StatusDate']}</StatusDate>
                    <ListOfPostalAddress>
                        <PostalAddress>
                            <IsPrimary>Y</IsPrimary>
                            <AddressType>Home</AddressType>
                            <StreetAddressLine1>{out['contrywise_address']['UK_address']['addressline1']}</StreetAddressLine1>
                        <!---   <StreetAddressLine2>1 Blackness Avenue</StreetAddressLine2> -->
                            <Town>{out['contrywise_address']['UK_address']['city']}</Town>
                        <!---   <District>Whitele Avenue</District> -->
                            <County>{out['contrywise_address']['UK_address']['county']}</County>
                            <Country>{out['contrywise_address']['UK_address']['country']}</Country>
                            <Postcode>{out['contrywise_address']['UK_address']['postcode']}</Postcode>
                        </PostalAddress>
                    </ListOfPostalAddress>
                    <ListOfCommunicationAddress>
                        <CommunicationAddress>
                          <ExternalId>{out['random_numbers']['HCommExtID']}</ExternalId>
                          <Type>Phone</Type>
                          <SubType>Daytime</SubType>
                          <Address>{out['contrywise_random_phoneno']['uk_homephone_number']}</Address>
                          <ActiveFlag>Y</ActiveFlag>
                        </CommunicationAddress>
                        <CommunicationAddress>
                          <ExternalId>{out['random_numbers']['MCommExtID']}</ExternalId>
                          <Type>Phone</Type>
                          <SubType>Mobile</SubType>
                          <Address>{out['contrywise_random_phoneno']['uk_mobile_number']}</Address>
                          <ActiveFlag>Y</ActiveFlag>
                        </CommunicationAddress>
                        <CommunicationAddress>
                          <ExternalId>{out['random_numbers']['WCommExtID']}</ExternalId>
                          <Type>Phone</Type>
                          <SubType>Evening</SubType>
                          <Address>{out['contrywise_random_phoneno']['uk_homephone_number']}</Address>
                          <ActiveFlag>Y</ActiveFlag>
                        </CommunicationAddress>
                        <CommunicationAddress>
                           <ExternalId>{out['random_numbers']['ECommExtID']}</ExternalId>
                           <Type>Email</Type>
                           <SubType>Email</SubType>
                           <Address>{out['email_random']['email_random_format1']}</Address>
                           <ActiveFlag>Y</ActiveFlag>
                        </CommunicationAddress>
                    </ListOfCommunicationAddress>
                    <ListOfInteraction>
                        <Interaction>
                           <EventSubtype>{out['random_appt_testdetails']['EventSubtype']}</EventSubtype>
                           <EventType>{out['random_appt_testdetails']['EventType']}</EventType>
                           <LastEventDate>{out['random_appt_testdetails']['LastEventDate']}</LastEventDate>
                        </Interaction>
                        <Interaction>
                           <EventSubtype>{out['random_sight_testdetails']['EventSubtype']}</EventSubtype>
                           <NextEventDate>{out['random_sight_testdetails']['NextEventDate']}</NextEventDate>
                           <OutsideRxFlag>{out['random_sight_testdetails']['OutsideRxFlag']}</OutsideRxFlag>
                           <EventType>{out['random_sight_testdetails']['EventType']}</EventType>
                           <LastEventDate>{out['random_sight_testdetails']['LastEventDate']}</LastEventDate>
                           <EventPeriod>24</EventPeriod>
                        </Interaction>
                        <Interaction>
                           <EventSubtype>{out['random_contactlens_testdetails']['EventSubtype']}</EventSubtype>
                           <NextEventDate>{out['random_contactlens_testdetails']['NextEventDate']}</NextEventDate>
                           <OutsideRxFlag>{out['random_contactlens_testdetails']['OutsideRxFlag']}</OutsideRxFlag>
                           <EventType>{out['random_contactlens_testdetails']['EventType']}</EventType>
                           <LastEventDate>{out['random_contactlens_testdetails']['LastEventDate']}</LastEventDate>
                           <EventPeriod>12</EventPeriod>
                        </Interaction>
                    </ListOfInteraction>
                    <ListOfReference>
                        <Reference>
                           <ReferenceType>{out['reference_info']['ref_type']}</ReferenceType>
                           <ReferenceValue>{out['reference_info']['ref_value']}</ReferenceValue>
                        </Reference>
                    </ListOfReference>
                    <ListOfAttribute>
                        <Attribute  name="Defect 681:last-c-lens-check"  value="2016-09-01T00:00:00Z"/>
                        <Attribute  name="Defect 681:c-lens-recall-period"  value="12"/>
                        <Attribute  name="Defect 681:next-c-lens-check"  value="2017-09-01T00:00:00Z"/>
                        <Attribute  name="Defect 681:last-test"  value="2016-01-01T00:00:00Z"/>
                        <Attribute  name="Defect 681:spec-recall-period"  value="24"/>
                        <Attribute  name="Defect 681:next-test"  value="2018-01-01T00:00:00Z"/>
                    </ListOfAttribute>
                </Contact>
            </ListOfSsOCHCustomer>
          </SiebelMessage> """
  print("Threaded time:", time.time() - threaded_start)      
  return Response(content=och_request, media_type="application/xml")

def get_consent_socrates_uk_data():
    socates_och_consent_request = [
                {
                    "consent":{
                    "store_country_code":"GB",
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
                    "store_number": out['specsaver_store']['uk_store_no'],
                    "source_system":"Socrates"
                },
                    "status": "Active",
                    "date_of_birth": out['personal']['random_dates']['dob_format1'],
                    "title": out['personal']['random_title'],
                    "first_name": out['personal']['random_names']['fake_first_name'],
                    "last_name": out['personal']['random_names']['fake_last_name'],
                    "gender": out['personal']['random_gender']['en_gender'],
                    "county": out['contrywise_address']['UK_address']['county'],
                    "country": out['contrywise_address']['UK_address']['country'],
                    "city": out['contrywise_address']['UK_address']['city'],
                    "district": out['contrywise_address']['UK_address']['county'],
                    "mobile": out['contrywise_random_phoneno']['uk_mobile_number'],
                    "home_phone": out['contrywise_random_phoneno']['uk_homephone_number'],
                    "work_phone": out['contrywise_random_phoneno']['uk_homephone_number'],
                    "email": out['email_random']['email_random_format1'],
                    "address_line_1": out['contrywise_address']['UK_address']['addressline1'],
                    "postcode": out['contrywise_address']['UK_address']['postcode']
                }
                    ] 
    return JSONResponse(content=socates_och_consent_request)

def get_merged_sycle_gb_data():
    unique_external_id = 111 * random.randint(1000, 12999)
    StatusDate_str = out['personal']['random_dates']['StatusDate']
    StatusDate = datetime.strptime(StatusDate_str[:10], "%Y-%m-%d")
    current_year = datetime.now().year
    if StatusDate.year != current_year:
       new_StatusDate = StatusDate + timedelta(days=365)
    else:
       new_StatusDate = StatusDate
    new_StatusDate_str = new_StatusDate.strftime("%Y-%m-%dT00:00:00Z")
    sycle_gb_request = f"""<ListOfSiebelMessages>
          <SiebelMessage>
            <SystemId>Sycle_GB</SystemId>
            <ExternalId>{unique_external_id}</ExternalId>
            <ListOfSsOCHCustomer>
                <Contact>
                    <Title>{out['personal']['random_title']}</Title>
                    <FirstName>{out['personal']['random_names']['fake_first_name']}</FirstName>
                    <LastName>{out['personal']['random_names']['fake_last_name']}</LastName>
                    <DateofBirth>{out['personal']['random_dates']['dob_format3']}</DateofBirth>
                    <Gender>{out['personal']['random_gender']['en_gender']}</Gender>
                    <Status>Active</Status>
                    <StatusDate>{new_StatusDate_str}</StatusDate>
                    <ListOfPostalAddress>
                        <PostalAddress>
                            <IsPrimary>N</IsPrimary>
                            <AddressType>Sycle Home</AddressType>
                            <StreetAddressLine1>{out['contrywise_address']['UK_address']['addressline1']}</StreetAddressLine1>
                        <!---   <StreetAddressLine2>1 Blackness Avenue</StreetAddressLine2> -->
                            <Town>{out['contrywise_address']['UK_address']['city']}</Town>
                        <!---   <District>Whitele Avenue</District> -->
                            <County>{out['contrywise_address']['UK_address']['county']}</County>
                            <Country>{out['contrywise_address']['UK_address']['country']}</Country>
                            <Postcode>{out['contrywise_address']['UK_address']['postcode']}</Postcode>
                        </PostalAddress>
                    </ListOfPostalAddress>
                    <ListOfCommunicationAddress>
                        <CommunicationAddress>
                          <ExternalId>Phone2_{unique_external_id}</ExternalId>
                          <Type>Phone</Type>
                          <SubType>Sycle Telephone 2</SubType>
                          <Address>{out['contrywise_random_phoneno']['uk_homephone_number']}</Address>
                          <ActiveFlag>Y</ActiveFlag>
                        </CommunicationAddress>
                        <CommunicationAddress>
                          <ExternalId>Phone1_{unique_external_id}</ExternalId>
                          <Type>Phone</Type>
                          <SubType>Sycle Telephone 1</SubType>
                          <Address>{out['contrywise_random_phoneno']['uk_mobile_number']}</Address>
                          <ActiveFlag>Y</ActiveFlag>
                        </CommunicationAddress>
                        <CommunicationAddress>
                          <ExternalId>Phone3_{unique_external_id}</ExternalId>
                          <Type>Phone</Type>
                          <SubType>Sycle Telephone 3</SubType>
                          <Address>{out['contrywise_random_phoneno']['uk_homephone_number']}</Address>
                          <ActiveFlag>Y</ActiveFlag>
                        </CommunicationAddress>
                        <CommunicationAddress>
                           <ExternalId>Email_{unique_external_id}</ExternalId>
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
    return Response(content=sycle_gb_request, media_type="application/xml")

def get_mergedconsent_sycle_gb_data():
    sycle_och_consent_request = [
                {
                    "consent":{
                    "store_country_code":"GB",
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