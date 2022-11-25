class Robot:
    def __init__(self, model, age):
        self.model = model
        self.age = age

    def talk(self):
        print(
            f"Hey man im robot {self.model} I've hated humans for {self.age} years")


class Teach(Robot):
    def __init__(self, model, age, subject):
        super().__init__(model, age)
        self.subject = subject

    def talk(self):
        print(
            f"Hey man im {self.model} I've served humans for {self.age} I teach in {self.subject} ")


class Cleaning(Robot):
    def __init__(self, model, age, efficency):
        super().__init__(model, age)
        self.efficency = efficency

    def talk(self):
        print(
            f"Hey man im {self.model} I've served humans for {self.age} years my rating speed is {self.efficency} /10 ")


class Builder(Robot):
    def __init__(self, model, age, job):
        super().__init__(model, age)
        self.job = job

    def talk(self):
        print(
            f"Hey man im {self.model} I've served humans for {self.age} my workplace is {self.job} ")


r = Robot("A245", 40)
r.talk()
t = Teach("A60k", 16, "Mathematics")
t.talk()
c = Cleaning("Aed0", 5, 10)
c.talk()
b = Builder("Rbogo", 5, "Volvo")
b.talk()
