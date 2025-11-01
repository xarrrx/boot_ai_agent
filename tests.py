from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

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


'''print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))'''

print("Test 1: expect instuctions: ")
print(run_python_file("calculator", "main.py"))
print("Test 2: expect calculation of 3+5")
print(run_python_file("calculator", "main.py", ["3 + 5"]))
print("Test 3: expect execution of calculator tests")
print(run_python_file("calculator", "tests.py"))
print("Test 4: expect out of bound error")
print(run_python_file("calculator", "../main.py"))
print("Test 5: expect file not found error")
print(run_python_file("calculator", "nonexistent.py"))
print("Test 6: expect not executable file error")
print(run_python_file("calculator", "lorem.txt"))