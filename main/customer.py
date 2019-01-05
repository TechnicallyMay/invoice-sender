import math


class Customer():

    def __init__(self, info):
        self.first_name = info[0]
        self.last_name = info[1]
        self.email = info[2]
        self.num_of_students = info[3]
        if math.isnan(info[4]):
            self.num_of_lessons = 4
        else:
            self.num_of_lessons = int(info[4])
        self.rate = info[5]
        if math.isnan(info[6]):
            self.fees = None
        else:
            self.fees = info[6]
