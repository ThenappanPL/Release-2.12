from concurrent.futures import ThreadPoolExecutor
import requests

from timer import timer

och_payload_url = 'https://tp_spec.deta.dev/api/v1/och_socrates_payload/ie'
# personal_url = 'https://tp_spec.deta.dev/api/v1/random_personal'
headers = {'Content-Type': 'application/json;charset=utf-8','x-api-key': '7ah5W8NQ.228oD7coJ9j8oh8LWMgNZy-m9vsVvfcey'}
# url_post = "https://osbpre.co.ad.specsavers.com/AudiologyCustomerUpdate/Audiology_PS"
url_post = "https://osbsit.az.specsavers.com/AudiologyCustomerUpdate/Audiology_PS"
headers_post = {'Content-Type': 'text/xml; charset=utf-8','Accept': 'application/xml'}

def post_url(args):
    with requests.get(och_payload_url,headers=headers) as response:
        return(requests.post(args[0],headers=args[1], data=response.text))

# def fetch(session, och_payload_url):
#     with session.get(och_payload_url) as response:
#         print(response.text)

# def main():
#     with ThreadPoolExecutor(max_workers=5) as executor:
#         with requests.Session() as session:
#         # with requests.Session.post(url=url_post,headers=headers_post) as session:
#             executor.map(fetch, [session] * 3, [och_payload_url] * 3)
#             executor.shutdown(wait=True)

# def main():
#   with ThreadPoolExecutor(max_workers=5) as executor:
#      with requests.Session() as session:
#         list_of_urls = [("https://osbpre.co.ad.specsavers.com/AudiologyCustomerUpdate/Audiology_PS",headers)]*10
#         response_list = list(executor.map(fetch(session, och_payload_url),list_of_urls))
#         for response in response_list:
#             print(response)

list_of_urls = [("https://osbsit.az.specsavers.com/AudiologyCustomerUpdate/Audiology_PS",headers_post)]*10
@timer(1, 1)
def main():
  with ThreadPoolExecutor(max_workers=5) as pool:
    with requests.Session():
      response_list = list(pool.map(post_url,list_of_urls))
      for response in response_list:
        print(response)
      pool.shutdown(wait=True)
