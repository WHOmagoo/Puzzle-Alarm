import AlarmPuzzle

def generate_and_solve_puzzle():
    puzzle = AlarmPuzzle.alarm_puzzle()

    while not puzzle.is_solved():
        print(puzzle.get_display(), " your input?")
        result = input()
        result = int(result)
        puzzle.input(result - 1)

class AlarmActions:
    def notify(self, alarm):
        puzzle = AlarmPuzzle.a
        generate_and_solve_puzzle()


