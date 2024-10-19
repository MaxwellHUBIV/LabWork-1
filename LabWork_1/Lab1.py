numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
medium_number = numbers
medium_number[4] = 0
medium = sum(medium_number)/(len(medium_number))
medium_number[4] = medium

print("Измененный список:", medium_number)
