class Student:
    def __init__(self, name, netid):
        self.name = name
        self.netid = netid
    def __lt__(self, other):
        if isinstance(other, Student):
            return self.name < other.name
        return NotImplemented

mylist = [
    Student("John Doe", 1),
    Student("Jane Doe", 5),
]
def get_netid(student):
    return student.netid
get_netid = lambda student: student.netid


#mylist.sort(key=get_netid)
#mylist.sort(key=lambda x: x.netid)
#mylist = sorted(mylist, key=lambda x: x.netid)
#max_stu = max(mylist, key=lambda x: x.netid)
#print([x.name for x in mylist])
