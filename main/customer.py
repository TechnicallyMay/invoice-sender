import math
import pandas as pd


customers = []
file_name = "../data/customers.xlsx"
file = pd.read_excel(file_name)
num_of_customers = file.shape[0]
data = file.to_dict()


class Customer():

    def __init__(self, info):
        self.first_name = info[0]
        self.last_name = info[1]
        self.full_name = self.first_name + " " + self.last_name
        self.email = info[2]
        self.num_of_students = info[3]
        if math.isnan(info[4]):
            self.num_of_lessons = 4
        else:
            self.num_of_lessons = int(info[4])
        self.rate = info[5]
        if math.isnan(info[6]):
            self.fees = None
        else:
            self.fees = info[6]


def read_customer(num):
    customer_info = []
    for key, values in data.items():
        customer_info.append(values[i])
    return Customer(customer_info)


for i in range(num_of_customers):
    customers.append(read_customer(i))
