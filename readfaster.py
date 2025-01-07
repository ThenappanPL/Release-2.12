import requests
import csv
from timer import timer
import time
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

headers = {'Content-Type': 'application/json','x-api-key': '7ah5W8NQ.228oD7coJ9j8oh8LWMgNZy-m9vsVvfcey'}
personal_url = 'https://tp_spec.deta.dev/api/v1/random_personal'
urls = []
df = []
CONNECTIONS = 10
TIMEOUT = 5

def fetch(session, personal_url):
    results = pd.DataFrame()
    session.headers.update({'x-api-key': '7ah5W8NQ.228oD7coJ9j8oh8LWMgNZy-m9vsVvfcey'})
    with session.get(personal_url) as response:
        response_data = response.json()
        rows = [value for key,value in (response_data['personal']['random_names'].items())]
        df.append(rows)
        df1 = pd.DataFrame(df, columns=["A", "B","C", "D","E", "F","G", "H"])
        results = pd.concat([results, df1])
        print(results.shape)
        df1.to_csv(f'C:/myapi/{pd.to_datetime("now", utc=True).date()}_json_parse_results.csv', index=False) 

print("Running threaded:")
threaded_start = time.time()
# for i in range(10):
#     ans = requests.get(personal_url, timeout=TIMEOUT,headers=headers).json()
#     # print(ans['personal']['random_names'])
#     data = ans['personal']['random_names']
#     df = pd.DataFrame.from_dict([data])
#     results = pd.concat([results,df])
#     # print(results.shape)
# results.to_csv(f'C:/myapi/{pd.to_datetime("now", utc=True).date()}_xml_parse_results.csv', index=False) 
# print("Threaded time:", time.time() - threaded_start)

@timer(1,1)
def main():
  with ThreadPoolExecutor(max_workers=15) as executor:
        with requests.Session() as session:
        # with requests.Session.post(url=url_post,headers=headers_post) as session:
            executor.map(fetch, [session] * CONNECTIONS, [personal_url] * CONNECTIONS)
            executor.shutdown(wait=True)


# for i in range(10):
#  print(fetch(requests.Session(), personal_url))
print("Threaded time:", time.time() - threaded_start)