# capitals = {"USA": "WashingtonDc", "France": "Paris", "Turkey": "Ankara"}
# print(type(capitals))
#
# france_capital = capitals["France"]
# print(france_capital)
#
# france_capital_2 = capitals.get("France")
# print(france_capital_2)
#
# # ethiopia_capital = capitals['Ethiopia']
# # print(ethiopia_capital)
#
# ethiopia_capital = capitals.get('Ethiopia', "NOT Exist")
# print(ethiopia_capital)
#
# capitals['kenya'] = 'Nairobia'
# print(capitals)
#
# capitals.update({"India": "New Dely"})
# print(capitals)
#
# capitals.update({"India": "New Dely"})
# print(capitals)
#
# all_keys = capitals.keys()
# all_values = capitals.values()
# print(all_keys)
# print(all_values)

employee = {"name": "John Doe",
            "age": 25,
            "phone": 123234986,
            "title": "Software Engineer",
            "skills": ["AWS", "Python", "Java", "Docker"]
            }

e_name = employee['name']
e_age = employee['age']
e_skils = employee['skills']
print(type(e_skils))
user_skill_count = len(e_skils)
print(f"User has {user_skill_count} skills")