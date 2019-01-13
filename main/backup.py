import os
import pandas as pd
from datetime import datetime


def backup(customers):
    data = {
            "Name" : [],
            "Charges" : [],
            "Total" : []
            }
    for customer in customers:
        if customer.send_invoice:
            d = customer.data
            data["Name"].append(d["First"] + " " + d["Last"])
            charges = []
            for charge in customer.charges:
                formatted = "%d %s @" % (charge[0], charge[1])
                formatted += " ${:.2f}".format(charge[2])
                charges.append(formatted)
            data["Charges"].append(", ".join(charges))
            data["Total"].append(customer.total)
    if len(data["Name"]) > 0:
        backup_name = get_dir(input("Name backup: "))
        df = pd.DataFrame(data)
        writer = pd.ExcelWriter(backup_name, engine="xlsxwriter")
        df.to_excel(writer, sheet_name="Sheet1", index=False)
        writer.save()


def get_dir(name):
    year = datetime.now().strftime("%Y")
    year_dir = "../data/Records/" + year
    file_name = year_dir + "/" + name + ".xlsx"
    if not os.path.exists(year_dir):
        os.makedirs(year_dir)
    return file_name
