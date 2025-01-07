# from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
from fastapi.responses import PlainTextResponse
import requests
import time
import random

headers = {'Content-Type': 'application/json','x-api-key': '7ah5W8NQ.228oD7coJ9j8oh8LWMgNZy-m9vsVvfcey'}
suppression_request ='CRN|EPOS_NUMBER|COMMUNICATION_ADDRESS|CLEANSE_CODE|CLEANSE_DATE\n'
out = {}
urls = []
CONNECTIONS = 50
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
  suppression_request1 = [f"""{out['random_numbers']['ExternalId']}|{out['specsaver_store']['uk_store_no']}|{out['contrywise_random_phoneno']['uk_mobile_number']}|{random.choice(['S0','S1','S2','S3'])}|{out['personal']['random_dates']['dob_format1']}"""]
  combined_request = '\n'.join(suppression_request1)
  print("Threaded time:", time.time() - threaded_start)
  return (PlainTextResponse(content=(suppression_request+combined_request)))

def main():
    ggg_test()


if __name__ == "__main__":
    main()