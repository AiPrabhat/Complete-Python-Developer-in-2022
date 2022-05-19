def do_stuff(num):
    try:
        return int(num) + 5
    except ValueError as err:
        return err
    
def do_stuff2(num=0):
    try:
        if num:
            return int(num) + 5
        else:
            return 'please enter number'
    except ValueError as err:
        return err