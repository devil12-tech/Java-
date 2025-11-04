import sys

if len(sys.argv) == 3:
    script_name = sys.argv[0]
    name = sys.argv[1]
    rollno = sys.argv[2]
    print("User Provided input values")
else:
    script_name = sys.argv[0]
    name = "Nikhil"
    rollno = "004"
    print("User didn't provide any input")

print("Script Name:", script_name)
print("Student Name:", name)
print("Roll Number:", rollno)
