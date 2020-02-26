def measurements(x):
    """
    :param x: list containing measurements of shape being passed
    :return message: string detailing measurements being returned
    """
    def area(y):
        """
        :param y: list containing measurements of shape being passed
        :return: area measurement of shape
        """
        return y[len(y) % 3 - 1] * y[0]

    def perimeter(z):
        """
        :param z: listing containing measurements of shape being passed
        :return: perimeter measurement of shape
        """
        return 2 * z[len(z) % 3 - 1] + 2 * z[0]

    message = "Perimeter = " + str(perimeter(x)) + " Area = " + str(area(x))
    return message
