class Guitar:

    def __init__(self, name=" ", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def get_name(self):
        return self.name

    def get_year(self):
        return self.year

    def get_cost(self):
        return self.cost

    def __str__(self):
        return "{} ({}) : ${:,}".format(self.name, self.year, self.cost)

    def get_age(self):
        age = 2018 - self.year
        return age

    def is_vintage(self):
        if 2018 - self.year >= 50:
            return True
        else:
            return False
