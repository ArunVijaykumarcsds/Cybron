"""
Python Programming Internship - Cybrom Technology Pvt. Ltd.
Program: List Operations - Comprehensive Guide
Author: Arun VK
Topic: List Creation, Indexing, Slicing, Methods, and Manipulation
"""

print("=" * 70)
print("LIST OPERATIONS - COMPLETE DEMONSTRATION")
print("=" * 70)
print()

# =====================================================
# Program 1: List Creation and Display
# =====================================================
print("Program 1: Creating and Displaying a List")
print("-" * 70)

lis = [1, 2, 5, 'a', 'o', 'element', 1, 2, 'amit', 3, 4, 3.5]
print("Original List:")
print(lis)
print()

print("Type of list:")
print(type(lis))
print()

# =====================================================
# Program 2: List Indexing
# =====================================================
print("Program 2: Accessing List Elements by Index")
print("-" * 70)

print("Element at index 8:")
print(lis[8])
print()

print("Element at index 0:")
print(lis[0])
print()

print("Last element (using negative index):")
print(lis[-1])
print()

# =====================================================
# Program 3: List Slicing
# =====================================================
print("Program 3: List Slicing Operations")
print("-" * 70)

print("Elements from index 2 to 7:")
print(lis[2:7])
print()

print("Elements from index 0 to end, step by 2:")
print(lis[::2])
print()

print("All elements except last one:")
print(lis[::-1])
print()

# =====================================================
# Program 4: List Modification
# =====================================================
print("Program 4: Modifying List Elements")
print("-" * 70)

print("Original list:")
print(lis)
print()

lis[2] = "amol"
print("After changing index 2 to 'amol':")
print(lis)
print()

lis[5] = 'k'
print("After changing index 5 to 'k':")
print(lis)
print()

lis[7] = 9
print("After changing index 7 to 9:")
print(lis)
print()

lis[8] = "am"
print("After changing index 8 to 'am':")
print(lis)
print()

# =====================================================
# Program 5: List Append Method
# =====================================================
print("Program 5: Adding Elements using append()")
print("-" * 70)

lis.append("qasim")
print("After appending 'qasim':")
print(lis)
print()

# =====================================================
# Program 6: Creating List from User Input
# =====================================================
print("Program 6: Dynamic List Creation from User Input")
print("-" * 70)

a = []
n = int(input("Enter number of elements you want to add: "))

for i in range(n):
    x = input(f"Enter element {i+1}: ")
    a.append(x)
    
print("\nYour custom list:")
print(a)
print()

# =====================================================
# Program 7: Creating Numeric List from User Input
# =====================================================
print("Program 7: Creating Numeric List")
print("-" * 70)

b = []
count = int(input("Enter how many numbers to add: "))

for i in range(1, count + 1):
    num = int(input(f"Enter value {i}: "))
    b.append(num)

print("\nNumeric list created:")
print(b)
print()

# =====================================================
# Program 8: All List Methods Demonstration
# =====================================================
print("=" * 70)
print("COMPREHENSIVE LIST METHODS")
print("=" * 70)
print()

# Sample list for demonstrations
sample_list = [10, 20, 30, 40, 50, 20, 60]
print("Sample List:", sample_list)
print()

# 1. append() - Add element at end
print("1. append(70):")
sample_list.append(70)
print(sample_list)
print()

# 2. insert() - Add element at specific position
print("2. insert(2, 25):")
sample_list.insert(2, 25)
print(sample_list)
print()

# 3. extend() - Add multiple elements
print("3. extend([80, 90]):")
sample_list.extend([80, 90])
print(sample_list)
print()

# 4. remove() - Remove first occurrence
print("4. remove(20):")
sample_list.remove(20)
print(sample_list)
print()

# 5. pop() - Remove and return element at index
print("5. pop(3):")
removed = sample_list.pop(3)
print(f"Removed: {removed}")
print(sample_list)
print()

# 6. pop() - Remove last element
print("6. pop() [removes last element]:")
last = sample_list.pop()
print(f"Removed: {last}")
print(sample_list)
print()

# 7. index() - Find index of element
print("7. index(50):")
idx = sample_list.index(50)
print(f"Index of 50: {idx}")
print()

# 8. count() - Count occurrences
print("8. count(20):")
count = sample_list.count(20)
print(f"20 appears {count} time(s)")
print()

# 9. sort() - Sort list in ascending order
print("9. sort():")
sample_list.sort()
print(sample_list)
print()

# 10. reverse() - Reverse list
print("10. reverse():")
sample_list.reverse()
print(sample_list)
print()

