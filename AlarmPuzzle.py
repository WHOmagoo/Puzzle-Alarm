import random

class alarm_puzzle:
    display = []
    correct = 0
    solved = False

    def __init__(self):
        self.generate_puzzle()

    def is_solved(self):
        return self.solved

    def generate_puzzle(self):
        self.correct = 0
        self.display = []
        for i in range(4):
            new_rand = random.randint(0, 9 - i)
            while new_rand in self.display:
                new_rand += 1

            self.display.append(new_rand)

    def get_display(self):
        return self.display

    def get_nth_lowest_index(self, n):

        indexes = []
        for i in range(n):
            low_index = -1
            low_val = 10
            for j in range(4):
                if j in indexes:
                    continue
                if self.display[j] < low_val:
                    low_index = j
                    low_val = self.display[j]

            indexes.append(low_index)

        return indexes.pop()

    def is_correct(self, button_pushed):
        return self.get_nth_lowest_index(self.correct + 1) == button_pushed - 1

    def input(self, button_pushed):
        correct = self.is_correct(button_pushed)

        if not correct:
            print(button_pushed, " was wrong should have been ", self.get_nth_lowest_index(self.correct + 1))
            self.generate_puzzle()
        else:
            print(button_pushed, " was correct!")
            self.correct += 1
            if self.correct >= 4:
                self.solved = True

    # def push_button(self, button_number):
    #
    #     i = button_number
    #     if self.is_correct(button_number):
    #         self.correct += 1
    #     else:
    #         self.correct = 0
    #         self.generate_puzzle()
    #
    #     self.solved = self.correct == 4
    #
    #     return self.solved
