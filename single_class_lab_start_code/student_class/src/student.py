class Student: 
    def __init__(self, name, cohort):
        self.name = name
        self.cohort = cohort
    def talk(self):
        self.print("I can talk")
    def say_favourite_language(self, fav_language):
        self.print(f"I love {fav_language}")


