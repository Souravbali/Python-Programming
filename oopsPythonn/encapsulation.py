class person:
    def __init__(self,name,age):
        self.__name = name 
        self.__age = age
    def getname(self):
        return self.__name
    def setname(self,name):
        self.__name = name 

per = person("sourav",24)
print(per.getname())
per.setname("Raj")
print(per.getname())