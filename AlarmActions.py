import alarm_puzzle

def generate_and_solve_puzzle():
    puzzle = alarm_puzzle.alarm_puzzle()

    while not puzzle.is_solved():
        print(puzzle.get_display(), " your input?")
        result = input()
        result = int(result)
        puzzle.input(result - 1)

class AlarmActions:
    def notify(self, alarm):
        generate_and_solve_puzzle()
        alarm.set_disarmed(True)


