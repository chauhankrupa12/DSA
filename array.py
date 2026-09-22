"""ARRAY"""
#1. Create and print an array
import array

numbers = array.array('i', [10, 20, 30, 40, 50])

print(numbers)

#2. Print each element
import array

numbers = array.array('i', [10, 20, 30, 40, 50])

for num in numbers:
    print(num)
    
#3. Add elements
import array

numbers = array.array('i', [10, 20, 30])

numbers.append(40)
numbers.append(50)

print(numbers)

#4. Insert an element
import array

numbers = array.array('i', [10, 20, 40, 50])

numbers.insert(2, 30)

print(numbers)

#5. Remove an element
import array

numbers = array.array('i', [10, 20, 30, 40, 50])

numbers.remove(30)

print(numbers)

#6. Find an element
import array

numbers = array.array('i', [10, 20, 30, 40, 50])

x = 30

if x in numbers:
    print("Found")
else:
    print("Not found")

#7. Find the largest number
import array

numbers = array.array('i', [10, 45, 23, 89, 12])

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest:", largest)

#8. Reverse an array
import array

numbers = array.array('i', [10, 20, 30, 40, 50])

numbers.reverse()

print(numbers)

#9. Sum of array elements
import array

numbers = array.array('i', [10, 20, 30, 40, 50])

total = 0

for num in numbers:
    total += num

print("Sum:", total)

#10. Take input from user
import array

numbers = array.array('i')

n = int(input("Enter number of elements: "))

for i in range(n):
    value = int(input("Enter number: "))
    numbers.append(value)

print("Array:", numbers)
