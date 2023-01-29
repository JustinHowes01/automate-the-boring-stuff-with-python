import traceback

"""
****************
*              *
*              *
*              *
****************
"""


def box_print(symbol, width, height):  # Raising an error if input goes out of bounds
    if len(symbol) != 1:
        raise Exception('Symbol needs to be a string of length 1')
    if (width < 2) or (height < 2):
        raise Exception('"width" and "height" must be greater than or equal to 2')

    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)


box_print('*', 15, 3)

# assert statement
market_2nd = {'ns': 'green', 'ew': 'red'}


def switch_lights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'

    # assertion calls out the fact that at some point, all cars will be going both directions and the light is not red
    assert 'red' in intersection.values(), 'Neither light is red! ' + str(intersection)


switch_lights(market_2nd)

# Outputting the error exception to a text file to be read later and not lost
try:
    raise Exception('This is an error message')
finally:
    error_file = open('error_log.txt', 'a')
    error_file.write(traceback.format_exc())
    error_file.close()
    print('The traceback info was written in error_log.txt')
