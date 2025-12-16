#comprehension example
students = [
    {"name": "Alice", "scores": [85, 90, 88]},
    {"name": "Bob", "scores": [70, None, 75]},
    {"name": "Charlie", "scores": [95, 92, 93]},
    {"name": "David", "scores": [60, 65, 58]},
    {"name": "Eva", "scores": [88, 90, None]},
]
cleaned_scores = {
    s["name"]: [score for score in s["scores"] if score is not None]
    for s in students
}

print(cleaned_scores)

#datatype
age = 25
years_of_experience = 3

total_years = age + years_of_experience
print("Total years:", total_years)

height = 5.9
weight = 72.5

bmi = weight / (height ** 2)
print("BMI:", round(bmi, 2))

#for loop
numbers = [10, 15, 20, 25, 30]

for num in numbers:
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")

#Dictionary example
# Simple dictionary
student = {
    "id": 101,
    "name": "Alice",
    "age": 21,
    "course": "Computer Science"
}

print(student)


