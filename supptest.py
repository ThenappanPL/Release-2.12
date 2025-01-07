import time
import requests
import concurrent.futures

headers = {'Content-Type': 'application/json','x-api-key': '7ah5W8NQ.228oD7coJ9j8oh8LWMgNZy-m9vsVvfcey'}

def get_wiki_page_existence(random_page_url, timeout=10):
    response = requests.get(url=random_page_url, timeout=timeout,headers=headers).json()
    # store_response = (response.json())
    # print(type(store_response))
    return response
    # return (response.append(json.loads(response.content.decode("utf-8"))))

random_page_urls = [
    "https://tp_spec.deta.dev/api/v1/random_stores",
    "https://tp_spec.deta.dev/api/v1/random_string_numbers",
    "https://tp_spec.deta.dev/api/v1/random_personal",
    "https://tp_spec.deta.dev/api/v1/random_contact",
]

def get_test_pae():
 threaded_start = time.time()
 with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
    futures = []
    results = []
    for url in random_page_urls:
        a = futures.append(executor.submit(get_wiki_page_existence, random_page_url=url))
    for future in concurrent.futures.as_completed(futures):
        results = [future.result()]
        results.append
        return(results,"Threaded time:", time.time() - threaded_start)
# print("Running threaded:")
# threaded_start = time.time()
# print("Threaded time:", time.time() - threaded_start)
     
# def cleanNullTerms(d):
#    clean = {}
#    for k, v in d.items():
#       if isinstance(v, dict):
#          nested = cleanNullTerms(v)
#          if len(nested.keys()) > 0:
#             clean[k] = nested
#       elif v is not None:
#          clean[k] = v
#    return clean    

# print(cleanNullTerms(a_r))
print(get_test_pae())