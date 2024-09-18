from pythonBasics_Rshetty.Classes_Objects import Calculator


class ChildClass(Calculator):
    numchild = 200

   # def __init__(self):
   #     Calculator.__init__(self, 5, 8)


    def getCompleteData(self):
        return  self.num + self.numchild +self.summation()


obj = ChildClass(5, 6)
completedata= obj.getCompleteData()
print(completedata)