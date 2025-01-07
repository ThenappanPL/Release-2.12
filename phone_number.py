import random
import string

def uk_mobile_no():
   uk_mobileno_prefix_list = ['+44738','0740','0044745','0753','779','0773','774','+44776','0781','0785','0795','797']
   uk_start_mobile = random.choice(uk_mobileno_prefix_list)
   uk_mobile_number = (uk_start_mobile + str(random.randrange(1000000,9999999, 2)))
   print(uk_mobile_number)
   return uk_mobile_number

def uk_homephone():
   uk_homephoneno_prefix_list = ['020','023','024','011','+4411','011','012','013','015','016','019']
   uk_homephoneno = random.choice(uk_homephoneno_prefix_list)
   uk_homephone_number = (uk_homephoneno + str(random.randrange(1000000000,9999999999, 2)))
   return uk_homephone_number

def nl_mobile_no():
   nl_mobileno_prefix_list = ['061','062','063','064','065','+3161','+3162','+3163','+3164','+3165','003161','003162','003163','003164','003165']
   nl_start_mobile = random.choice(nl_mobileno_prefix_list)
   nl_mobile_number = (nl_start_mobile + str(random.randrange(1000000,9999999, 2)))
   print(nl_mobile_number)
   return nl_mobile_number

def nl_homephone():
   nl_homephoneno_prefix_list = ['072','053','024','036','+3138','0318','053','050','045','058','071','043','024','010','013','075','079']
   nl_homephoneno = random.choice(nl_homephoneno_prefix_list)
   nl_homephone_number = (nl_homephoneno + str(random.randrange(100000000,999999999, 2)))
   print(nl_homephone_number)
   return nl_homephone_number

def ie_mobile_no():
   ie_mobileno_prefix_list = ['35383','083','0035387','085','086','087','089','+35389','083','089','087','086']
   ie_start_mobile = random.choice(ie_mobileno_prefix_list)
   ie_mobile_number = (ie_start_mobile + str(random.randrange(1000000,9999999, 2)))
   print(ie_mobile_number)
   return ie_mobile_number

def ie_homephone():
   ie_homephoneno_prefix_list = ['022','023','024','025','026','042','043','044','045','046','047','051','049','052','053']
   ie_homephoneno = random.choice(ie_homephoneno_prefix_list)
   ie_homephone_number = (ie_homephoneno + str(random.randrange(200000000,999999999, 2)))
   print(ie_homephone_number)
   return ie_homephone_number

def esp_mobile_no():
   es_mobileno_prefix_list = ['03461','+3461','+3462','+3463','+3464','+3465','+3466','+3467','+3468','+3469','003461','003462','003463','003464','003465']
   es_start_mobile = random.choice(es_mobileno_prefix_list)
   es_mobile_number = (es_start_mobile + str(random.randrange(1000000,9999999, 2)))
   print(es_mobile_number)
   return es_mobile_number

def esp_homephone():
   es_homephoneno_prefix_list = ['34911','34912','34913','34914','34915','34916','34917','34918','34931','34938','34944','34954','34955','34960','34961','34962','34963']
   es_homephoneno = random.choice(es_homephoneno_prefix_list)
   es_homephone_number = (es_homephoneno + str(random.randrange(100000,999999, 2)))
   print(es_homephone_number)
   return es_homephone_number

def email_address(length):
    email_suffix = ['@gmail.com','@gmail.co.uk','@hotmail.co.uk','@hotmail.com','@aol.com','@aol.co.uk','@yahoo.com','@yahoo.co.uk','@specsavers.com']
    email_suffix_randomemail = random.choice(email_suffix)
    source = string.digits
    last_name_digit = ''.join((random.choice(source) for i in range(3)))
    first_name = ''.join(random.choice(string.ascii_letters) for i in range(length))
    last_name = ''.join(random.choice(string.ascii_letters) for i in range(length))
    return {"email_random_format1" : first_name + '.' + last_name + email_suffix_randomemail, "email_random_format2" : first_name + '.' + last_name + last_name_digit + email_suffix_randomemail}

def random_identifier():
    ref_type = ['Passport','SSN','National Identifier','Birth Number','NHS Number']
    ref_type = random.choice(ref_type)
    letters = string.ascii_uppercase
    ref_value_1 = ''.join((random.choice(letters) for i in range(3)))
    numerics = string.digits
    ref_value_2 = ''.join((random.choice(numerics) for i in range(10)))
    return {"ref_type" : ref_type, "ref_value" : ref_value_1 + ref_value_2}

def main():
    uk_mobile_no()
    uk_homephone()
    nl_mobile_no()
    nl_homephone()
    ie_mobile_no()
    ie_homephone()
    esp_mobile_no()
    esp_homephone()
    email_address()

if __name__ == "__main__":
    main()