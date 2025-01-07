import random
from datetime import datetime,timedelta
from dateutil.relativedelta import relativedelta
import random
import csv

def get_random_CLtest():
    start_date = datetime(2017, 1, 1, 00, 00, 00)
    end_date = datetime.now() - timedelta(1)
    time_between_dates = (end_date - start_date)
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)
    LastEventDate = datetime.strftime(random_date, '%Y-%m-%d') + 'T00:00:00Z'
    random_date1 = random_date + relativedelta(months=24)
    NextEventDate = datetime.strftime(random_date1, '%Y-%m-%d') + 'T00:00:00Z'
    with open("resources/CLtesttypes.csv", "r") as store_csv_file:
       csv_reader = csv.reader(store_csv_file, delimiter=',')
      # This skips over the header row
       next(csv_reader)
       filtered_list = list(filter(None, csv_reader))
       CLEventtype = (random.choice([row for row in filtered_list]))
       if(CLEventtype[1] == 'Outside Prescription'):
        OutsideRxFlag = 'Y'
       else: 
        OutsideRxFlag = 'N'
    return {"EventType":CLEventtype[0],"EventSubtype" :CLEventtype[1],"LastEventDate":LastEventDate,"EventPeriod": 24,"NextEventDate":NextEventDate,"OutsideRxFlag":OutsideRxFlag}

def get_random_sighttest():
    start_date = datetime(2017, 1, 1, 00, 00, 00)
    end_date = datetime.now() - timedelta(1)
    time_between_dates = (end_date - start_date)
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)
    LastEventDate = datetime.strftime(random_date, '%Y-%m-%d') + 'T00:00:00Z'
    random_date1 = random_date + relativedelta(months=12)
    NextEventDate = datetime.strftime(random_date1, '%Y-%m-%d') + 'T00:00:00Z'
    with open("resources/sighttesttypes.csv", "r") as store_csv_file:
       csv_reader = csv.reader(store_csv_file, delimiter=',')
      # This skips over the header row
       next(csv_reader)
       filtered_list = list(filter(None, csv_reader))
       sighteventtype = (random.choice([row for row in filtered_list]))
       if(sighteventtype[1] == 'Outside Prescription'):
        OutsideRxFlag = 'Y'
       else: 
        OutsideRxFlag = 'N'
    return {"EventType":sighteventtype[0],"EventSubtype" :sighteventtype[1],"LastEventDate":LastEventDate,"EventPeriod": 12,"NextEventDate":NextEventDate,"OutsideRxFlag":OutsideRxFlag}

def get_random_appointment():
    start_date = datetime(2017, 1, 1, 00, 00, 00)
    end_date = datetime.now() - timedelta(1)
    time_between_dates = (end_date - start_date)
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)
    LastEventDate = datetime.strftime(random_date, '%Y-%m-%d') + 'T00:00:00Z'
    with open("resources/Appttypes.csv", "r") as store_csv_file:
       csv_reader = csv.reader(store_csv_file, delimiter=',')
      # This skips over the header row
       next(csv_reader)
       filtered_list = list(filter(None, csv_reader))
       appteventtype = (random.choice([row for row in filtered_list]))
    return {"EventType":appteventtype[0],"EventSubtype" :appteventtype[1],"LastEventDate":LastEventDate}