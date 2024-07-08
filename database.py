import sqlite3

# create the connection and the cursor to the database
conn = sqlite3.connect('todo.db')
c = conn.cursor()


def add_todo_to_database(attributes):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()

    # push the data to the database
    c.execute('INSERT INTO Todos VALUES (?,?,?,?,?,?,?,?,?,?)', attributes)
    conn.commit()


def clear_database():
    c.execute('DELETE FROM Todos')
    conn.commit()


def load_contacts():
    return c.execute('Select * from Contacts').fetchall()


def add_contact(name):
    c.execute(f'INSERT INTO "Contacts" VALUES ("{name}")')
    conn.commit()


def remove_contact(name):
    c.execute(f' DELETE FROM Contacts WHERE Name = "{name}" ')
    conn.commit()


def load_todos():
    from todo import Todo
    return_list = []

    # select everything from the database
    c.execute('SELECT * FROM Todos')
    n = c.fetchall()

    for _ in n:
        people = []

        # separate the people
        '''m = _[1].split(',')
        for o in m:
            if o[0] == '[':
                if o[-1] == ']':
                    people.append(o[2:-2])
                else:
                    people.append(o[2:-1])
            else:
                if o[-1] == ']':
                    people.append(o[1:-2])
                else:
                    people.append(o[1:-1])'''

        people.append(_[1])
        people.append(_[8])
        people.append(_[9])

        # create a new task and put it into a list
        return_list.append(Todo(_[5], people, _[6], _[2], _[3], _[4], _[0], _[7]))

    # clears the database
    clear_database()

    # return all the tasks in a list
    return return_list
