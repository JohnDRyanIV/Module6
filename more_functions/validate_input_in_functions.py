def score_input(test_name, test_score=0, invalid_message="Invalid test score, try again!"):
    """
    :param test_name: represents name of the test
    :param test_score: represents score on test, valid between 0 and 100, inclusive
    :param invalid_message: represents message shown to user upon invalid input
    :return message: represents message being printed
    """
    while True:
        try:
            if 0 <= test_score <= 100:
                break
        except TypeError as err:
            pass
        try:
            print(invalid_message + " (" + str(test_score) + ")")
            test_score = int(input("Enter the test score: "))
        except ValueError as err:
            pass

    message = test_name + ": " + str(test_score)
    return message


if __name__ == '__main__':
    pass
