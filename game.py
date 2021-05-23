from models.calculate import Calculate


def main():
    points = 0
    game(points)


def game(points):
    difficulty = int(input('Info the difficulty [1,2,3 or 4]: '))

    calculate = Calculate(difficulty)

    print('Info the result to the desired operation: ')

    calculate.show_operation()

    result = int(input())

    if calculate.check_result(result):
        points += 1
        print(f'You have {points} point(s).')

    continue_to_play = int(input('Do you want to continue playing? [1 - yes, 0 - no] '))

    if continue_to_play:
        game(points)
    else:
        print(f'You finished the game with {points} point(s).')
        print('See you soon! :)')


if __name__ == '__main__':
    main()
