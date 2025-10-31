from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

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

'''print("test1:")
print(get_file_content("calculator", "main.py"))
print("test2:")
print(get_file_content("calculator", "pkg/calculator.py"))
print("test3:")
print(get_file_content("calculator", "/bin/cat"))
print("test4:")
print(get_file_content("calculator", "pkg/does_not_exist.py"))'''



'''write_file("write_test", "writetest.py", "content")
write_file("write_test2", "testdir/writetest.py", "content")
write_file("write_test2", "writetest.py", "content")'''


print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))