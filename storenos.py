# importing the required modules
import glob
import random
import csv
  
# specifying the path to csv files
path = "resources"
  
# csv files in the path
files = glob.glob(path + "/*.csv")

def random_store_details():  
  with open("resources/stores.csv", "r",encoding="utf8") as store_csv_file:
    csv_reader = csv.reader(store_csv_file, delimiter=',')
    next(csv_reader)
    filtered_list = list(filter(None, csv_reader))
    uk_store = random.choice([row for row in filtered_list if ((row[2] == '1' or row[2] == '4' or row[2] == '5') and (row[1] != '') and (row[1] != 'null'))])
    ie_store = random.choice([row for row in filtered_list if ((row[2] == '3') and (row[1] == 'Eire') and (row[1] != '') and (row[1] != 'null'))])
    nl_store = random.choice([row for row in filtered_list if ((row[2] == '2') and (row[1] == 'Nederland') and (row[1] != '') and (row[1] != 'null'))])
    esp_store = random.choice([row for row in filtered_list if ((row[2] == '9') and (row[1] != '') and (row[1] != 'null'))])
    aus_store = random.choice([row for row in filtered_list if ((row[2] == '13') and (row[1] != '') and (row[1] != 'null'))])
    return {"uk_store_no":uk_store[0],"uk_store_country" :uk_store[1],
            "ie_store_no":ie_store[0],"ie_store_country" :ie_store[1],
            "nl_store_no":nl_store[0],"nl_store_country" :nl_store[1],
            "esp_store_no":esp_store[0],"es_store_country" :esp_store[1],
            "aus_store_no":aus_store[0],"aus_store_country" :aus_store[1]}

def random_uk_store():  
  with open("resources/ukstores.csv", "r",encoding="utf8") as uk_store_csv_file:
    csv_reader = csv.reader(uk_store_csv_file, delimiter=',')
    # This skips over the header row
    next(csv_reader)
    filtered_list = list(filter(None, csv_reader))
    random_store = (random.choice([row for row in filtered_list]))
    return {"uk_store_no":random_store[0]}

def get_random_uk_address(): 
  country_list = ['England', 'Wales', 'Scotland', 'Northern Ireland','United Kingdon', 'UK']
  country = random.choice(country_list)
  with open("resources/UKaddress.csv", "r",encoding="utf8") as address_csv_file:
    csv_reader = csv.reader(address_csv_file, delimiter=',')
    # This skips over the header row
    next(csv_reader)
    filtered_list = list(filter(None, csv_reader))
    address = (random.choice([row for row in filtered_list]))
  return {"addressline1":address[0],"city" :address[1],"county":address[2],"postcode":address[3],"country":country}

def get_random_nl_address(): 
  with open("resources/NLaddress.csv", "r",encoding="utf8") as address_csv_file:
    csv_reader = csv.reader(address_csv_file, delimiter=',')
    # This skips over the header row
    next(csv_reader)
    filtered_list = list(filter(None, csv_reader))
    address = (random.choice([row for row in filtered_list]))
    return {"addressline1":address[0],"city" :address[1],"county":address[2],"postcode":address[3],"country": 'Netherlands'}

def get_random_es_address(): 
  with open("resources/ESaddress.csv", "r",encoding="utf8") as address_csv_file:
    csv_reader = csv.reader(address_csv_file, delimiter=',')
    # This skips over the header row
    next(csv_reader)
    filtered_list = list(filter(None, csv_reader))
    address = (random.choice([row for row in filtered_list]))
    return {"addressline1":address[0],"city" :address[1],"county":address[2],"postcode":address[3],"country": 'Spain'}

def get_random_roi_address(): 
  with open("resources/ROIaddress.csv", "r",encoding="utf8") as address_csv_file:
    csv_reader = csv.reader(address_csv_file, delimiter=',')
    # This skips over the header row
    next(csv_reader)
    filtered_list = list(filter(None, csv_reader))
    address = (random.choice([row for row in filtered_list]))
    return {"addressline1":address[0],"city" :address[1],"county":address[2],"postcode":address[3],"country": random.choice(['Ireland','Republic of Ireland'])}