import json_file
import csv

def csv_01(data, university_data):
    with open(university_data, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['University ID', 'Name', 'City', 'State', 'Zip', 'Website'])
        for record in data:
            university = record.get('university',{})
            writer.writerow([university.get('id','N/A'), university.get('name','N/A'), university.get('city','N/A'), university.get('state','N/A'), university.get('zip','N/A'), university.get('website','N/A')])
    return writer    

csv_01(json_file.data,'university_data.csv')