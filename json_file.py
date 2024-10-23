import json
import os

def load_json_file():
    folder_name=input('Enter folder name where JSON file is located: ')
    file_name = 'srihari_janapati_adoptions.json'
    pathway = os.path.join(folder_name,file_name)
    try:
        with open(pathway, 'r') as file:
            data = json.load(file)
            print('file loaded succesfully')
        return data    
    except FileNotFoundError as fnf_error:
        print(f'file{pathway} not found')
    except json.JSONDecodeError as json_error:
        print(f"Error decoding JSON: {json_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
data = load_json_file()
#print(data[10])