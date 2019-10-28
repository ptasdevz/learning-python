import os
import pathlib

# try:
#     os.makedirs("test",0o755, True)
# except OSError as e:
#     print(e)

pathlib.Path('test/look/in/here').mkdir(parents=True, exist_ok=True)


employee_handle = open("test/employee1.txt", "a+")
# print(employee_handle.readable())
# print(employee_handle.read())
employee_handle.write("mandy - tester1\n")
employee_handle.close()