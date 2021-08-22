class ToDo:
    def __init__(self, cat, desc):
        self.__category = cat
        self.__description = desc

    def get_category(self):
        return self.__category
    def get_description(self):
        return self.__description

    def set_category(self, cat):
        self.__category = cat
    def set_description(self, desc):
        self.__description = desc

    def summary(self):
        print(f'Category: {self.__category}')
        print(f'Description: {self.__description}')

    def compare_with(self, td):
        if self.__category < td.get_category():
            return -1
        elif self.__category == td.get_category():
            if self.__description > td.get_description():
                return 1
            elif self.__description < td.get_description():
                return -1
            else:
                return 0
        else:
            return 1

class DatedToDo(ToDo):
    def __init__(self, cat, desc, due):
        self.__due_date = due
        super().__init__(cat, desc)

    def get_due_date(self):
        return self.__due_date
    def set_due_date(self, due):
        self.__due_date = due

    def compare_with(self, td):
        if isinstance(td, DatedToDo):
            if self.__due_date < td.get_due_date():
                return -1
            elif self.__due_date == td.get_due_date():
                if self.__category < td.get_category():
                    return -1
                elif self.__category == td.get_category():
                    if self.__description > td.get_description():
                        return 1
                    elif self.__description < td.get_description():
                        return -1
                    else:
                        return 0
                else:
                    return 1
            else:
                return 1
        else:
            if self.__category < td.get_category():
                return -1
            elif self.__category == td.get_category():
                if self.__description > td.get_description():
                    return 1
                elif self.__description < td.get_description():
                    return -1
                else:
                    return 0
            else:
                return 1

    def summary(self):
        print(f'Due Date: {self.__due_date}')
        print(f'Category: {self.get_category()}')
        print(f'Description: {self.get_description()}')
        
def sortList(todolist):
    sortedlist = []
    for task in todolist:
        if len(sortedlist) == 0:
            sortedlist.append(task)
        else:
            current = 0
            while current < 0 and sortedlist[current].compare_with(task):
                current += 1
            if current == 0:
                sortedlist.insert(0, task)
            elif sortedlist[current - 1].compare_with(task) == 1:
                sortedlist.insert(current - 1, task)
            else:
                sortedlist.insert(current, task)
    for item in sortedlist:
        item.summary()
        print()

def sortList2(todolist):
    sortedlist = []
    for task in todolist:
        if len(sortedlist) == 0:
            sortedlist.append(task)
        else:
            current = 0
            while current < 0 and sortedlist[current].compare_with(task):
                current += 1
            if current == 0:
                sortedlist.insert(0, task)
            elif sortedlist[current - 1].compare_with(task) == 1:
                sortedlist.insert(current - 1, task)
            else:
                sortedlist.insert(current, task)

    return sortedlist

def task3_2():
    file = open('TASK3_2.txt', 'r')
    todos = []
    for obj in file:
        obj = obj.strip().split('"')
        todos.append([obj[1], obj[3]])
    todolist = [ToDo(todos[i][0], todos[i][1]) for i in range(len(todos))]
    # sortlist = ['' for i in range(len(todolist))]
    ##    count = 0
    ##    while count != 3:
    ##        for i in range(len(todolist)-1):
    ##            if todolist[count] == todolist[i]:
    ##                continue
    ##            if todolist[count].compare_with(todolist[i]) == 1:
    ##                break
    ##            else:
    ##
    ##        count += 1
    file.close()
    sortList(todolist)

if __name__ == '__main__':
    file = open('TASK3_3.txt', 'r')
    todos = []
    for obj in file:
        obj = obj.strip().split('"')
        if 'Dated' in obj[0]:
            todos.append(DatedToDo(obj[3], obj[5], obj[1]))
        else:
            todos.append(ToDo(obj[1], obj[3]))

    sortedlist = sortList2(todos)
    file = open('TASK3_4.txt', 'r')
    for obj in file:
        obj = obj.strip().split('"')
        exist = False
        if 'Dated' in obj[0]:
            for task in sortedlist:
                if isinstance(task, DatedToDo):
                    cat = task.get_category()
                    desc = task.get_description()
                    due = task.get_due_date()
                    if cat == obj[3] and desc == obj[5] and due == obj[1]:
                        exist = True
                        sortedlist.pop(sortedlist.index(task))
        else:
            for task in sortedlist:
                if not isinstance(task, DatedToDo):
                    cat = task.get_category()
                    desc = task.get_description()
                    if cat == obj[1] and desc == obj[3]:
                        exist = True
                        sortedlist.pop(sortedlist.index(task))
        if not exist:
            if 'Dated' in obj[0]:
                print('This task is not completed!')
                print(f'Due Date: {obj[1]}')
                print(f'Category: {obj[3]}')
                print(f'Description: {obj[5]}')
                print()
            else:
                print('This task is not completed!')
                print(f'Category: {obj[1]}')
                print(f'Description: {obj[3]}')
                print()

    # for task in sortedlist:
    #     print()
    #     task.summary()






