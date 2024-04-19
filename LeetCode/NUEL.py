def lunchProcess(sandwiches:int, students:int) -> int:
    assert len(sandwiches) == len(students), "Error in sizes of arrays"
    sandwiches_array = sandwiches.copy()
    students_array = students.copy()
    while True:
        if len(students_array) == 0:
            return 0
        if len(set(students_array)) == 1:
            ele = list(set(students_array))[0]
            if ele != sandwiches_array[0]:
                return len(students_array)
        if students_array[0] == sandwiches_array[0]:
            sandwiches_array.pop(0)
            students_array.pop(0)
        else:
            students_array = students_array[1:] + [students_array[0]]
    

if __name__ == '__main__':
    sandwiches = [0,1,0,1]
    students = [1,1,0,0]
    print (lunchProcess(sandwiches,students))

    sandwiches = [1,0,0,0,1,1]
    students = [1,1,1,0,0,1]

    print (lunchProcess(sandwiches,students))