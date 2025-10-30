from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

'''try:
    print(get_files_info("calculator", "."))

    print(get_files_info("calculator", "pkg"))

    print(get_files_info("calculator", "/bin"))

    print(get_files_info("calculator", "../"))
except Exception as e:
    print("An error occurred:", e)'''

'''testresultstring = get_file_content("calculator", "lorem.txt")

print(testresultstring)
print(f'length is: {len(testresultstring)}')'''

print("test1:")
print(get_file_content("calculator", "main.py"))
print("test2:")
print(get_file_content("calculator", "pkg/calculator.py"))
print("test3:")
print(get_file_content("calculator", "/bin/cat"))
print("test4:")
print(get_file_content("calculator", "pkg/does_not_exist.py"))