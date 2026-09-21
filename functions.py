# 1. Print Hello World

def hello():
    print("Hello, World!")


hello()


# 2. Greeting using name

def greet(name):
    print("Hello", name)


greet("Atmiya")


# 3. Add two numbers

def add(a, b):
    return a + b


print("Addition:", add(10, 20))


# 4. Find square of a number

def square(num):
    return num * num


print("Square:", square(5))


# 5. Check even or odd

def even_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


even_odd(10)


# 6. Find maximum of two numbers

def maximum(a, b):
    if a > b:
        return a
    else:
        return b


print("Maximum:", maximum(10, 20))


# 7. Convert Celsius to Fahrenheit

def fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


print("Fahrenheit:", fahrenheit(25))


# 8. Area of a circle

def circle_area(radius):
    return 3.14 * radius * radius


print("Area of circle:", circle_area(5))


# 9. Factorial of a number

def factorial(num):
    result = 1

    for i in range(1, num + 1):
        result = result * i

    return result


print("Factorial:", factorial(5))


# 10. Check positive, negative or zero

def check_number(num):
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")


check_number(-5)


# 11. Maximum of three numbers

def maximum_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


print("Maximum:", maximum_three(10, 30, 20))


# 12. Count vowels in a string

def count_vowels(text):
    count = 0

    for letter in text:
        if letter.lower() in "aeiou":
            count += 1

    return count


print("Vowels:", count_vowels("Hello World"))


# 13. Reverse a string

def reverse_string(text):
    return text[::-1]


print("Reverse:", reverse_string("Python"))


# 14. Check palindrome

def palindrome(text):
    if text == text[::-1]:
        print("Palindrome")
    else:
        print("Not a palindrome")


palindrome("madam")


# 15. Sum of all elements in a list

def list_sum(numbers):
    total = 0

    for num in numbers:
        total += num

    return total


numbers = [10, 20, 30, 40]
print("List Sum:", list_sum(numbers))


# 16. Find largest element in a list

def largest(numbers):
    big = numbers[0]

    for num in numbers:
        if num > big:
            big = num

    return big


numbers = [10, 50, 20, 40]
print("Largest:", largest(numbers))


# 17. Remove duplicate elements from a list

def remove_duplicates(numbers):
    new_list = []

    for num in numbers:
        if num not in new_list:
            new_list.append(num)

    return new_list


numbers = [1, 2, 2, 3, 3, 4]
print("Without duplicates:", remove_duplicates(numbers))


# 18. Count how many times an element appears

def count_element(numbers, element):
    count = 0

    for num in numbers:
        if num == element:
            count += 1

    return count


numbers = [1, 2, 2, 3, 2, 4]
print("Count of 2:", count_element(numbers, 2))


# 19. Check whether a number is prime

def prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


print("Is 7 prime?", prime(7))


# 20. Find prime numbers between two numbers

def prime_numbers(start, end):
    result = []

    for num in range(start, end + 1):

        if num < 2:
            continue

        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            result.append(num)

    return result


print("Prime numbers:", prime_numbers(1, 20))


# 21. Fibonacci numbers

def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")

        c = a + b
        a = b
        b = c

    print()


print("Fibonacci:")
fibonacci(10)


# 22. Find second-largest number in a list

def second_largest(numbers):
    numbers = list(set(numbers))
    numbers.sort()

    return numbers[-2]


numbers = [10, 20, 30, 40, 50]
print("Second largest:", second_largest(numbers))


# 23. Sort a list without using sort()

def my_sort(numbers):
    for i in range(len(numbers)):

        for j in range(i + 1, len(numbers)):

            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

    return numbers


numbers = [5, 2, 8, 1, 3]
print("Sorted list:", my_sort(numbers))


# 24. Merge two lists and remove duplicates

def merge_lists(list1, list2):
    result = []

    for num in list1 + list2:
        if num not in result:
            result.append(num)

    return result


list1 = [1, 2, 3]
list2 = [3, 4, 5]

print("Merged list:", merge_lists(list1, list2))
