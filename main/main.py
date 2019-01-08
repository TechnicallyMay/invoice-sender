import people
import pandas as pd
import os
import invoice
import translate
from invoice_email import InvoiceEmail


owner = people.Owner()
customers = []
customer_file = pd.read_excel("../data/customers.xlsx")
num_of_customers = customer_file.shape[0]
for i in range(num_of_customers):
    customers.append(people.Customer(i))
owner.data["Due Date"] = translate.translate(owner.data["Due Date"], customers[0].data, owner.data)
i = invoice.Invoice(customers[11], owner)
# emails = []
# for customer in customers:
#     email = InvoiceEmail(owner, customer)
#     emails.append(email)
#
#
# print("Sending following emails: ")
# for email in emails:
#     print(email.customer.data["Name"])
#
# done = False
# while not done:
#     choice = input("Continue? (Y/N)")
#     if choice.lower() == "y":
#         for email in emails:
#             print("Sending email to %s." % email.customer.data["Name"])
#             email.send()
#         done = True
#     elif choice.lower() != "n":
#         print("Invalid choice, try again.")
#     else:
#         done = True
# os.remove("../data/temp.docx")
