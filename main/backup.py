import shutil
import os
import pandas as pd
from datetime import datetime


def backup(customers, backup_name):
    backup_name = get_dir(backup_name)
    data = {
            "Names" : [],
            "Charges" : [],
            "Totals" : []
            }
    for customer in customers:
        d = customer.data
        data["Names"].append(d["First"] + " " + d["Last"])
        charge_descriptions = [charge[1] for charge in customer.charges]
        data["Charges"].append(", ".join(charge_descriptions))
        data["Totals"].append(customer.total)
    df = pd.DataFrame(data)
    writer = pd.ExcelWriter(backup_name, engine="xlsxwriter")
    df.to_excel(writer, sheet_name="Sheet1", index=False)
    writer.save()


def get_dir(name):
    date = datetime.now()
    year = date.strftime("%Y")
    year_dir = "../data/Records/" + year
    file_name = year_dir + "/" + name + ".xlsx"
    if not os.path.exists(year_dir):
        os.makedirs(year_dir)
    return file_name
