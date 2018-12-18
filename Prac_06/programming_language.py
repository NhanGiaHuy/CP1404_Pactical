class ProgrammingLanguage:
    def __init__(self, field, typing, reflection, year):
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year


    def get_field(self):
        return self.field

    def get_typing(self):
        return self.typing

    def get_reflection(self):
        return self.reflection

    def get_year(self):
        return self.year

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True
        else:
            return False

    def __str__(self):
        return "{}, {} typing, Reflection = {}, First appered in {}".format(self.field, self.typing, self.reflection, self.year)