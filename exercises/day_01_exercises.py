# Exercise 1: User Profile Generator

name: str = input("Enter your name: ")
age: int = int(input("Enter your age: "))
career_goals: str = input("Enter your career goals: ")
hours_per_day: float = float(input("How many hours can you study daily? "))

profile: dict[str, object] = {
    "name": name,
    "age": age,
    "career_goals": career_goals,
    "hours_per_day": hours_per_day
}

print("\n--- Developer Profile ---")
print(f"Name: {profile["name"]}")
print(f"Age: {profile["age"]}")
print(f"Career Goals: {profile["career_goals"]}")
print(f"Daily study time: {profile["hours_per_day"]}")

# Exercise 2: Weekly Study Calculator

daily_hours: float = float(input("How many hours will you study each day? "))
study_days: int = int(input("How many days will you study each week? "))

weekly_hours: float = daily_hours * study_days
monthly_hours: float = weekly_hours * 4

print(f"\nWeekly study time: {weekly_hours} hours")
print(f"Estimated monthly study time: {monthly_hours} hours")

if weekly_hours >= 30:
    print("Commitment level: Intensive")
elif weekly_hours >= 15:
    print("Commitment level: Consistent")
elif weekly_hours >= 7:
    print("Commitment level: Moderate")
else:
    print("Commitment level: You should increase your study time")


# Exercise 3: Skills Tracker

print("\n--- Skills Tracker ---")
skill_input: str= input("Enter your skills seperated by commas: ")

skill_list: list[str] = []

for skill in skill_input.split(","):
    cleaned_skill = skill.strip().title()

    if cleaned_skill:
        skill_list.append(cleaned_skill)

# Sets automatically remove duplicates from lists

unique_skills: set[str] = set(skill_list)

print("\nYour skills:", skill_list)
print("Unique skills:", unique_skills)
print(f"Number of entered skills: {len(skill_list)}")
print(f"Number of unique skills: {len(unique_skills)}")

required_ai_skills: set[str] = {
    "Python",
    "Git",
    "Sql",
    "Machine Learning",
}

matching_skills: set[str] = unique_skills.intersection(required_ai_skills)
missing_skills: set[str] = required_ai_skills.difference(unique_skills)

print("\nAI roadmap skills you already have:", matching_skills)
print("AI roadmap skils to learn:", missing_skills)

# Exercise 4: Freelance Earnings Calculator

print("\n--- Freelance Earnings Calcuator ---")

hourly_rate: float = float(input("Enter your hourly rate in USD: "))
hours_worked: float = float(input("Enter number of hours worked: "))
platform_fee_percentage: float = float(input("Enter the platform fee percentage: "))

gross_earnings = hourly_rate * hours_worked
platform_fee = gross_earnings * platform_fee_percentage / 100
net_earnings = gross_earnings - platform_fee

print("\n--- Earnings Summery ---")
print(f"Gross earnings: ${gross_earnings:.2f}")
print(f"Platform fee: ${platform_fee:.2f}")
print(f"Net Earnings: ${net_earnings:.2f}")

if net_earnings >= 1000:
    print("Earnings level: Excellent project")
elif net_earnings >= 500:
    print("Earnings level: Good Project")
elif net_earnings >= 100:
    print("Earnings level: Small project")
else:
    print("Earnings level: Micro project")

# Exercise 5: AI Job Readiness Checker

print("\n--- AI Job Readiness Checker ---")

skill_scores: dict[str,int] = {
    "Python": int(input("Rate your python skill from 0 to 10: ")),
    "Git": int(input("Rate your Git skill from 0 to 10: ")),
    "SQL": int(input("Rate your SQL skill from 0 to 10: ")),
    "Machine Learning": int(input("Rate your Machine Learning skill from 0 to 10: "))
}

total_score: int = sum(skill_scores.values())
number_of_skills: int = len(skill_scores)
average_score: float = total_score / number_of_skills

strong_skills : list[str] = []
skills_to_improve : list[str] = []

for skill, score in skill_scores.items():
    if score > 7:
        strong_skills.append(skill)
    else:
        skills_to_improve.append(skill)

print("\n--- Readiness Report ---")

for skill, score in skill_scores.items():
    print(f"{skill}L {score}/10")

print(f"Avergae score: {average_score:.1f}/10")
print("Strong skills:",strong_skills)
print("Skills to improve:", skills_to_improve)

if average_score >= 8:
    print("Readiness level: Ready to apply for AI jobs")
elif average_score >= 6:
    print("Readiness level: Almost ready - continue building projects")
elif average_score >= 4:
    print("Readiness level: Developing - strengthen your foundations")
else:
    print("Readiness level: Beginner - continue learning step by step")