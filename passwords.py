import secrets
import uuid
import random
import string

def get_random_token():
  return(secrets.token_hex(32))

def get_random_id():
   return(uuid.uuid4())

def get_random_password():
    random_source = string.ascii_letters + string.digits + string.punctuation
    # select 1 lowercase
    password = random.choice(string.ascii_lowercase)
    # select 1 uppercase
    password += random.choice(string.ascii_uppercase)
    # select 1 digit
    password += random.choice(string.digits)
    # select 1 special symbol
    password += random.choice(string.punctuation)

    # generate other characters
    for i in range(6):
        password += random.choice(random_source)

    password_list = list(password)
    # shuffle all characters
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    return password

def get_random_secure_password():
    password = ''.join((secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(8)))
    return(password)

import random
import string

def get_string(letters_count, digits_count):
    letters = ''.join((random.choice(string.ascii_letters) for i in range(letters_count)))
    digits = ''.join((random.choice(string.digits) for i in range(digits_count)))

    # Convert resultant string to list and shuffle it to mix letters and digits
    sample_list = list(letters + digits)
    random.shuffle(sample_list)
    # convert list to string
    final_string = ''.join(sample_list)
    return(final_string)

def get_random_numbers():
    num1 = 221 * random.randint(1000, 12999)
    num2 = 632 * random.randrange(2900, 32000)
    num3 = 321 * random.randint(4900, 52000)
    num4 = 421 * random.randint(5900, 62000)
    num5 = 521 * random.randint(6900, 72000)
    singed_int = random.randrange(-60, -1)
    float_neg = round(random.uniform(-10.99, -0.01), 1)
    float_post = round(random.uniform(10.99, 0.01), 1)
    return{"ExternalId" :num1,"ECommExtID" :num2,"MCommExtID" :num3,"HCommExtID" :num4,"WCommExtID":num5, "negative" :singed_int, "decimal_negative" :float_neg,"decimal_pstive": float_post}