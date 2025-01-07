from random import randrange
import requests
from datetime import datetime,timedelta,date
from dateutil.relativedelta import relativedelta
import random
import string
import decimal
import glob
import concurrent.futures
import csv
import numpy as np
import time
from multiprocessing import Pool

first_name = names.get_name()
print(first_name)
# from numpy import arange
    
# start_date = datetime(1900, 1, 1, 00, 00, 00)
# end_date = datetime(2022, 12, 1, 00, 00, 00)
# time_between_dates = (end_date - start_date)
# days_between_dates = time_between_dates.days
# random_number_of_days = random.randrange(days_between_dates)
# random_date = start_date + timedelta(days=random_number_of_days)
# # print(random_date)
# random_date1 = datetime.strftime(random_date, '%Y,%m,%d')
# # random_date1 = str(random_date) + 'T00:00:00Z'
# random_date2 = datetime.strftime(random_date, '%d/%m/%Y %I:%M %p')
# random_date3 = datetime.strftime(random_date, '%Y-%m-%d %H:%M:%S')
# # print(random_date, random_date1,random_date2,random_date3)

# start_date = datetime.date(2020, 1, 1)
# end_date = datetime.date(2020, 2, 1)

# time_between_dates = end_date - start_date
# days_between_dates = time_between_dates.days
# random_number_of_days = random.randrange(days_between_dates)
# random_date = start_date + datetime.timedelta(days=random_number_of_days)

# print(random_date)

# def get_random_dob_format1():
#     start_date = datetime.datetime(1900, 1, 1, 00, 00 ,10)
#     end_date = datetime.datetime(2022, 11, 1, 11, 10 ,10)
#     time_between_dates = (end_date - start_date)
#     days_between_dates = time_between_dates.days
#     random_number_of_days = random.randrange(days_between_dates)
#     random_date2 = start_date + datetime.timedelta(days=random_number_of_days)
#     return random_date2
# print(get_random_dob_format1())


for i in range(3):
    # get random string of length 6 without repeating letters
    result_str = ''.join(random.sample(string.ascii_lowercase, 2))
    # print(result_str)

def get_random_string():
    # choose from all lowercase letter
    letters = string.ascii_uppercase
    # result_str = ''.join(random.choice(letters)) + '.' + ''.join(random.choice(letters))
    result_str = ''.join(random.choice(letters) for i in range(1)) + '.' + ''.join(random.choice(letters) for i in range(1))
    # print(result_str)
# get_random_string()

def get_random_string(length):
    # With combination of lower and upper case
    letters = string.ascii_uppercase
    first_name = ''.join(random.choice(string.ascii_letters) for i in range(length))
    last_name = ''.join(random.choice(string.ascii_letters) for i in range(length))
    middle_name = ''.join(random.choice(letters) for i in range(1)) + '.' + ''.join(random.choice(letters) for i in range(1))
    # print random string
    # return ({"first_name": first_name,"middle_name" : middle_name, "last_name": last_name, "full_name" : (first_name + ' ' + middle_name + ' ' + last_name)})
# print(get_random_string(8))

# def get_email_address():
#     email_suffix = ['@gmail.com','@gmail.co.uk','@hotmail.co.uk','@hotmail.com','@aol.com','@aol.co.uk','@yahoo.com','@yahoo.co.uk','@specsavers.com' ]
#     email_suffix_randomhome = random.choice(email_suffix)
#     for key in get_random_string(8):
#         print("key:", first_name, "Value:", d[first_name])
#     return {"email":email_random}

def calculateAge(birthDate):
    days_in_year = 365.2425   
    age = int((date.today() - birthDate).days / days_in_year)
    # return age
         
# Driver code
# print(calculateAge(random_date), "years")

start_date = datetime(2017, 1, 1, 00, 00, 00)
end_date = datetime.now() - timedelta(1)
time_between_dates = (end_date - start_date)
days_between_dates = time_between_dates.days
random_number_of_days = random.randrange(days_between_dates)
random_date = start_date + timedelta(days=random_number_of_days)
LastEventDate = datetime.strftime(random_date, '%Y-%m-%d') + 'T00:00:00Z'
random_date1 = random_date + relativedelta(months=24)
NextEventDate = datetime.strftime(random_date1, '%Y-%m-%d') + 'T00:00:00Z'
# print(LastEventDate)
# print(NextEventDate)
# days_in_year = 365.2425   
# age = int((date.today() - birthDate).days / days_in_year)
# print(type(random_date))
# print(random_date)
# print(random_date.year,random_date.month,random_date.day)

