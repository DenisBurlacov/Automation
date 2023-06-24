import pdb
sample_file_path = './sample_files/programming_language_wikipedia.txt'
with open(sample_file_path, 'r') as f:
    content = f.read()
print(content)

country_file = './sample_files/list_of_countries_with_no_comma.txt'
with open(country_file, 'r') as r:
    country = r.read()
print(country)

pdb.set_trace()

