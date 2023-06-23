# def get_count_of_small_world(input_sting, max_size=3):
#
#     small_worlds = []
#     for word in input_sting.split():
#         if len(word) <= max_size:
#             small_worlds.append(word)
#     return len(small_worlds)
#
#
#
# _string = 'In Python hashtags are used to tell the computer a line is not worth reading. Much like social media.'
#
# num_small = get_count_of_small_world(_string, max_size=3)
# print(num_small)

def connect_to_database(host='test.db.com', username='testuser', password='testpass'):
    print(f'Connection to host: {host}')
    print(f'Username: {username}')


connect_to_database()




