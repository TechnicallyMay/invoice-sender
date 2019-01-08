import pandas as pd
import math
from getpass import getpass


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
        self.get_pass()


    def get_pass(self):
        self.password = getpass()


class Customer(Person):

    def __init__(self, index):
        self.file_name = "../data/customers.xlsx"
        self.index = index
        super().__init__()
        self.charges = self.find_charges()


    def find_charges(self):
        charges = []
        for i in range(self.data["Students"] + 1):
            charges.append([self.data["Lessons"], "Lessons", self.data["Rate"]])
        try:
            for charge in self.data["Fees"].split(","):
                charge = charge.split()
                charge_qty = charge[0]
                charge_type = charge[1]
                charge_amount = charge[2]
                if charge_type == "B":
                    charge_type = "Books"
                elif charge_type == "L":
                    charge_type = "Late Fees"
                else:
                    charge_type = "Other"
                charges.append([charge_qty, charge_type, charge_amount])
        except AttributeError:
            return charges
        return charges