mydict1 = {"personal" :{"firstname": str(get_random_string(8)), 
            "lastname": str(get_random_string(8)),
             "roles": {'admin', 'user'}}}
for x in mydict1:
    val = mydict1[x]
    # print(val)

a = {"personal" :{"firstname": mydict1['personal']['firstname'], 
                  "lastname": mydict1['personal']['lastname'],
                  "permission": mydict1['personal']['roles'],
                  "fullname": (mydict1['personal']['firstname'] + ' ' + mydict1['personal']['lastname'])}}

# url = 'https://tp_spec.deta.dev/api/v1/random_personal'
# headers = {'Content-Type': 'application/json'}

# def get_web_data():
#   response = requests.get(url,headers=headers).json()
#   Title = response['personal']['random_title']
#   FirstName = response['personal']['random_names']['first_name']
#   LastName = response['personal']['random_names']['last_name']
#   return(Title,FirstName,LastName)
# print(get_web_data())


start = datetime.strptime('1/1/2008 1:30 PM', '%m/%d/%Y %I:%M %p')
end = datetime.strptime('1/1/2009 4:50 AM', '%m/%d/%Y %I:%M %p')
delta = end - start
# print(delta)
int_delta = (delta.days * 24 * 60 * 60) +  delta.seconds
# print(int_delta)
random_second = randrange(int_delta)
# print(random_second)
input = start + timedelta(seconds=random_second)
input1 = str(input.date()) + 'T'
input2 = str(input.time()) + 'Z'
# input2 = str(timedelta(seconds=random_second)) + 'Z'
# input1 = (str(input1) + 'T')
# print(input1+input2)

# def random_date(start, end):
#     d1 = datetime.strptime('1/1/2008 1:30 PM', '%m/%d/%Y %I:%M %p')
#     d2 = datetime.strptime('1/1/2009 4:50 AM', '%m/%d/%Y %I:%M %p')
#     delta = end - start
#     int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
#     random_second = randrange(int_delta)
#     start + timedelta(seconds=random_second)
#     return str((random_date(d1, d2)) + 'Z') 
# print str((random_date(d1, d2)) + 'Z')


start_date = datetime.now() + relativedelta(years = -16)
end_date = datetime.now()
days_in_year = 365.2425
time_between_dates = (end_date - start_date)
days_between_dates = time_between_dates.days
random_number_of_days = random.randrange(days_between_dates)
random_date = start_date + timedelta(days=random_number_of_days)
minor_date = datetime.strftime(random_date, '%Y-%m-%d')
minor_age = int((datetime.now() - random_date).days / days_in_year)



with open("resources/stores.csv", "r") as store_csv_file:
    csv_reader = csv.reader(store_csv_file, delimiter=',')
    # This skips over the header row
    next(csv_reader)
    filtered_list = list(filter(None, csv_reader))
    random_store = random.choice([row for row in filtered_list if row[2] == '1' and row != '' and row != None])
    # print({"store_no":random_store[0],"store_country" :random_store[1]})

singed_int = random.randrange(-60, -1)
# print(singed_int)
float_neg = round(random.uniform(+6.00, -6.00), 2)
# print(float_neg)
float_post = round(random.uniform(10.99, 0.01), 1)
# print(float_post)

int_num = random.choice(range(10, 1000))
float_num = int_num/10
# print(float_num)


def float_range(start, stop, step):
  while start < stop:
    yield float(start)
    start += decimal.Decimal(step)

# print(list(float_range(5, -6, '0.25')))

#specific range
min = +2.50
max = -3.00

#generate a random floating point number
f = min + (max-min)*random.random()
float_neg = round((f), 2)
# print(f)

# def uniform(a, b):
#     "Get a random number in the range [a, b) or [a, b] depending on rounding."
#     return a + (b-a) * random.random()
# print(round(random.uniform(+2.50,-3.00),2))