# 11. copy() - Create shallow copy
print("11. copy():")
list_copy = sample_list.copy()
print(f"Original: {sample_list}")
print(f"Copy: {list_copy}")
print()

# 12. clear() - Remove all elements
print("12. clear() on copy:")
list_copy.clear()
print(f"After clear: {list_copy}")
print(f"Original unchanged: {sample_list}")
print()

# =====================================================
# Program 9: List Comprehension Examples
# =====================================================
print("Program 9: List Comprehension")
print("-" * 70)

# Squares of numbers
squares = [x**2 for x in range(1, 11)]
print("Squares of 1 to 10:")
print(squares)
print()

# Even numbers
evens = [x for x in range(1, 21) if x % 2 == 0]
print("Even numbers from 1 to 20:")
print(evens)
print()

# Odd numbers
odds = [x for x in range(1, 21) if x % 2 != 0]
print("Odd numbers from 1 to 20:")
print(odds)
print()

# =====================================================
# Program 10: Nested Lists (2D Lists)
# =====================================================
print("Program 10: Working with Nested Lists")
print("-" * 70)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("2D List (Matrix):")
for row in matrix:
    print(row)
print()

print("Accessing element at row 1, column 2:")
print(matrix[1][2])
print()

# =====================================================
# Program 11: List Operations - Sum, Max, Min, Len
# =====================================================
print("Program 11: Built-in Functions with Lists")
print("-" * 70)

numbers = [45, 12, 78, 23, 56, 89, 34]
print("Number list:", numbers)
print()

print(f"Sum of elements: {sum(numbers)}")
print(f"Maximum element: {max(numbers)}")
print(f"Minimum element: {min(numbers)}")
print(f"Length of list: {len(numbers)}")
print(f"Average: {sum(numbers)/len(numbers):.2f}")
print()

# =====================================================
# Program 12: List Concatenation and Repetition
# =====================================================
print("Program 12: List Concatenation and Repetition")
print("-" * 70)

list1 = [1, 2, 3]
list2 = [4, 5, 6]

print("List 1:", list1)
print("List 2:", list2)
print()

# Concatenation
combined = list1 + list2
print("Concatenation (list1 + list2):")
print(combined)
print()

# Repetition
repeated = list1 * 3
print("Repetition (list1 * 3):")
print(repeated)
print()

# =====================================================
# Program 13: Membership Testing
# =====================================================
print("Program 13: Membership Testing")
print("-" * 70)

fruits = ['apple', 'banana', 'orange', 'mango', 'grape']
print("Fruit list:", fruits)
print()

search = input("Enter fruit name to search: ")
if search in fruits:
    print(f"✓ {search} is in the list!")
else:
    print(f"✗ {search} is NOT in the list!")
print()

# =====================================================
# Program 14: Interactive List Manager
# =====================================================
print("Program 14: Interactive List Manager")
print("-" * 70)

my_list = []
print("Starting with empty list:", my_list)

while True:
    print("\n--- List Operations Menu ---")
    print("1. Display List")
    print("2. Add Element")
    print("3. Remove Element")
    print("4. Update Element")
    print("5. Sort List")
    print("6. Reverse List")
    print("7. Search Element")
    print("8. Clear List")
    print("9. Exit")
    
    choice = input("\nEnter your choice (1-9): ")
    
    if choice == '1':
        print("Current List:", my_list)
    
    elif choice == '2':
        element = input("Enter element to add: ")
        my_list.append(element)
        print("Element added!")
    
    elif choice == '3':
        if my_list:
            element = input("Enter element to remove: ")
            if element in my_list:
                my_list.remove(element)
                print("Element removed!")
            else:
                print("Element not found!")
        else:
            print("List is empty!")
    
    elif choice == '4':
        if my_list:
            try:
                idx = int(input("Enter index to update: "))
                new_value = input("Enter new value: ")
                my_list[idx] = new_value
                print("Element updated!")
            except IndexError:
                print("Invalid index!")
        else:
            print("List is empty!")
    
    elif choice == '5':
        if my_list:
            my_list.sort()
            print("List sorted!")
        else:
            print("List is empty!")
    
    elif choice == '6':
        if my_list:
            my_list.reverse()
            print("List reversed!")
        else:
            print("List is empty!")
    
    elif choice == '7':
        element = input("Enter element to search: ")
        if element in my_list:
            print(f"Found at index: {my_list.index(element)}")
        else:
            print("Element not found!")
    
    elif choice == '8':
        my_list.clear()
        print("List cleared!")
    
    elif choice == '9':
        print("Exiting List Manager...")
        break
    
    else:
        print("Invalid choice! Please try again.")

print()
print("=" * 70)
print("All List Operations Completed Successfully!")
print("=" * 70)