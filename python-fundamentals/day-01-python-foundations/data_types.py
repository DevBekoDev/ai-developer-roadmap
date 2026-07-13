# Python variable and basic data types

name: str = "Abubakr Nasir"
age: int = 25
height: float = 1.83
is_learning_ai: bool = True

skills: list[str] = ["python", "flutter", "git"]
profile: dict[str, object] = {
    "name" : name,
    "age" : age,
    "skills" : skills
}

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Learning Ai:", is_learning_ai)
print("Profile:", profile)

print("\nData Types:")
print(type(name))
print(type(age))
print(type(height))
print(type(is_learning_ai))
print(type(skills))
print(type(profile))

