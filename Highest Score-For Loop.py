# Exercise 5.1
student_heights = input("Enter the list of Students height: ").split()

for x in range(0, len(student_heights)):
    student_heights[x] = int(student_heights[x])

height = 0
for height1 in student_heights:
    height += height1

#print(height)

total = 0
for total1 in student_heights:
    total += 1
#print(total)

average = round(height /total)
print(average)



# Exercise 5.2

student_scores = input("Enter the list of Student score: ").split()


for high in range(0, len(student_scores)):
    student_scores[high] = int(student_scores[high])

marks = 0
for x in student_scores:
    if x > marks:
        marks = x
        
print(f"The highest score in the class is: {marks}")

# Exercise 5.3

#1st Method
value = 0
for x in range(2,101,2):
    value += x
print(value)
    
#2nd Method
value = 0
for x in range(0,101):
    if x % 2 ==0:
        value += x
print(value)

#Exercise 5.4 - FizzBuzz

for x in range(1,101):
    if x % 3 == 0 and x % 5 ==0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)

















