import sqlite3

connection = sqlite3.connect('library.db')
#connection.execute('CREATE TABLE Book (ID INTEGER PRIMARY KEY, Title TEXT)')

def insertrandom():
    for i in range(10):
        connection.execute('INSERT INTO Book (ID, Title) VALUES(?, ?)',(str(i), f'EXAMPLE book {i}'))
    connection.commit()

#connection.execute('DELETE FROM Book WHERE ID > ? AND ID < ?', (2,4))

def deleteallwhere():
    book_id = '1 or 1'
    connection.execute('DELETE FROM Book WHERE ID = ' + book_id)
    #connection.rollback()
    connection.commit()

def deleteall():
    connection.execute('DELETE FROM book')
    connection.commit()

def showtitle():
    cursor = connection.execute('SELECT ID, Title FROM Book')
    for row in cursor:
        print(row[1])

def deleteid():
    book_id = input('Enter book id to be deleted')
    connection.execute('DELETE FROM Book where ID = ?', (book_id))
    connection.commit()

def insert():
    while True:
        try:
            book_id = int(input('Enter a book id to be INserted'))
        except:
            print('Not a valid id')
            continue
        title = input('Enter name of new book')
        try:
            connection.execute('INSERT INTO Book(ID, Title) VALUES(?,?)', (book_id, title))
            connection.commit()
        except:
            print('DATABASE ERROR (e.g duplicated id)')
            continue
        print('insertion successful')
        if input('CONTINUE? (Y/N)').upper() == 'Y':
            continue
        else:
            break
#delete()
#deleteallwhere()
#insertrandom()
#insert()
#deleteall()
showtitle()
#connection.commit()
connection.close()
