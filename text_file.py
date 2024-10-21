import json_file

def books_category(data, category, textfile):
    with open(textfile, 'w') as file:
        file.write(f"Books in the {category} category:\n")
        for record in data:
            adoptions = record.get('adoptions', [])
            for adoption in adoptions:
                book = adoption.get('book', {})
                if book.get('category') == category:
                    file.write(f"{book['title']}\n")

category=input('Enter category: ').title()
textfile=input('Enter textfile name you would like to assign: ')
books_category(json_file.data, category,textfile)