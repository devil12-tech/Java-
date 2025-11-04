import sys 
if len(sys.argv) == 3:
  script_name = sys.argv[0]
  name = sys.arv[1]
  rollno = sys.argv[2]
  print("User Provided input values")
else: 
   script_name =sys.argv[0]
   name = "Nikhil"
   rollno = "004"
   print9"User didn't provide any input")

pint("Script Name:",script_name)
print("Student Name: ",name)
print("Roll Number:", rollno)
