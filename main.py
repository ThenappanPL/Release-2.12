from typing import List
from fastapi import FastAPI, HTTPException
from uuid import UUID,uuid4
from models import User, Gender, Role, UserUpdateRequest, User2, User1, personal
import xml.etree.ElementTree as ET
from datetime import datetime
from personal import get_random_title_from_List_format,get_random_string,get_random_status_from_List_format,get_random_value_from_List_format,get_random_dob_format,get_random_comm_method_from_List_format,get_random_dob_format,get_NL_address,get_minor_dates,random_date
from address import get_uk_address
from phone_number import uk_mobile_no, uk_homephone, nl_mobile_no, nl_homephone, ie_mobile_no, ie_homephone, esp_mobile_no, esp_homephone, email_address,random_identifier
from passwords import get_random_token,get_random_id,get_random_password,get_random_secure_password,get_string,get_random_numbers
from storenos import random_store_details,random_uk_store,get_random_uk_address,get_random_nl_address,get_random_es_address,get_random_roi_address
from testdetails import get_random_CLtest,get_random_sighttest,get_random_appointment
from ochrequests_UK import get_socrates_uk_data, get_consent_socrates_uk_data, get_merged_sycle_gb_data, get_mergedconsent_sycle_gb_data
from ochrequests_IE import get_socrates_ie_data, get_consent_ie_data, get_merged_sycle_ie_data, get_mergedconsent_sycle_ie_data
from ochrequests_NL import get_socrates_nl_data, get_consent_nl_data
from ochrequests_ESP import get_socrates_esp_data, get_consent_esp_data
from syclerequests_GB import get_sycle_uk_data,get_sycle_consent_uk_data
from syclerequests_IE import get_sycle_ie_data,get_sycle_consent_ie_data
from prescription import random_cl_rx, random_presribed_rx
from supptest_1 import ggg_test

tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users. The **login** logic is also here. Do not use for now",
    },
    {
        "name": "OCH Payload",
        "description": "Oracle Customer Hub Payloads generated for test team using random service",
    },
    {
        "name": "Random",
        "description": "Random test data can be generated for each service",

        },
]

d1 = datetime.strptime('1/1/2019 12:30 PM', '%m/%d/%Y %I:%M %p')
d2 = datetime.strptime('1/1/2023 12:00 AM', '%m/%d/%Y %I:%M %p')

app = FastAPI(openapi_tags=tags_metadata)

db: List[User] = [
    User(
         id = UUID("5e6d9e42-b45b-46c0-81d2-af26050ad466"), 
         first_name=str(get_random_string(8)), 
         last_name="Ryan",
         gender=Gender.female,
         roles=[Role.student] 
    ),
    User(
         id = UUID("2db3b062-a0d3-4794-b807-1b9431f885b4"), 
         first_name=str(get_random_string(8)), 
         last_name="Jones",
         gender=Gender.male,
         roles=[Role.admin, Role.user] 
    )
]

@app.get("/")
async def root():
    return {"Hello": "Mya33p"}

@app.get("/api/v1/users", tags=["users"])
async def fetch_users():
    return {"data" : db}

@app.get("/api/v1/random_personal",tags=["Random"], status_code=200)
async def fetch_random_personal_information():
    return {"personal" :{"random_title": get_random_title_from_List_format(),
                        "random_names" : get_random_string(8),
             "random_gender": get_random_value_from_List_format(),
             "random_status": get_random_status_from_List_format(),
             "random_comm_status": get_random_comm_method_from_List_format(),
             "random_dates": get_random_dob_format(),
             "random_datetime": random_date(start=d1,end=d2),
             "random_minor_dates": get_minor_dates()}}

@app.get("/api/v1/random_address",tags=["Random"],status_code=200)
async def fetch_random_address_per_region():
    return {"contrywise_address" :{"NL_address": get_random_nl_address(),
                                   "UK_address": get_random_uk_address(),
                                   "ESP_address": get_random_es_address(),
                                   "ROI_address": get_random_roi_address()}}

@app.get("/api/v1/random_address_from_savs", tags=["Random"])
async def fetch_random_address_per_region_from_savs_DO_NOT_USE():
    return {"contrywise_address" :{"NL_address": get_NL_address(),
                                   "UK_address": get_uk_address()}}

@app.get("/api/v1/random_contact",tags=["Random"],status_code=200)
async def fetch_random_phone_numbers_per_region():
    return {"contrywise_random_phoneno" :{
                                          "uk_mobile_number": uk_mobile_no(),
                                          "uk_homephone_number": uk_homephone(),
                                          "nl_mobile_number": nl_mobile_no(),
                                          "nl_homephone_number": nl_homephone(),
                                          "ie_mobile_number": ie_mobile_no(),
                                          "ie_homephone_number": ie_homephone(),
                                          "esp_mobile_number": esp_mobile_no(),
                                          "esp_homephone_number": esp_homephone()
                                          },
           "email_random" : email_address(6),
           "reference_info" :random_identifier()
                                          }       

