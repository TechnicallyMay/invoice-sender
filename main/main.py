import people
import pandas as pd
import os
import shutil
from datetime import datetime

owner = people.Owner()
customers = []
customer_file = pd.read_excel("../data/customers.xlsx")
num_of_customers = customer_file.shape[0]

print("Sending following emails: \n")
any_invoices = False
for i in range(num_of_customers):
    customers.append(people.Customer(i, owner))
    if customers[i].send_invoice:
        any_invoices = True
        print("Invoice to %s (%s):" % (customers[i].data["Name"], customers[i].data["Email"]))
        for charge in customers[i].charges:
            print(charge[1], end = ": ")
            print("${:0.2f}".format(charge[3]))
        print("Total: ${:0.2f}\n".format(customers[i].total))
    else:
        print("Announcement (no invoice) to %s\n" % customers[i].data["Name"])
if any_invoices:
    print("Check 'temp' folder to see invoices.")

done = False
while not done:
    choice = input("Continue? (Y/N): ").lower().strip()
    if choice == "y":
        for customer in customers:
            print("Sending email to %s." % customer.data["Name"])
            #customer.email.send()
            if customer.send_invoice:
                os.remove(customer.invoice.file_name)
            print("Sent")
        done = True
    elif choice != "n":
        print("Invalid choice, try again.")
    else:
        for customer in customers:
            os.remove(customer.invoice.file_name)
        done = True
date = datetime.now()
year = date.strftime("%Y")
month = input("Name backup: ")
year_dir = "../data/Records/" + year
file_name = year_dir + "/" + month + ".xlsx"
if not os.path.exists(year_dir):
    os.makedirs(year_dir)
shutil.copyfile("../data/customers.xlsx", file_name)
