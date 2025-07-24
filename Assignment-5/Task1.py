dict={'Alice':85,'Joe':89,'Peter':74,'Henry':96,'Hetwik':92}
key=input("Enter the student's name: ")
if key in dict:
    print("{}'s marks: {}".format(key,dict[key]) )
else:
    print("Student not found.")