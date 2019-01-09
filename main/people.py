import pandas as pd
import translate
import invoice
import invoice_email
from collections import defaultdict
from getpass import getpass


class Person():

    def __init__(self):
        file = pd.read_excel(self.file_name, keep_default_na=False)
        self.data = defaultdict()
        for column in file.columns:
            self.data[column] = file[column][self.index]
        self.data["Name"] = self.data["First"] + " " + self.data["Last"]


class Owner(Person):

    def __init__(self):
        self.file_name = "../data/owner.xlsx"
        self.index = 0
        super().__init__()
        self.data["Due Date"] = translate.translate(self.data["Due Date"], self.data)
        self.get_pass()


    def get_pass(self):
        self.password = getpass()


class Customer(Person):

    def __init__(self, index, owner):
        self.file_name = "../data/customers.xlsx"
        self.index = index
        super().__init__()
        self.owner = owner
        self.total = 0
        self.charges = self.find_charges()
        self.invoice = invoice.Invoice(self, self.owner)
        self.email = invoice_email.InvoiceEmail(self, self.owner)


    def find_charges(self):
        fee_code_file_name = "../data/fee_codes.xlsx"
        file = pd.read_excel(fee_code_file_name)
        charges = []
        for i in range(self.data["Students"]):
            charges.append([self.data["Lessons"], "Lessons", self.data["Rate"]])
            self.total += self.data["Lessons"] * self.data["Rate"]
        if self.data["Fees"] != "":
            for charge in self.data["Fees"].split(","):
                charge = charge.split()
                charge_qty = int(charge[0])
                charge_type = charge[1]
                charge_amount = float(charge[2])
                for i in range(len(file["Code"])):
                    if charge_type == file["Code"][i]:
                        charge_type = file["Description"][i]
                charges.append([charge_qty, charge_type, charge_amount])
                self.total += charge_qty * charge_amount
        return charges
