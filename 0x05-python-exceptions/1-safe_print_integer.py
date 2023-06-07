def safe_print_integer(value):
    try:
        value = int(value)
        print("{:d}".format(value))
        return True
    except ValueError:
        return False