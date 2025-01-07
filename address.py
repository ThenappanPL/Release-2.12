import requests
import xml.etree.ElementTree as ET
import random

def get_uk_address():
  ps_code = ['a*','b*','c*','d*','e*','f*','g*','h*','i*','j*','k*','l*','m*','n*','o*','p*','q*','r*','s*','t*','u*','v*','w*','x*','y*','z*' ]
  # ps_code = ['PO15*']
  # ps_code = ['SY23 2AR']
  ps_format1 = random.choice(ps_code)
  url = 'https://osbpre.co.ad.specsavers.com/savs/validateaddress/search/v1?maxresults=100&countryiso=GBR&postcode=' + str(ps_format1) + '&street=[a-z]'
  headers = {'Content-Type': 'application/xml;charset=utf-8'}

  response = requests.request("GET", url, headers=headers).text
  root = ET.fromstring(response)

  company = list([(elem.text) for elem in root.iter() if (elem.tag == 'company')])
  if (company != []):
    company = random.choice(company)
  print(company)
  subbuilding = list([(elem.text) for elem in root.iter() if (elem.tag == 'subBuilding')])
  if (subbuilding != []):
    subbuilding = random.choice(subbuilding)
  print(subbuilding)
  building = list([(elem.text) for elem in root.iter() if (elem.tag == 'building')])
  if (building != []):
    building = random.choice(building)
  print(building)
  premise = list([(elem.text) for elem in root.iter() if (elem.tag == 'premise')])
  if (premise != []):
    premise = random.choice(premise)
  print(premise)
  street = list([(elem.text) for elem in root.iter() if (elem.tag == 'street')])
  if (street != []):
    street = random.choice(street)
  print(street)
  poBox = list([(elem.text) for elem in root.iter() if (elem.tag == 'poBox')])
  if (poBox != []):
    poBox = random.choice(poBox)
  print(poBox)
  cedex = list([(elem.text) for elem in root.iter() if (elem.tag == 'cedex') ])
  if (cedex != []):
    cedex = random.choice(cedex)
  print(cedex)
  substreet = list([(elem.text) for elem in root.iter() if (elem.tag == 'subStreet')])
  if (substreet != []):
    substreet = random.choice(substreet)
  # substreet = random.choice(list([(elem.text) if (elem.tag == 'subStreet') else None for elem in root.iter()]))
  print(substreet)
  subcity = list([(elem.text) for elem in root.iter() if (elem.tag == 'subCity')])
  if (subcity != []):
    subcity = random.choice(subcity)
  print(subcity)
  city = list([(elem.text)  for elem in root.iter() if (elem.tag == 'city')])
  if (city != []):
    city = random.choice(city)
  print(city)
  postcode = random.choice(list([(elem.text) for elem in root.iter() if (elem.tag == 'postcode')]))
  print(postcode)
  country = random.choice(list([(elem.text) for elem in root.iter() if (elem.tag == 'country')]))
  city = str(city)
  postcode = str(postcode)
  country = str(country)
  if((company == None or building == None) and subcity == None and subbuilding == None):
    addressline1 = str(premise) + ' ' + str(street)
    print(addressline1,city,postcode,country)
    return {"addressline1":addressline1,"city":city,"postcode":postcode,"country": country}
  elif(subcity != None and substreet == None and subbuilding == None):
    addressline1 = str(premise) + ' ' + str(street)
    addressline2 = str(subcity)
    print(addressline1,addressline2,city,postcode,country)
    return {"addressline1":addressline1,"addressline2":addressline2,"city":city,"postcode":postcode,"country": country}
  elif(premise != None and subbuilding != None and street != None ):
    addressline1 = (str(subbuilding) + ' ' + str(premise) + ' ' + str(street))
    print(addressline1,city,postcode,country)
    return {"addressline1":addressline1,"city":city,"postcode":postcode,"country": country}
  elif(building !=  None and subbuilding != None and subcity != None and substreet == None):
    addressline1 = (str(subbuilding) + ' ' + str(building))
    addressline2 = str(subcity)
    print(addressline1,city,postcode,country)
    return {"addressline1":addressline1,"addressline2":addressline2,"city":city,"postcode":postcode,"country": country}
  elif(substreet != None and subcity != None):
    addressline1 = ((str(subbuilding) or str(premise)) + ' ' + (str(building) or str(street)))
    addressline2 = str(substreet)
    addressline3 = str(subcity)
    print(addressline1,city,postcode,country)
    return {"addressline1":addressline1,"addressline2":addressline2,"addressline3":addressline3,"city":city,"postcode":postcode,"country": country}
  elif((company != None or building != None) or poBox !=  None and city != None):
    addressline1 = (str(company) or str(building))
    addressline2 = (str(poBox))
    # more_addressline1 = (str(subbuilding) + ' ' + str(building) + ' ' +  str(premise) + ' ' + str(street))
    print(addressline1,addressline2,city,postcode,country)
    return {"addressline1":addressline1,"addressline2":addressline2,"city":city,"postcode":postcode,"country": country}

def main():
    uk_address()

if __name__ == "__main__":
    main()