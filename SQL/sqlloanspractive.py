import sqlite3

connection = sqlite3.connect('loans.db')
def create_table():
    connection.execute('CREATE TABLE Borrower(ID INTEGER PRIMARY KEY, Name TEXT NOT NULL)')
    connection.execute('CREATE TABLE Book(ID INTEGER PRIMARY KEY, Title TEXT NOT NULL)')
    connection.execute('''CREATE TABLE Loan(ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                            BorrowerID INTEGER NOT NULL,
                                            BookID INTEGER NOT NULL,
                                            FOREIGN KEY(BorrowerID) REFERENCES Borrower(ID),
                                            FOREIGN KEY(BookID) REFERENCES Book(ID))''')
    connection.commit()

def checkborrower():
    cursor = connection.execute('SELECT ID FROM Borrower')
    exist = False
    for row in cursor:
        if row[0] == borrowerID:
            exist = True
            break
    if exist == False:
        print('Borrower not found')
        name = input('Enter your name to be added')
        connection.execute('INSERT INTO Borrower(ID, Name) VALUES(?,?)', (borrowerID, name))
        connection.commit()
        print('You have been added.')

def checkbook():
    cursor = connection.execute('SELECT ID FROM Book')
    exist = False
    for row in cursor:
        if row[0] == bookID:
            exist = True
            break
    if exist == False:
        print('Book Not found')
        title = input('Enter title of book')
        connection.execute('INSERT INTO Book(ID, Title) VALUES(?,?)', (bookID, title))
        connection.commit()
        print('Book inserted')
while True:
    try:
        borrowerID = int(input('Enter your ID'))
    except:
        print('Invalid ID')
        continue
    checkborrower()
    try:
        bookID = int(input('Enter Book id'))
    except:
        print('Invalid book ID, please try again')
        continue
    checkbook()
    cursor = connection.execute('SELECT ID, BorrowerID, BookID FROM Loan')
    onloan = False
    for row in cursor:
        if row[2] == bookID:
            onloan = True
            break
    if onloan == False:
        print('-')
        connection.execute('INSERT INTO Loan(BorrowerID, BookID) VALUES(?,?)', (borrowerID, bookID))
        connection.commit()
        print('Book is now on loan')
    else:
        print('ERROR, book is already on loan')

    connection.row_factory = sqlite3.Row
    show = connection.execute('SELECT ID, BorrowerID, BookID FROM Loan')
   #rows = show.fetchall()
    for row in show:
        print(row['ID'])
    if input('Quit? (Y/N)').upper() == 'Y':
        break
connection.close()