# print("\n\nTest 2:")
threshold_range1 = np.arange(-6.00,+6.00,0.25) 
threshold_range2 = np.arange(-12.00,-6.00,0.50)
threshold_range = (threshold_range1.tolist() + threshold_range2.tolist())
# print(threshold_range)
result=random.choice(np.round(threshold_range, 2))
result_rx = (f"{result:+.2f}")
result_rx1 = f"{result:{'+.2f' if result else ''}}"
result_rx2 = f'{result:{1}}'.format(result, '+' if result else '')
# print(result_rx)
# print(result_rx1)
# print(result_rx2)
# if (result_rx == '+0.00'):
#     result_rx = '0.00'
# else:
#     result_rx
# print(result_rx)
store_url = 'https://tp_spec.deta.dev/api/v1/random_stores'
nos_url = 'https://tp_spec.deta.dev/api/v1/random_string_numbers'
personal_url = 'https://tp_spec.deta.dev/api/v1/random_personal'
contact_url = 'https://tp_spec.deta.dev/api/v1/random_contact'
headers = {'Content-Type': 'application/json','x-api-key': '7ah5W8NQ.228oD7coJ9j8oh8LWMgNZy-m9vsVvfcey'}

# suppression_request ='CRN|EPOS_NUMBER|COMMUNICATION_ADDRESS|CLEANSE_CODE|CLEANSE_DATE\n'
# suppression_request1 = []
# for i in range(4):
#    systemstore_response = requests.get(store_url,headers=headers).json()
#    customerno_response = requests.get(nos_url,headers=headers).json()
#    contact_response = requests.get(contact_url,headers=headers).json()
#    personal_response = requests.get(personal_url,headers=headers).json()
#    suppression_request1 += [f"""{customerno_response['random_numbers']['ExternalId']}|{systemstore_response['specsaver_store']['uk_store_no']}|{contact_response['contrywise_random_phoneno']['uk_mobile_number']}|{random.choice(['S0','S1','S2','S3'])}|{personal_response['personal']['random_dates']['dob_format1']}"""]
#    txt = '\n'.join(suppression_request1)
# print(suppression_request+txt)

# def fetch(session, store_url):
#   session.headers.update({'x-api-key': '7ah5W8NQ.228oD7coJ9j8oh8LWMgNZy-m9vsVvfcey'})
#   with session.get(store_url) as response:
#         a = (response.json()['specsaver_store']['uk_store_no'])
# #   print(fetch(session, store_url))

# session = requests.Session()
# session.headers.update({'x-api-key': '7ah5W8NQ.228oD7coJ9j8oh8LWMgNZy-m9vsVvfcey'})
# with session.get(store_url) as response:
#         print(response.json()['specsaver_store']['uk_store_no'])

# session.headers.update({'x-api-key': '7ah5W8NQ.228oD7coJ9j8oh8LWMgNZy-m9vsVvfcey'})
# with session.get(store_url) as response:
#         a = (response.json()['specsaver_store']['uk_store_no'])
#         print(a)

headers = {'Content-Type': 'application/json','x-api-key': '7ah5W8NQ.228oD7coJ9j8oh8LWMgNZy-m9vsVvfcey'}
suppression_request ='CRN|EPOS_NUMBER|COMMUNICATION_ADDRESS|CLEANSE_CODE|CLEANSE_DATE\n'
out = {}
urls = []
CONNECTIONS = 70
TIMEOUT = 5

with open("resources/url_list.txt") as reader:
    for url in reader:
        urls.append(url.strip())

def load_url(url, timeout):
   with requests.Session() as s:
    resp = s.get(url, timeout=timeout,headers=headers).json()
    return resp

print("Running threaded:")
threaded_start = time.time()
def ggg_test():
  suppression_request1 = []
  with concurrent.futures.ThreadPoolExecutor(max_workers=CONNECTIONS) as executor:
    future_to_url = {executor.submit(load_url, url, TIMEOUT): url for url in urls}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
            out.update(data)
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
    print("Threaded time:", time.time() - threaded_start)
    # a = out['random_contactlens_testdetails']['LastEventDate']
    # b = out['random_contactlens_testdetails']['NextEventDate']
    # c = out['personal']['random_title']
  return out
    # return {"event_date" : out['random_contactlens_testdetails']['LastEventDate'],"next_event_date" : out['random_contactlens_testdetails']['NextEventDate']}

list_of_urls = [(urls,headers)]

# if __name__ == '__main__':
#     with Pool(5) as p:
#         print(p.map(load_url,url,TIMEOUT))