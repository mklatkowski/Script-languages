class Excercise():
    def __init__(self, content, points):
        self.content = content
        self.points = points

    def get_points(self):
        return self.points


class ClosedExcercise(Excercise):
    def __init__(self, content, points, anwsers_list, correct_index):
        super().__init__(content, points)
        self.anwsers_list = anwsers_list
        self.correct_index = correct_index

    #TODO validate

class MultipleChoiceExcercise(Excercise):
    def __init__(self, content, points, anwsers_list, correct_index_list):
        super().__init__(content, points)
        self.anwsers_list = anwsers_list
        self.correct_index_list = correct_index_list

class OpenExercise(Excercise):
    def __init__(self, content, points, correct_anwser, lines_count):
        super().__init__(content, points)
        self.correct_anwser = correct_anwser
        self.lines_count = lines_count

    #TODO validate


