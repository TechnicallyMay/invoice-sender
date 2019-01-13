import people
import pandas as pd
import os
import backup

owner = people.Owner()
customers = []
customer_file = pd.read_excel("../data/customers.xlsx")
num_of_customers = customer_file.shape[0]

print("Sending following emails: \n")
any_invoices = False
for i in range(num_of_customers):
    customers.append(people.Customer(i, owner))
    if customers[i].confirm():
        any_invoices = True
if any_invoices:
    print("Check 'temp' folder to see invoices.")

done = False
while not done:
    choice = input("Continue? (Y/N): ").lower().strip()
    if choice == "y":
        for customer in customers:
            print("Sending email to %s." % customer.data["Name"])
            customer.email.send()
            if customer.send_invoice:
                deleted = False
                while not deleted:
                    try:
                        os.remove(customer.invoice.file_name)
                        deleted = True
                    except PermissionError:
                        print("\nPlease close invoice and try again.")
                        _ = input("Press enter when invoice has been closed.")
            print("Sent")
        backup.backup(customers)
        done = True
    elif choice != "n":
        print("Invalid choice, try again.")
    else:
        for customer in customers:
            if customer.send_invoice:
                os.remove(customer.invoice.file_name)
        done = True
