import pdb
sample_file = './sample_files/programming_language_wikipedia.txt'

# my_file = open(sample_file, 'r')
# content = my_file.read()
# my_file.close()
#
# my_content_list = content.split('\n\n')
# print(my_content_list)

#
# content = my_file.readlines()
# my_file.close()
#
# print(content)
my_file = open(sample_file, 'r')
content = my_file.read()
print(content)
my_file.seek(0)
print('--------')
content2 = my_file.read()

print(content2)
print('2---------')
my_file.close()

