class student:
    def __init__(self,name):
        self.name = name
        self.attend = 0
        self.marks = []
        print('Welcome {} to the school'.format(name))
    def addmarks(self,ma):
        self.marks.append(ma)
    def attenddayss(self):
        self.attend += 1
    def getavg(self):
        return sum(self.marks) / len(self.marks)