@app.get("/api/v1/random_string_numbers",tags=["Random"],status_code=200)
async def fetch_random_password_or_random_string_or_random_numbers():     
    return {"Secure_hexadecimal_string_token" : get_random_token(),
            "Secure_unique_string_id": get_random_id(),
            "random_password": get_random_password(),
            "secure_random_password": get_random_secure_password(),
            "random_string": get_string(6,2),
            "random_numbers": get_random_numbers()}     

@app.get("/api/v1/random_stores",tags=["Random"],status_code=200)
async def fetch_random_store_infromation():     
    return {"specsaver_store" : random_uk_store(),
            "specsaver_store_all" : random_store_details()}

@app.get("/api/v1/random_test_dates",tags=["Random"],status_code=200)
async def fetch_random_testdetails_or_testdates():     
    return {"random_contactlens_testdetails" : get_random_CLtest(),
            "random_sight_testdetails" : get_random_sighttest(),
            "random_appt_testdetails" : get_random_appointment()}

@app.get("/api/v1/random_prescription",tags=["Random"],status_code=200)
async def fetch_random_Rx_details():     
    return {"random_contactlens_rx" : random_cl_rx(),
             "random_glasses_rx" : random_presribed_rx()}

@app.get("/api/v1/och_socrates_payload/{country}",tags=["OCH Payload"],status_code=200)
async def fetch_random_och_socrates_payload_per_region(country: str):
    if country in ('uk','UK'):
      return get_socrates_uk_data()
    if country in ('ie','IE'):
      return get_socrates_ie_data()
    if country in ('nl','NL'):
      return get_socrates_nl_data()
    if country in ('esp','ESP'):
      return get_socrates_esp_data()
    if country != ('uk','UK','ie','IE','nl','NL','esp','ESP'):
      raise HTTPException(
        status_code = 404,
        detail=f"country {country} not found, acceptable values are NL, IE, ESP and UK"
    )

@app.get("/api/v1/och_merge_payload/{country}",tags=["OCH Payload"],status_code=200)
async def fetch_random_och_merged_payload_per_region(country: str):
    if country in ('uk','UK'):
      return get_merged_sycle_gb_data()
    if country in ('ie','IE'):
      return get_merged_sycle_ie_data()
    if country != ('uk','UK','ie','IE','nl','NL','esp','ESP'):
      raise HTTPException(
        status_code = 404,
        detail=f"country {country} not found, acceptable values are UK and IE"
    )

@app.get("/api/v1/och_mergedconsent_payload/{country}",tags=["OCH Payload"],status_code=200)
async def fetch_random_och_mergedsycleconsent_payload_per_region(country: str):
    if country in ('uk','UK'):
      return get_mergedconsent_sycle_gb_data()
    if country in ('ie','IE'):
      return get_mergedconsent_sycle_ie_data()
    if country != ('uk','UK','ie','IE','nl','NL','esp','ESP'):
      raise HTTPException(
        status_code = 404,
        detail=f"country {country} not found, acceptable values are UK and IE"
    )

@app.get("/api/v1/och_socrates_consent_payload/{country}",tags=["OCH Payload"],status_code=200)
async def fetch_random_och_consent_payload_per_region(country: str):
    if country in ('uk','UK'):
      return get_consent_socrates_uk_data()
    if country in ('ie','IE'):
      return get_consent_ie_data()
    if country in ('nl','NL'):
      return get_consent_nl_data()
    if country in ('esp','ESP'):
      return get_consent_esp_data()
    if country != ('uk','UK','ie','IE','nl','NL','esp','ESP'):
      raise HTTPException(
        status_code = 404,
        detail=f"country {country} not found, acceptable values are NL, IE, ESP and UK"
    )

@app.get("/api/v1/och_sycle_payload/{country}",tags=["OCH Payload"],status_code=200)
async def fetch_random_och_sycle_payload_per_region(country: str):
    if country in ('uk','UK'):
      return get_sycle_uk_data()
    if country in ('ie','IE'):
      return get_sycle_ie_data()
    if country != ('uk','UK','ie','IE'):
      raise HTTPException(
        status_code = 404,
        detail=f"country {country} not found, acceptable values are IE and UK"
    )

@app.get("/api/v1/och_sycle_consent_payload/{country}",tags=["OCH Payload"],status_code=200)
async def fetch_random_och_sycle_consent_payload_per_region(country: str):
    if country in ('uk','UK'):
      return get_sycle_consent_uk_data()
    if country in ('ie','IE'):
      return get_sycle_consent_ie_data()
    if country != ('uk','UK','ie','IE'):
      raise HTTPException(
        status_code = 404,
        detail=f"country {country} not found, acceptable values are IE and UK"
    )

@app.get("/api/v1/och_suppression_payload",tags=["OCH Payload"],status_code=200)
async def fetch_random_och_suppression_payload_UK_region():
    return ggg_test()
       
@app.post("/api/v1/users", tags=["users"])
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{user_id}", tags=["users"])
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"id": user.id}
    raise HTTPException(
        status_code = 404,
        detail=f"user with id: {user_id} does not exists"
    )

@app.put("/api/v1/users/{user_id}", tags=["users"])
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles   
            return {"id": user.id}
    raise HTTPException(
        status_code = 404,
        detail=f"user with id: {user_id} does not exists"
    )