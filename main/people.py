import pandas as pd
import math


class Person():

    def __init__(self):
        file = pd.read_excel(self.file_name)
        data = file.to_dict()
        self.data = {key : values[self.index] for key, values in data.items()}
        self.data["Name"] = self.data["First"] + " " + self.data["Last"]


class Owner(Person):

    def __init__(self):
        self.file_name = "../data/owner.xlsx"
        self.index = 0
        super().__init__()


class Customer(Person):

    def __init__(self, index):
        self.file_name = "../data/customers.xlsx"
        self.index = index
        super().__init__()
        self.set_defaults()
        
