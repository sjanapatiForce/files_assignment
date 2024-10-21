import json_file
import csv

def csv_05(data, csv_filename):
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Message ID', 'Date', 'Content', 'Category', 'University ID'])
        for record in data:
            university_id = record.get('university', {}).get('id', 'N/A')
            messages = record.get('messages', [])
            for message in messages:
                writer.writerow([message.get('id', 'N/A'),message.get('date', 'N/A'),message.get('content', 'N/A'),message.get('category', 'N/A'),university_id])


csv_05(json_file.data,'messages.csv')