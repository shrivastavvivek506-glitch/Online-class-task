
numbers = []

n = int(input("How many numbers? "))

for i in range(n):
    value = int(input("Enter Number: "))
    numbers.append(value)

print("Original List:", numbers)

numbers.sort()

print("Ascending Order:", numbers)

numbers.sort(reverse=True)

print("Descending Order:", numbers)

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))
