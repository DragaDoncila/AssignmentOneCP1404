class ProgrammingLanguage:
    def __init__(self, name ="", typing="static", reflection=False, year=0):
        self.name = name.capitalize()
        self.typing = typing.capitalize()
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{}, {} typing, Reflection={}, First appeared in {}".format(
            self.name, self.typing, self.reflection, self.year
        )

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True
        else:
            return False
