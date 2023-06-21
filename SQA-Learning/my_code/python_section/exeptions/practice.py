# try:
#     a = 5 / 0
# except:
#     print("Devide by zero")

try:
    a = 5 / 0
    b = {'name', 'foo', 'age', 45}
    x = b['scool']
except (KeyError, ZeroDivisionError):
    print(f"Error has happened:")
