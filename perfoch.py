import requests
from concurrent.futures import ThreadPoolExecutor
import time

store_url = 'https://tp_spec.deta.dev/api/v1/random_stores'
nos_url = 'https://tp_spec.deta.dev/api/v1/random_string_numbers'
personal_url = 'https://tp_spec.deta.dev/api/v1/random_personal'
address_url = 'https://tp_spec.deta.dev/api/v1/random_address'
contact_url = 'https://tp_spec.deta.dev/api/v1/random_contact'
testdates_url = 'https://tp_spec.deta.dev/api/v1/random_test_dates'
headers = {'Content-Type': 'application/json'}

def post_url(args):
    systemstore_response = requests.get(store_url,headers=headers).json()
    SystemId = systemstore_response['specsaver_store']['uk_store_no']
    customerno_response = requests.get(nos_url,headers=headers).json()
    ExternalId = customerno_response['random_numbers']['ExternalId']
    ECommExtID = customerno_response['random_numbers']['ECommExtID']
    MCommExtID = customerno_response['random_numbers']['MCommExtID']
    HCommExtID = customerno_response['random_numbers']['HCommExtID']
    WCommExtID = customerno_response['random_numbers']['WCommExtID']
    personal_response = requests.get(personal_url,headers=headers).json()
    Title = personal_response['personal']['random_title']
    FirstName = personal_response['personal']['random_names']['first_name']
    LastName = personal_response['personal']['random_names']['last_name']
    DateofBirth = personal_response['personal']['random_dates']['dob_format3']
    Gender = personal_response['personal']['random_gender']['en_gender']
    RegistrationDate = personal_response['personal']['random_dates']['RegistrationDate']
    PreferredCommunicationMethod = personal_response['personal']['random_comm_status']['comm_method_desc']
    Status = personal_response['personal']['random_status']['status_desc']
    StatusDate = personal_response['personal']['random_dates']['StatusDate']
    add_response = requests.get(address_url,headers=headers)
    time.sleep(2)
    if (
           add_response.status_code != 204 and
           add_response.headers["content-type"].strip().startswith("application/json")
       ):
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
    reference_type = contact_response['reference_info']['ref_type']
    reference_value = contact_response['reference_info']['ref_value']
    test1_response = requests.get(testdates_url,headers=headers)
    time.sleep(2)
    if (
           test1_response.status_code != 204 and
           test1_response.headers["content-type"].strip().startswith("application/json")
       ):   
            testdates_response = requests.get(testdates_url,headers=headers).json()
            appt_type = testdates_response['random_appt_testdetails']['EventType']
            appt_sub_type = testdates_response['random_appt_testdetails']['EventSubtype']
            appt_event_date = testdates_response['random_appt_testdetails']['LastEventDate']
            sight_event_type = testdates_response['random_sight_testdetails']['EventType']
            sight_event_sub_type = testdates_response['random_sight_testdetails']['EventSubtype']
            last_sight_event_date = testdates_response['random_sight_testdetails']['LastEventDate']
            next_sight_event_date = testdates_response['random_sight_testdetails']['NextEventDate']
            sight_test_flag = testdates_response['random_sight_testdetails']['OutsideRxFlag']
            cl_event_type = testdates_response['random_contactlens_testdetails']['EventType']
            cl_event_sub_type = testdates_response['random_contactlens_testdetails']['EventSubtype']
            last_cl_event_date = testdates_response['random_contactlens_testdetails']['LastEventDate']
            next_cl_event_date = testdates_response['random_contactlens_testdetails']['NextEventDate']
            cl_test_flag = testdates_response['random_contactlens_testdetails']['OutsideRxFlag']
    #   return(SystemId,ExternalId,Title,FirstName,LastName,DateofBirth,Gender,RegistrationDate,PreferredCommunicationMethod,Status,StatusDate,StreetAddressLine1,Town,District,Country,Postcode,email,homephone,workphone,mobile,ECommExtID,MCommExtID,HCommExtID,WCommExtID,appt_type,appt_sub_type,appt_event_date,sight_event_type,sight_event_sub_type,last_sight_event_date,next_sight_event_date,sight_test_flag,cl_event_type,cl_event_sub_type,last_cl_event_date,next_cl_event_date,cl_test_flag)
    data = f"""<SiebelMessage>
            <SystemId>{SystemId}</SystemId>
            <ExternalId>{ExternalId}</ExternalId>
            <ListOfSsOCHCustomer>
                <Contact>
                    <Title>{Title}</Title>
                    <FirstName>{FirstName}</FirstName>
                    <LastName>{LastName}</LastName>
                    <DateofBirth>{DateofBirth}</DateofBirth>
                    <Gender>{Gender}</Gender>
                    <RegistrationDate>{RegistrationDate}</RegistrationDate>
                    <PreferredCommunicationMethod>{PreferredCommunicationMethod}</PreferredCommunicationMethod>
                    <Status>{Status}</Status>
                    <StatusDate>{StatusDate}</StatusDate>
                    <ListOfPostalAddress>
                        <PostalAddress>
                            <IsPrimary>Y</IsPrimary>
                            <AddressType>Home</AddressType>
                            <StreetAddressLine1>{StreetAddressLine1}</StreetAddressLine1>
                        <!---   <StreetAddressLine2>1 Blackness Avenue</StreetAddressLine2> -->
                            <Town>{Town}</Town>
                        <!---   <District>Whitele Avenue</District> -->
                            <County>{District}</County>
                            <Country>{Country}</Country>
                            <Postcode>{Postcode}</Postcode>
                        </PostalAddress>
                    </ListOfPostalAddress>
                    <ListOfCommunicationAddress>
                        <CommunicationAddress>
                          <ExternalId>{HCommExtID}</ExternalId>
                          <Type>Phone</Type>
                          <SubType>Daytime</SubType>
                          <Address>{homephone}</Address>
                          <ActiveFlag>Y</ActiveFlag>
                        </CommunicationAddress>
                        <CommunicationAddress>
                          <ExternalId>{MCommExtID}</ExternalId>
                          <Type>Phone</Type>
                          <SubType>Mobile</SubType>
                          <Address>{mobile}</Address>
                          <ActiveFlag>Y</ActiveFlag>
                        </CommunicationAddress>
                        <CommunicationAddress>
                          <ExternalId>{WCommExtID}</ExternalId>
                          <Type>Phone</Type>
                          <SubType>Evening</SubType>
                          <Address>{workphone}</Address>
                          <ActiveFlag>Y</ActiveFlag>
                        </CommunicationAddress>
                        <CommunicationAddress>
                           <ExternalId>{ECommExtID}</ExternalId>
                           <Type>Email</Type>
                           <SubType>Email</SubType>
                           <Address>{email}</Address>
                           <ActiveFlag>Y</ActiveFlag>
                        </CommunicationAddress>
                    </ListOfCommunicationAddress>
                    <ListOfInteraction>
                        <Interaction>
                           <EventSubtype>{appt_sub_type}</EventSubtype>
                           <EventType>{appt_type}</EventType>
                           <LastEventDate>{appt_event_date}</LastEventDate>
                        </Interaction>
                        <Interaction>
                           <EventSubtype>{sight_event_sub_type}</EventSubtype>
                           <NextEventDate>{next_sight_event_date}</NextEventDate>
                           <OutsideRxFlag>{sight_test_flag}</OutsideRxFlag>
                           <EventType>{sight_event_type}</EventType>
                           <LastEventDate>{last_sight_event_date}</LastEventDate>
                           <EventPeriod>24</EventPeriod>
                        </Interaction>
                        <Interaction>
                           <EventSubtype>{cl_event_sub_type}</EventSubtype>
                           <NextEventDate>{next_cl_event_date}</NextEventDate>
                           <OutsideRxFlag>{cl_test_flag}</OutsideRxFlag>
                           <EventType>{cl_event_type}</EventType>
                           <LastEventDate>{last_cl_event_date}</LastEventDate>
                           <EventPeriod>12</EventPeriod>
                        </Interaction>
                    </ListOfInteraction>
                    <ListOfReference>
                        <Reference>
                           <ReferenceType>{reference_type}</ReferenceType>
                           <ReferenceValue>{reference_value}</ReferenceValue>
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
    return requests.post(args[0],headers=args[1], data=data)

headers = {'Content-Type': 'text/xml; charset=utf-8','Accept': 'application/xml'}

list_of_urls = [("https://osbpre.co.ad.specsavers.com/AudiologyCustomerUpdate/Audiology_PS",headers)]*1000

with ThreadPoolExecutor(max_workers=10) as pool:
    response_list = list(pool.map(post_url,list_of_urls))

for response in response_list:
    print(response)