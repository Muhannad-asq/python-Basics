
def find_average(numbers):
    return sum(numbers) / len(numbers)    



def find_average(array):
    return sum(array) / len(array) if array else 0




def find_average(array):
    try:
        return sum(array) / len(array)
    except ZeroDivisionError:
        return 0



def find_average(array):
    return 0 if not array else sum(array) / len(array)    
