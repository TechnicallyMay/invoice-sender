import people
import pandas as pd
import os
import invoice
import translate


owner = people.Owner()
customers = []
customer_file = pd.read_excel("../data/customers.xlsx")
num_of_customers = customer_file.shape[0]
for i in range(num_of_customers):
    customers.append(people.Customer(i, owner))
    print(customers[i].data["Name"], customers[i].total)

# print("Sending following emails: ")
# for customer in customers:
#     print(customer.data["Name"])
#
# done = False
# while not done:
#     choice = input("Continue? (Y/N)")
#     if choice.lower() == "y":
#         for customer in customers:
#             print("Sending email to %s." % customer.data["Name"])
#             customer.email.send()
#             print("Sent")
#         done = True
#     elif choice.lower() != "n":
#         print("Invalid choice, try again.")
#     else:
#         done = True
# os.remove("../data/temp.docx")
