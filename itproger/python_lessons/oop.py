class Cat:
    name = None
    age = None
    isHappy = None
    
    def __init__(self, name, age, isHappy): # конструктор
        # self.name = name
        # self.age = age
        # self.isHappy = isHappy
        self.setData(name, age, isHappy)
        self.getData()

    # def setData(self, name, age, isHappy): # метод 
    def setData(self, name = None, age = None , isHappy = None): # метод 
        self.name = name
        self.age = age
        self.isHappy = isHappy
    
    def getData(self): # метод 
        print('Name: ', self.name, 'Age: ', self.age, 'Happy: ', self.isHappy)

firstCat = Cat('Bob', 3, True)
# firstCat.setData('Bob', 4, True) # передача аргументов
firstCat.setData('Fred', 4)

secondCat = Cat('Kate', 5, False)
# secondCat.setData('Kate', 5, False) # передача аргументов 

firstCat.getData()
secondCat.getData()