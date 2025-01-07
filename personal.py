import random
import string
from random import randrange
from datetime import datetime,timedelta
from dateutil.relativedelta import relativedelta
import requests
import xml.etree.ElementTree as ET
import names

def get_random_title_from_List_format():
    title_list = ['Mr','Mrs','Miss','Ms','Master','Dr','Reverend','Sister','Lady','Father','Professor','Lord','Captain','Baron','Countess','Duchess','Mw','Dhr','Dña.','D.','Sir','Rabbi','Dame','Flight Lt.','Major','HRH',
'General','Sergeant','Colonel','Duke','Earl','Brigadier','Honourable','Canon','Commander','Lieutenant','Lieut. Col','Lieut. Com','Ds','Drs','Lieut. Gov','Mej','Count','Mx']
    # using random.choice() to
    random_title = random.choice(title_list)
    return random_title

def get_random_string(length):
    # With combination of lower and upper case
    letters = string.ascii_uppercase
    spec_chars = ["-","'"]
    first_name = ''.join(random.choice(string.ascii_letters) for i in range(length))
    last_name = ''.join(random.choice(string.ascii_letters) for i in range(length))
    spec_last_name = random.choice(string.ascii_uppercase) + random.choice(spec_chars) + ''.join(random.choice(string.ascii_letters) for i in range(length))
    middle_name = ''.join(random.choice(letters) for i in range(1)) + '.' + ''.join(random.choice(letters) for i in range(1))
    fake_first_name = names.get_first_name()
    fake_last_name = names.get_last_name()
    # print random string
    return {"first_name": first_name,"middle_name" : middle_name, "last_name": last_name , "special_last_name": spec_last_name, "full_name" : (first_name + ' ' + middle_name + ' ' + last_name), "fake_first_name" : fake_first_name,"fake_last_name" :fake_last_name,"fake_full_name" : (fake_first_name  + ' ' + fake_last_name)}

def get_random_value_from_List_format():
    english_gender_list = ['Male', 'Female', 'Unknown', 'Unspecified']
    nl_gender_list = ['Mannelijk','Female','Onbekend','Ongespecifieerd']
    english_gender_code_list = ['m', 'f', 'U', 'US']
    random_english_gedner = random.choice(english_gender_list)
    random_dutch_gedner = random.choice(nl_gender_list)
    random_english_gedner_code = random.choice(english_gender_code_list)
    return {"en_gender": random_english_gedner,"nl_gender": random_dutch_gedner,"en_gender_code": random_english_gedner_code}

def get_random_status_from_List_format():
    status_desc_list = ['Registered', 'Active', 'Closed', 'Deceased']
    status_code_list = ['R', 'A', 'C', 'D', 'r', 'a', 'c', 'd']
    status_desc = random.choice(status_desc_list)
    status_code = random.choice(status_code_list)
    return {"status_desc": status_desc,"status_code":status_code}

def get_random_comm_method_from_List_format():
    comm_method_desc_list = ['Phone Evening', 'Phone Daytime', 'Phone Mobile', 'Email']
    comm_method_desc = random.choice(comm_method_desc_list)
    return {"comm_method_desc": comm_method_desc}

def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    input = start + timedelta(seconds=random_second)
    input1 = str(input.date()) + 'T'
    input2 = str(input.time()) + 'Z'
    return(input1+input2)
# print(str(random_date(d1, d2)))  
# d1 = datetime.strptime('1/1/2019 12:30 PM', '%m/%d/%Y %I:%M %p')
# d2 = datetime.strptime('1/1/2023 12:00 AM', '%m/%d/%Y %I:%M %p') 

def get_random_dob_format():
    start_date = datetime(1900, 1, 1)
    end_date = datetime(2018, 12, 1)
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    max_date = today - timedelta(days=10)
    RegistrationDate = min(random_date + relativedelta(months=120), max_date)
    RegistrationDate1 = RegistrationDate.strftime('%Y-%m-%dT00:00:00Z')
    StatusDate = min(RegistrationDate + relativedelta(months=1), max_date)
    StatusDate = StatusDate.strftime('%Y-%m-%dT00:00:00Z')
    random_date1 = random_date.strftime('%Y-%m-%d')
    random_date2 = random_date.strftime('%Y-%m-%dT00:00:00Z')
    random_date3 = random_date.strftime('%d/%m/%Y %I:%M %p')
    random_date4 = random_date.strftime('%Y-%m-%d %H:%M:%S')
    days_in_year = 365.2425
    age = int((today - random_date).days / days_in_year)
    return {
        "dob_format1": random_date1,"dob_format2": random_date,
        "dob_format3": random_date2,"dob_format4": random_date3,
        "dob_format5": random_date4,"RegistrationDate": RegistrationDate1,
        "StatusDate": StatusDate,"age": age
    }

def get_NL_address():
   ps_code = ['1*','2*','3*','4*','5*','6*','7*','8*','9*' ]
   ps_format1 = random.choice(ps_code)
   url = 'https://osbpre.co.ad.specsavers.com/savs/validateaddress/search/v1?maxresults=100&countryiso=NLD&postcode=' + str(ps_format1)
   headers = {'Content-Type': 'application/xml;charset=utf-8'}

   response = requests.request("GET", url, headers=headers).text
   root = ET.fromstring(response)
   add1 = random.choice(list([(elem.text) for elem in root.iter() if (elem.tag == 'addressLine1')]))
   add2 = random.choice(list([(elem.text) for elem in root.iter() if (elem.tag == 'addressLine2')]))
   add3 = random.choice(list([(elem.text) for elem in root.iter() if (elem.tag == 'addressLine3')]))
   return {"addressline1":add1,"addressline2" :add2,"country":add3}

def get_minor_dates():
    start_date = datetime.now() + relativedelta(years = -16)
    end_date = datetime.now()
    days_in_year = 365.2425
    time_between_dates = (end_date - start_date)
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)
    minor_date = datetime.strftime(random_date, '%Y-%m-%d')
    minor_age = int((datetime.now() - random_date).days / days_in_year)
    return {"minor_dob":minor_date,"minor_age":minor_age}