def check_answer(status, answer, object_x, object_y):
    """
    Checks if the user's answers were right or wrong with the
    object they collided with.

    :param status: the current status of the game
    :param answer: the answer the user gave
    :param object_x: the x-coordinate location of the object
    :param object_y: the y-coordinate location of the object
    :return bool: True if their answer is correct and false otherwise
    """

    # Lowercases the answer
    s = answer.lower()

    if status == 1 and s == "hollywood":
        return True

    if status == 2 and s == "150723":
        return True

    if status == 4:
        if s == "y":
            if object_x == 563 and object_y == 360:
                return True
            else:
                return False

    if status == 5:
        if s == "y":
            return True

    if status == 7 and s == "h":
        return True

    if status == 8 and s == "a":
        return True

    if status == 9 and s == "i":
        return True

    if status == 10 and s == "l":
        return True

    if status == 11 and s == "ng":
        return True

    if status == 14 and s == "1105":
        return True

    if status == 15:
        if s == "y":
            return True

    if status == 18:
        if s == "y":
            if object_x == 300 and object_y == 250:
                return True

    if status == 20 and s == "paths":
        return True

    if status == 22:
        if s == "y":
            if object_x == 70 and object_y == 310:
                return True

    if status == 23:
        if s == "y":
            return True

    return False
