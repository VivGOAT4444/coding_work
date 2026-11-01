class Employee:
    def __init__(self):
        print('Employee created')


    def __del__(self):
        print('Destructor called')


def Creates_obj():
    print('Making Object...')
    obj = Employee()
    print('function end...') 
    return obj

print('Calling Creates_obj() function...')
obj = Creates_obj()
print('Program End...')
