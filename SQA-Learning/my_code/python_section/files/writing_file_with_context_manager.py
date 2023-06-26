my_string = 'I love to programe in Python language'
# with open('./sample_files/sample_output2.txt', 'w') as my_f:
#     my_f.write(my_string)

my_l = ['user_1', 'user_2', 'User_3']
with open('./sample_files/sample_output2.txt', 'w') as my_f:
    for i in my_l:
        my_f.write(i + '\n')

#appending

var2 = "Also love testing"
with open("./sample_files/sample_output2.txt", 'a') as f:
    f.write('\n')
    f.write(var2)


my_langs = ['Python', 'Java', 'Js', 'PHP', 'Ruby']
with open('./sample_files/my_fav_languages.csv', 'w') as f:
    str_my_langs = '\n'.join(my_langs)
    f.writelines(my_langs)