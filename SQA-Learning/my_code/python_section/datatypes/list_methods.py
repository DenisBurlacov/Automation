countries = ['USA', 'Mexico', 'Canada', 'India', 'Germany', 'Japan']
print(type(countries))
no_of_countries = len(countries)
print(no_of_countries)
#adding elements to list
countries.append('China')
print(countries)
last_element_list = countries.pop()
print(last_element_list)
print(countries)
countries.remove('Canada')
print(countries)