from datetime import datetime
notebook = []

def add_note(notebook):
    note = {"title": input("title:"),
            "note": input("note:"),
            "data": datetime.now()}
    notebook.append(note)
    return notebook

while True:
    command = input("""
chikar konam?
a: append note
end:exit the notebook!
show: show the whole notebook!
""")

    if command == "a":
       notebook = add_note(notebook)
    elif command == "end":
        break
    elif command == "show":
        print(notebook)