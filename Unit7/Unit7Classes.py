class pet:
    petType = 'cage free pet'
    def __init__(self, age, name, breed):
        self.age = age
        self.name = name
        self.breed = breed
    def getAge(self):
        return(self.age)
    def getBreed(self):
        return(self.breed)
    def getName(self):
        return(self.name)
    def what(self):
        return('This is a '+ self.petType + ' who is ' + self.age + ' years old, is a ' + self.breed + ' named ' + self.name + '.')
#--------------------------------------------------------------------------------------------------------------------
class cage:
    petType = 'caged pet'
    def __init__(self, breed, danger):
        self.breed = breed
        self.danger = danger
    def getDanger(self):
        return(self.danger)
    def getBreed (self) :
        return(self.breed)
    def what(self):
        return('This is a '+ self.petType + ' who is a ' + self.breed + ' and ' + self.danger + ' dangerous.')
#=====================================================================================================================
