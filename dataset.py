from faker import Faker
import random
import os
import csv

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
desktop=desktop.replace("\\", "\\\\")
head=['First Name','Last Name','Gender','Reg No','Marks','Email','Password','Medical Issue','Duration','Age','Admission Date','Date of Birth','Course','Address']
data=Faker()
firstN=[]
lastN=[]
age=[]
course=[]
address=[]
admissionD=[]
regno=[]
dob=[]
email=[]

gender=[]
password=[]
duration=[]
marks=[]
mediissue=[]
allmediissue=['HeadAche','Bullying','Prolonged Periods','Anxiety','Depression','Skin Disease','Astama','Stress','Body Shaming','Social Anxiety']

allcourses=['Introduction to C++','Maths','Python Programming','Object oriented Programming','Data Structures','Mechanics-1','Electromagnetism-1','Nuclear Physics']
dura=['2Y','3Y','4Y','5Y','4.5Y','4.5Y']
allgen=['Female','Male', 'Other']
print("Please wait Generating Data...")
for x in range(1000):
    a = random.randint(16, 24)
    age.append(str(a))
    email.append(data.email())
    fn=data.first_name()
    firstN.append(fn)
    lastN.append(data.last_name())
    c = random.randint(0, 7)
    gx = random.randint(0, 2)

    m = random.randint(10, 100)
    da = random.randint(0, 5)
    mi = random.randint(0, 9)
    mediissue.append(allmediissue[mi])
    course.append(allcourses[c])
    gender.append(allgen[gx])
    password.append(data.password())
    duration.append(dura[da])
    marks.append((str(m)))

    address.append(data.address())
    dob.append(str(data.date_between_dates(date_start="-23y", date_end="-19y")))
    regno.append(str(fn)+str(data.random_digit())+str(data.random_letter())+str(data.random_digit())+str(data.random_digit()))
    admissionD.append(str(data.date_between_dates(date_start="-4y", date_end="-1y")))

print("\n\t*** DATASET GENERATED SUCESSFULLY ***")

with open(desktop+'\\\\GeneratedDataset.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(head)
    for xa in range(1000):
        writer.writerow([firstN[xa],lastN[xa],gender[xa],regno[xa],marks[xa],email[xa],password[xa],mediissue[xa],duration[xa],age[xa],admissionD[xa],dob[xa],course[xa],address[xa]])


