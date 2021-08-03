import pymongo as py

class client:
    def __init__(self): # connect to server and link to student collection
        print("Connecting to server...")
        self.client = py.MongoClient("127.0.0.1", 27017)
        self.db = self.client.get_database("20s24")
        self.col = self.db.get_collection("student")

    def close(self): # disconnect from server
        print("Disconnecting from server...")
        self.client.close()
        
    def open(self): # Reconnect and link to student collection
        self.client = py.MongoClient("127.0.0.1", 27017)
        self.db = self.client.get_database("20s24")
        self.col = self.db.get_collection("student")
        
    def clearDB(self,dbname): # Clear Database
        self.client.drop_database(dbname)
        print("cleared DB")

    def checkID(self, _id): # Check ID in Database
        result = self.col.find()
        for doc in result:
            if doc.get("_id") == _id:
                return True      
        return False

    def insertDoc(self, textfile): # Insert Documents from a text file
        print("Running insertDoc(self, textfile)")
        file = open(textfile, 'r')
        lines = file.readlines()
        for idx in range(1, len(lines)):
            line = lines[idx].strip().split(',')
            hobbies = line[4:]
            if self.checkID(int(line[0])) == False:
                self.col.insert_one({"_id": int(line[0]),
                                "name" : line[1],
                                "class" : line[2],
                                "age": int(line[3]),
                                "hobbies": hobbies})
                print(f"{line[1]} added to students")
        file.close()
        print()

    def findUserByName(self, inName): # Get Users with input name
        print("Running findUserByName(self, inName)")
        result = self.col.find({"name":inName})
        count = 0
        print("{:^4}|{:^16}|{:^5}|{:^7}".format("ID",'Name','Age','Class'))
        for item in result:
            count += 1
            print("{:^4}|{:^16}|{:^5}|{:^7}".format(item.get("_id"),
                                                    item.get("name"),
                                                    item.get("age"),
                                                    item.get("class")))
        print(f"\n Total number of students found: {count}\n")

    def getUsersByAge(self, age): # Get users by Age
        print("Running  getUsersByAge(self, age)")
        query = {"age":{"$gte": age}}
        result = self.col.find(query)

        # print("List of documents found:")
        # print("{:^16}|{:^5}|{:^35}".format("Name", "Age", "Hobbies"))
        # for item in result:
        #     print("{:^16}|{:^5}|{:^35}".format(item.get("name"),
        #                                             item.get("age"),
        #                                             str(item.get("hobbies"))))
        # print()

        projection = {'name': 1, 'age': 1, 'hobbies': 1}
        print("Calling dynamicDisplay(projection, result)")
        self.dynamicDisplay(projection, result)

    def returnUserByAgeRange(self): # Get users based on a specified age range
        print("Running returnUserByAgeRange(self)")
        getAgeMin = int(input("Min age of student: "))
        getAgeMax = int(input("Max age of student: "))
        cond1 = {"age":{"$gt": getAgeMin}}
        cond2 = {"age":{"$lt": getAgeMax}}
        query = {"$and":[cond1,cond2]}
        result = self.col.find(query)

        # print("List of documents found:")
        # print("{:^16}|{:^5}|{:^35}".format("Name", "Age", "Hobbies"))
        # for item in result:
        #     print("{:^16}|{:^5}|{:^35}".format(item.get("name"),
        #                                             item.get("age"),
        #                                             str(item.get("hobbies"))))
        # print()

        projection = {'name': 1, 'age': 1, 'hobbies': 1}
        print("Calling dynamicDisplay(projection, result)")
        self.dynamicDisplay(projection, result)

    def getUserByHobby(self): # Get users by their hobby
        print("Running getUserByHobby(self)")
        hobby = input("Enter hobby: ")
        query = {'hobbies':{"$in":[hobby]}}
        result = self.col.find(query)

        # print("List of documents found:")
        # print("{:^4}|{:^16}|{:^5}|{:^7}".format("ID",'Name','Age','Class'))
        # for item in result:
        #     print("{:^4}|{:^16}|{:^5}|{:^7}".format(item.get("_id"),
        #                                             item.get("name"),
        #                                             item.get("age"),
        #                                             item.get("class")))
        # print()

        projection = {'name':1,'class':1,'age':1}
        print("Calling dynamicDisplay(projection, result)")
        self.dynamicDisplay(projection, result)

    def dynamicDisplay(self, projection, results):
        fieldlength = {'_id':4,'name':16, 'age':6, 'class':8, 'hobbies': 34}  # length specification for each field
        header = '|'
        for field in projection:   # Creates the header with the fields from the projection
            header = header + f'{" "*(fieldlength[field]//2)}{field}{" "*(fieldlength[field]//2)}|'
        print(header)
        for item in results:
            document = '|'
            for field in projection:   # Creates the row with data arranged nicely
                length = (len(str(item.get(field))) - len(field)) // 2  # code to format data nicely
                right = " "* ((fieldlength[field]//2) - length)
                if (len(str(item.get(field))) - len(field)) % 2 == 0:
                    left = " " * ((fieldlength[field] // 2) - length)
                else:
                    left = " " * ((fieldlength[field]//2) - length - 1)
                document = document + f'{right}{item.get(field)}{left}' + '|'
            print(document)

        print()


if __name__ == "__main__":
    prog = client()
    prog.clearDB("20s24")
    prog.insertDoc("s24stu.txt")
    # prog.findUserByName('Kor Qian Fu')
    prog.getUsersByAge(18)
    # prog.returnUserByAgeRange()
    # prog.getUserByHobby()
    # prog.dynamicDisplay()
    prog.close()

    
