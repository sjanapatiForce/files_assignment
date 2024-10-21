import json_file


def list_universities_by_state(data,state_name):
    
    universities_in_state = [rec['university']['name'] for rec in data if rec['university']['state'] == state_name]
    if universities_in_state:
        print(f"Universities in {state_name}:")
        for uni in universities_in_state:
            print(uni)
    else:
        print(f"No universities found in {state_name}")
        
state_name= input('Enter the state name : ').title()        
list_of_university=list_universities_by_state(json_file.data,state_name)