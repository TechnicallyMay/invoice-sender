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

print("Sending following emails: \n")
any_invoices = False
for customer in customers:
    if customer.send_invoice:
        any_invoices = True
        print("Invoice to %s:" % (customer.data["Name"]))
        for charge in customer.charges:
            print(charge[1], end = ": ")
            print("${:0.2f}".format(charge[3]))
        print("Total: ${:0.2f}\n".format(customer.total))
    else:
        print("Announcement to %s\n" % customer.data["Name"])
if any_invoices:
    print("Check 'temp' folder to see invoices.")
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
for customer in customers:
    if customer.send_invoice:
        os.remove(customer.invoice.file_name)
