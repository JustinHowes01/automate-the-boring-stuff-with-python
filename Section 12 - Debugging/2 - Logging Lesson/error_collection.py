import logging

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# OR log to a text file
logging.basicConfig(filename='my_program.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Use to disable logging
# logging.disable(logging.CRITICAL)

logging.debug('Start of Program')


def factorial(n):
    logging.debug('Start of factorial(%s)' % n)
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))

    logging.debug('Return value is %s' % total)
    return total


print(factorial(5))

logging.debug('End of Program')
