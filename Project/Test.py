import Excercise

class Test():
    def __init__(self, exercises_list):
        self.excercises_list = exercises_list
        self.points = self.get_points()

    def get_points(self):
        points = 0
        for exc in self.excercises_list:
            points += exc.get_points()
        return points