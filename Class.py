class student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def show(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)    

s1 = student("shakib", 10)
s1.show()
s2 = student("Alice", 20)
s2.show()

