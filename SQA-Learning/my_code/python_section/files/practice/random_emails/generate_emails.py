import random
import string
list_of_domains = ['superqa.com', 'gmail.com', 'yahoo.com', 'outlook.com', 'msn.com']
length_of_email = 10 #each email has 20 characters
letters = string.ascii_lowercase
output_path = 'out_generate_random_email_with_list_of_domains.csv'

#Generate a random emails and store in the list
all_emails = []
for domain in list_of_domains:
    for j in range(20):
        random_string = ''.join(random.choice(letters) for i in range(length_of_email))
        email = f'{random_string}@{domain}'
        all_emails.append(email)
# print(all_emails)

#Take the list and write to file
with open(output_path, 'w') as f:
    for email in all_emails:
        f.write(email)
        f.write(',\n')


    # all_emails_str = ',\n'.join(all_emails)
    # f.write(all_emails_str)