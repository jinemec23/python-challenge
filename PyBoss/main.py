# Import file
import os
import csv


# Set path
employee_data = os.path.join('Resources','employee_data.csv')


#Set variable lists
employee_list = []
headers = ['Emp ID','First Name','Last Name','DOB','SSN','State']



us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#Set new list

# Use with open to read the file
with open(employee_data, newline="") as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        index = {}
        index['Emp ID']= row['Emp ID']
        first, last = row['Name'].split(" ")
        index['First Name'] = first
        index['Last Name']  = last
        Yr, Mo, Day = row['DOB'].split('-')
        index['DOB']= '/'.join([Mo, Day, Yr])
        ssn_last_four = row['SSN'].split('-')[2]
        ssn = '***-**' + ssn_last_four
        index['SSN'] = ssn
        st = us_state_abbrev[row['State']]
        index['State'] = st
        employee_list.append(index)


#Output file
output_file = os.path.join('Analysis','employee_list.csv')
with open(output_file,"w", newline="") as employee_file:
    writer = csv.DictWriter(employee_file, fieldnames = headers)
    writer.writeheader()
    writer.writerows(employee_list)

#Print and Export Results to txt file
for line in employee_list:
    print(f"{line['Emp ID']}, {line['First Name']}, {line['Last Name']}, \
{line['DOB']}, {line['SSN']}, {line['State']}")