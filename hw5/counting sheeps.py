def count_sheeps(arrayOfSheeps):
    array1=[sheep for sheep in arrayOfSheeps if sheep == True]
    return len(array1)