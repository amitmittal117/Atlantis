import csv
import random

records = 1000
print("Making %d records\n" % records)

fieldnames = ['id', 'first_name', 'last_name', 'email', 'Pincode', 'timestamp']
writer = csv.DictWriter(open("data.csv", "w"), fieldnames=fieldnames)

first_names = ['Deepak', 'Sangeeta', 'Geetika', 'Anubhav', 'Sahil', 'Akshay']
last_names = ['Mittal', 'kumar', 'Singh', 'Gupta', 'Bhatt', 'Khan', 'Sharma', 'Jain', 'Shaik']
cities = ['Delhi', 'Kolkata', 'Chennai', 'Mumbai']


def generate_csv():
    writer.writerow(dict(zip(fieldnames, fieldnames)))
    for i in range(1, records):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        writer.writerow(dict([
            ('id', i),
            ('first_name', first_name),
            ('last_name', last_name),
            ('email', str(first_name + '@' + last_name + '.com')),
            ('Pincode', str(random.randint(100001, 999999))),
            ('timestamp',
             str(str(random.randint(0, 24)) + ':' + str(random.randint(0, 59)) + ':' + str(random.randint(0, 59))))]))
