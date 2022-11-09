from functions import *
f = open('')

class Rednit:
    
    def __init__(self, row: str): # str mer hogy ne kelljen gondolkozni hogy split vagy mi xDDDDD
        data = row.split(';')
        self.name = data[0]
        self.age = int(data[1])
        self.gender = data[2]
        self.residence = data[3]
        self.children = int(data[4])
        self.sexuality = data[5]