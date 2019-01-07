import people
import pandas as pd
from invoice_email import InvoiceEmail


owner = people.Owner()
customers = []
customer_file = pd.read_excel("../data/customers.xlsx")
num_of_customers = customer_file.shape[0]
for i in range(num_of_customers):
    customers.append(people.Customer(i))

email = InvoiceEmail(owner, customers[0])
email.replace_key_words()
# print(email.body)

for customer in customers:
    for key, value in vars(customer).items():
        print(key, value)
    print()
