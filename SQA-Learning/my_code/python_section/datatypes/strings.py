abc = 'Some sting'
print(abc.upper())
print(abc.lower())
print(abc.strip())
print(abc.split())
print(abc.count('s'))
print(len(abc))
print(abc.casefold())


full_name = 'Denis Burlakov'
name_s = full_name.split()
print(name_s)

ssn = '123-12-1233'

ssn_s = ssn.split(ssn[0])
print(ssn_s)

full_name = 'Den burlakov.'
print(full_name)
full_name_s = full_name.strip('.')
print(full_name_s)

url = 'https://supr.com/'
is_url = url.endswith('.com/')
print(is_url)
is_absolute = url.startswith('https://')
print(is_absolute)
info = 'This%20is%20url%20encoded'
clear_info = info.replace('%20', ' ')
print(clear_info)