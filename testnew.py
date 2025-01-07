import requests
import csv
import concurrent.futures
import time
import pandas as pd

# API endpoint
headers = {'Content-Type': 'application/json','x-api-key': '7ah5W8NQ.228oD7coJ9j8oh8LWMgNZy-m9vsVvfcey'}
# url = "https://api.example.com/data?limit=1000"
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

def get_sycle_data():
  with concurrent.futures.ThreadPoolExecutor(max_workers=CONNECTIONS) as executor:
    future_to_url = {executor.submit(load_url, url, TIMEOUT): url for url in urls}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
            out.update(data)
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
    return out


# print(get_sycle_data())
results = pd.DataFrame()
print("Running threaded:")
threaded_start = time.time()  
# with concurrent.futures.ThreadPoolExecutor(max_workers=CONNECTIONS) as executor:
for i in range(100):
    df = pd.DataFrame.from_dict(get_sycle_data())
    test = df['personal']['random_names']['fake_first_name'],df['personal']['random_names']['fake_last_name']
    data = pd.DataFrame([test],columns=['firstname','lastname'])
    results = pd.concat([results,data])
    print(results.shape)
results.to_csv(f'C:/myapi/{pd.to_datetime("now", utc=True).date()}_xml_parse_results.csv', index=False) 
# with open("C:/myapi/data.csv", "w", newline="") as file:
#         writer = csv.writer(file)

        # Write header row
        # writer.writerow(["firstname", "lastname", "fullname"])          

        # Fetch and write data in batches
        # with concurrent.futures.ThreadPoolExecutor(max_workers=CONNECTIONS) as executor:
        #  for i in range(100):
        #   firstname = get_sycle_data()['personal']['random_names']['fake_first_name']
        #   lastname = get_sycle_data()['personal']['random_names']['fake_last_name']
        #   fullname = get_sycle_data()['personal']['random_names']['fake_full_name']
        #   writer.writerow([firstname, lastname, fullname])
print("Threaded time:", time.time() - threaded_start)

# # Open the CSV file for writing
# with open("data.csv", "w", newline="") as file:
#     writer = csv.writer(file)

#     # Write header row
#     writer.writerow(["column1", "column2", "column3", ...])

#     # Fetch and write data in batches
#     for i in range(100):
#         response = requests.get(url + "&offset=" + str(i * 1000))
#         data = response.json()

#         for item in data:
#             writer.writerow([item["column1"], item["column2"], item["column3"], ...])