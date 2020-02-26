def measurements(x):
    def area(y):
        return y[0] * y[1]

    def perimeter(z):
        return 2*z[0] + 2*z[1]

    message = "Perimeter = " + str(perimeter(x)) + " Area = " + str(area(x))
    print(message)
    return message
    pass


