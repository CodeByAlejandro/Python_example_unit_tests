def chk_succesful_guess(number, answer):
    if isinstance(number, bool):
        raise TypeError('Got boolean, expected int')
    number = int(number)
    if 0 < number < 11:
        if number == answer:
            return True
        else:
            return False
    else:
        raise ValueError('Got value out of range')


if __name__ == '__main__':

    from random import randint
    # generate a number 1~10
    randint = randint(1, 10)

    # input from user?
    # check that input is a number 1~10
    while True:
        guess = input('guess a number 1~10:  ')
        try:
            result = chk_succesful_guess(guess, randint)
            if result:
                print('you are a genius!')
                break
        except ValueError as err:
            if str(err) == 'Got value out of range':
                print('hey bozo, I said 1~10')
            else:
                print('please enter a number')
        except TypeError:
            print('please enter a number')
