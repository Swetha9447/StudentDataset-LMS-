from faker import Faker
import random
import os
import csv

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
desktop=desktop.replace("\\", "\\\\")
head=['First Name','Last Name','Email','Age','Admission Date','Date of Birth','Reg No','Course','Address']
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
allcourses=['BE. Computer Science','BE. Mechanical Engineering','BE. Petrochemical Engineering','BE. Mechatronics Engineering','BE. Electronics and Communications Engineering','BE. Electrical and Electronics Engineering','BSc. Computer Science','Bachelors in computer application', 'BSc. Maths', 'BSc. Physics']
print("Please wait Generating Data...")
for x in range(1000):
    a = random.randint(16, 24)
    age.append(str(a))
    email.append(data.email())
    firstN.append(data.first_name())
    lastN.append(data.last_name())
    c = random.randint(0, 7)
    course.append(allcourses[c])
    address.append(data.address())
    dob.append(str(data.date_between_dates(date_start="-23y", date_end="-19y")))
    regno.append(str(data.random_letter())+str(data.random_letter())+str(data.random_letter())+str(data.random_digit())+str(data.random_digit()))
    admissionD.append(str(data.date_between_dates(date_start="-4y", date_end="-1y")))

print("\n\t*** DATASET GENERATED SUCESSFULLY ***")

with open(desktop+'\\\\GeneratedDataset.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(head)
    for xa in range(1000):
        writer.writerow([firstN[xa],lastN[xa],email[xa],age[xa],admissionD[xa],dob[xa],regno[xa],course[xa],address[xa]])

print("____________________________________________\n")
print("\t*** CSV FILE CREATED ON DESKTOP (generatedDataset.csv) ***")
