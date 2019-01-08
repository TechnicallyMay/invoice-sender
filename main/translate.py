from datetime import datetime


months = ["January", "Febuary", "March", "April",
          "May", "June", "July", "August", "September",
          "October", "November", "December"]
current_month = datetime.now().strftime("%B")
next_month = ""
for i, month in enumerate(months):
    if current_month == month:
        next_month = months[(i + 1) % len(months)]


def translate(text, c, o):
    translations = [("<customer.first_name>", c["First"]),
                    ("<customer.full_name>", c["Name"]),
                    ("<customer.number_of_students>", c["Students"]),
                    ("<customer.monthly_rate>", c["Rate"]),
                    ("<customer.num_of_lessons>", c["Lessons"]),
                    ("<owner.full_name>", o["Name"]),
                    ("<owner.cell_number>", o["Cell"]),
                    ("<owner.address>", o["Address"]),
                    ("<owner.city_state_zip>", o["City, State, Zip"]),
                    ("<date>", datetime.now().strftime("%B %d, %Y")),
                    ("<month>", current_month),
                    ("<next_month>", next_month),
                    ("<due_date>", o["Due Date"]),
                    ("<header>", o["Header"]),
                    ("<title>", o["Title"])]
    for translation in translations:
        text = text.replace(translation[0], str(translation[1]))
    return text
