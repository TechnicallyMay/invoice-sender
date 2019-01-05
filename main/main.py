import pandas as pd
from customer import Customer


file_name = "../data/customers.xlsx"
file = pd.read_excel(file_name)
num_of_customers = file.shape[0]
data = file.to_dict()

customers = []


def read_customer(num):
    customer_info = []
    for key, values in data.items():
        customer_info.append(values[i])
    return Customer(customer_info)


for i in range(num_of_customers):
    customers.append(read_customer(i))
    
for customer in customers:
    for key, value in vars(customer).items():
        print(key, value)
    print()
