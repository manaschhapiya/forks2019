'''

Code Challenge 2
Perform similar steps as in the above code challenge but store the contents in 
an online mongo atlas database.


'''


import pymongo


client = pymongo.MongoClient("mongodb://manaschhapiya:manas%40123@cluster0-shard-00-00-v8npm.mongodb.net:27017,cluster0-shard-00-01-v8npm.mongodb.net:27017,cluster0-shard-00-02-v8npm.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
db = client.employee
def addstudent(name, age, rollno,branch):
    #unique_employee = mydb.employees.find_one({"id":idd})
    #if unique_employee:
    #    return "Employee already exists"
    #else:
    db.employees.insert_one(
            {
            "Student_Name" : name,
            "Student_Aget" : age,
            "Student_Roll_no" : rollno,
            "Student_Branch" : branch
            })
    return "Employee added successfully"


def fetch_all_student():
    user = db.employees.find()
    for i in user:
        print (i)




addstudent('manas',20, '12', 'cse')
addstudent('dhruvin',21, '14', 'cs')
addstudent('bhavya',19, '17', 'ee')
addstudent('aayush',20, '128', 'ce')

fetch_all_student()

