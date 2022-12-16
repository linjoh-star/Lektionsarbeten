class Robot:
    def __init__(self, model, age):
        self.model = model
        self.age = age

    def talk(self):
        print(
            f"(Robot)Hey man im robot {self.model} I've hated humans for {self.age} years\n")


class Teach(Robot):
    def __init__(self, model, age, subject):
        super().__init__(model, age)
        self.subject = subject

    def talk(self):
        print(
            f"(Teach)Hey man im {self.model} I've served humans for {self.age} I teach in {self.subject}\n ")


class Cleaning(Robot):
    def __init__(self, model, age, efficency):
        super().__init__(model, age)
        self.efficency = efficency

    def talk(self):
        print(
            f"(Cleaning)Hey man im {self.model} I've served humans for {self.age} years my rating speed is {self.efficency} /10\n ")


class Builder(Robot):
    def __init__(self, model, age, job):
        super().__init__(model, age)
        self.job = job

    def talk(self):
        print(
            f"(Builder)Hey man im {self.model} I've served humans for {self.age} my workplace is {self.job}\n ")


class RobotFactory:
    def create_robot(self, model, age):
        return Robot(model, age)


class TeachFactory(RobotFactory):
    def create_robot(self, model, age, subject):
        return Teach(model, age, subject)


class CleaningFactory(RobotFactory):
    def create_robot(self, model, age, efficency):
        return Cleaning(model, age, efficency)


class BuilderFactory(RobotFactory):
    def create_robot(self, model, age, job):
        return Builder(model, age, job)


class AbstractRobotFactory:
    def create_robot(self, robot_type, *args, **kwargs):
        if robot_type == "robot":
            return Robot(*args, **kwargs)
        elif robot_type == "teach":
            return Teach(*args, **kwargs)
        elif robot_type == "cleaning":
            return Cleaning(*args, **kwargs)
        elif robot_type == "builder":
            return Builder(*args, **kwargs)


factory = RobotFactory()
robot = factory.create_robot("Samuel", 40)
robot.talk()

factory = TeachFactory()
robot = factory.create_robot("Emil", 16, "Mathematics")
robot.talk()

factory = CleaningFactory()
robot = factory.create_robot("Arvid", 5, 10)
robot.talk()

factory = BuilderFactory()
robot = factory.create_robot("Widescott", 5, "Volvo")
robot.talk()

factory = AbstractRobotFactory()
robot = factory.create_robot("robot", "Empdo", 40)
robot.talk()

robot = factory.create_robot("teach", "Essung", 16, "Physics")
robot.talk()

robot = factory.create_robot("cleaning", "Kvocka", 5, 10)
robot.talk()

robot = factory.create_robot("builder", "Linus", 5, "Tesla")
robot.talk()
