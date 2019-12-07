import turtle


class Robot:
    def __init__(self):
        self.direction = "nord"
        self.x = 0
        self.y = 0

    def avance(self):
        pass

    def tourne_gauche(self):
        pass

    def tourne_droite(self):
        pass




class Simulation:
    def __init__(self):
        self.robot = Robot()

    def démarre(self):
        turtle.goto(0, 0)
        turtle.setheading(90)
        turtle.pendown()

        turtle.listen()

        self.connecte_touches()
        turtle.mainloop()

    def connecte_touches(self):
        turtle.onkey(self.avance_robot, "Up")
        turtle.onkey(self.tourne_robot_gauche, "Left")
        turtle.onkey(self.tourne_robot_droite, "Right")
        turtle.onkey(self.quitte, "q")

    def quitte(self):
        turtle.bye()

    def avance_robot(self):
        self.robot.avance()
        self.affiche_robot()

    def tourne_robot_droite(self):
        self.robot.tourne_droite()
        self.affiche_robot()

    def tourne_robot_gauche(self):
        self.robot.tourne_gauche()
        self.affiche_robot()

    def affiche_robot(self):
        turtle.goto(self.robot.x * 10, self.robot.y * 10)
        heading = {"nord": 90, "est": 0, "sud": 270, "ouest": 180}[self.robot.direction]
        turtle.setheading(heading)


def main():
    simulation = Simulation()
    simulation.démarre()


main()
