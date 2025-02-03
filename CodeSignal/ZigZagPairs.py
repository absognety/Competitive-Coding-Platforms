def solution(numbers):
    size_of_numbers = len(numbers)
    if len(set(numbers)) == 1:
        return [0]
    indicators = []
    for index in range(size_of_numbers-1):
        if numbers[index+1] > numbers[index]:
            indicators.append(True)
        else:
            indicators.append(False)
    if len(set(indicators)) == 1:
        if True in indicators:
            if size_of_numbers % 2 == 0:
                return [0] * (size_of_numbers // 2)
            elif size_of_numbers % 2 == 1:
                return [0] * ((size_of_numbers // 2) + 1)
    output = []
    for index in range(size_of_numbers-2):
        if (numbers[index] < numbers[index+1]) & (numbers[index+1] > numbers[index+2]):
            output.append(1)
        elif (numbers[index] > numbers[index+1]) & (numbers[index+1] < numbers[index+2]):
            output.append(1)
        else:
            output.append(0)
    return output
