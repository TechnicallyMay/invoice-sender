import pandas as pd


class Owner():

    def __init__(self):
        file_name = "../data/owner.xlsx"
        file = pd.read_excel(file_name)
        data = file.to_dict()
        self.read_data(data)


    def read_data(self, data):
        self.first_name = data['First Name'][0]
        self.last_name = data['Last Name'][0]
        self.full_name = self.first_name + " " + self.last_name
        self.title = data['Title'][0]
        self.header = data['Header'][0]
        self.pay_to = data['Payable To'][0]
        self.street_address = data['Street Address'][0]
        self.city_state_zip = data['City, State, Zip'][0]
        self.cell = data['Cell'][0]
        self.other_phone = data['Business/Home'][0]
