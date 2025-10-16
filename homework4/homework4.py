# homework4.py


# 3. Lists 

# 3.1 List Operations 
food = ["cookie", "peach", "pasta", "coffee", "oatmeal"]

print(food[1])

print(food[-1])

food.append("lemon")
print(food) 

food.insert(0, "apple")
print(food)

food.remove("peach")
print(food)

print(len(food))

for item in food:
    print(item.upper())

print(food[0::5])

if "potato" in food:
    print("A potato!")
else:
    print("No potato!")


# 3.2 Slicing and Striding 
numbers = list(range(0,21))
print(numbers)

def get_first_15(numbers):
    return numbers[:15]

step1 = get_first_15(numbers)
print(step1)

def get_every_5th(step1):
    return step1[::5]

step2 = get_every_5th(step1)
print(step2)

def reverse_and_stride(step1):
    reversed = step1[::-1]
    final = reversed[::3]
    return final 

step3 = reverse_and_stride(step1)
print(step3)



# 3.3 Nested Lists 
# 3.3.1 Nested List Operations 

numbers = [[1,2,3], [4,5,6], [7,8,9]]
print(numbers[2])
print(numbers[1][1])
numbers.append([10,11,12])
print(numbers)

def sum_nested(numbers):
    total = 0
    for row in numbers:
        for num in row:
            total += num 

    return total 

total_sum = sum_nested(numbers)
print(total_sum)

# 3.4 Create a 5x5 List 

def create_5x5():
    result = []
    num = 1

    for i in range(5):      # 5 item rows 
        row = []            # create a new row
        for j in range(5):  # 5 item column 
            row.append(num) # add the number to the row 
            num +=1         # add by 1
        result.append(row)  #add row to the result 

    return result 

matrix = create_5x5()
print(matrix)

def replace_multiples(matrix):
    new_matrix = []

    for row in matrix:
        new_row = []
        for num in row:
            if num % 3 == 0:
                new_row.append("?")
            else:
                new_row.append(num)
        new_matrix.append(new_row)

    return new_matrix

matrix = create_5x5()

question_matrix = replace_multiples(matrix)
for row in question_matrix:
    print(row)

def sum_no_question(matrix):
    total = 0 
    for row in matrix:
        for num in row: 
            if num != "?": 
                total += num 
    return total 

matrix = create_5x5()
question_matrix = replace_multiples(matrix)
result = sum_no_question(question_matrix) 

print(result)

# 4 Dictionaries 

# 4.1 Dictionary Operations 

ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25, 
    "Mira": 48 
}

print(ages)
print(ages["Katie"])

ages["Mira"] = 100
print(ages["Mira"])

ages["Milana"] = 52
print(ages)

del ages["Mariam"]
print(ages)

for key, value in ages.items():
    print(f"{key} = {value}")








