from datetime import datetime


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
                    ("<month>", datetime.now().strftime("%B")),
                    ("<header>", o["Header"]),
                    ("<title>", o["Title"])]
    for translation in translations:
        text = text.replace(translation[0], str(translation[1]))
    return text
