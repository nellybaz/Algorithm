import sys

data = sys.stdin.readlines()
email = data[0]
phone1 = data[1]
phone2 = data[2]

#email masking
email_right_end = email[email.index('@')-1:]
email_left_end = email[2]
masked_mail = email_left_end+'*****'+email_right_end

#phone without countyr code masking

phone_right_end = phone1[-5:]
masked_phone_without_country_code = 'P:***-***-'+phone_right_end


#phone with country code
phone2_country_code, phone2_other_digit = phone2.split('(')
phone2_country_code = phone2_country_code[3:]
phone2_right = phone2_other_digit[-4:]

masked_country_code = ''
for digit in phone2_country_code:
    masked_country_code += '*'
    
masked_phone2 = 'P:+'+ masked_country_code + '-***-***-' 

sys.stdout.write(masked_mail)
sys.stdout.write(masked_phone_without_country_code)


sys.stdout.write(masked_phone2)
