"""Basic Python function examples."""

def greet_user(name:str) -> str:
    """Return a personalzied greeting."""
    return f"Hello, {name}! Welcome to Day 2."

def calculate_weekly_hours(
        daily_hours: float,
        study_days: int,
) -> float:
    """Calculate the total number of study hours per week."""
    return daily_hours * study_days

user_name: str = input("Enter your name: ")
daily_hours: float = float(input("Daily study hours: "))
study_days: int = int(input("Study days per weeek: "))

greeting: str = greet_user(user_name)
weekly_hours: float = calculate_weekly_hours(daily_hours,study_days)

print(greeting)
print(f"You will study {weekly_hours:.1f} hours per week")

def create_learning_plan(
        topic: str,
        days: int = 7,
        hours_per_day: float = 2.0,
) ->str:
    """Create a simple learning-plan summary."""
    total_hours: float = days * hours_per_day

    return(
        f"Topic: {topic}\n"
        f"Duration: {days} days\n"
        f"Daily study time: {hours_per_day} hours\n"
        f"Total study time: {total_hours} hours"
    )

print("\n--- Learning Plan ---")

plan: str = create_learning_plan(
    topic="Python Functions",
    days=5,
    hours_per_day=3
)

print(plan)


"""Reusable utility functions for common calculations."""

def caculate_net_earnings(
        hourly_rate: float,
        hours_worked: float,
        platform_fee_percent: float = 10.0,
) -> float:
     """Calculate earnings after deducting a platform fee."""
     gross_earnings: float = hourly_rate * hours_worked
     platform_fee: float = gross_earnings * platform_fee_percent / 100
     
     return gross_earnings - platform_fee


rate: float = float(input("Enter your hours rate: "))
hours: float = float(input("Enter hours worked: "))
fee: float = float(input("Enter platfrom fee percent: "))

net_earnings: float = caculate_net_earnings(hourly_rate=rate, hours_worked=hours, platform_fee_percent=fee)

print(f"Net earnings: ${net_earnings:.2f}")


"""Calculate Progress"""

def calculate_progress(
        completed_hours: float,
        target_hours: float
) -> float:
    """Calculate study progress"""
    if target_hours < 0:
        return 0.0
    
    progress: float = completed_hours / target_hours * 100

    return min(progress, 100.0)

completed: float = float(input("Enter completed study hours: "))
target: float = float(input("Enter target study hours: "))

progress_percentage: float = calculate_progress(completed_hours=completed, target_hours=target)

print("\n--- Prgoress ---")
print(f"Prgoress: {progress_percentage:.1f}%")

if progress_percentage >=100:
    print("Goal completed!")
elif progress_percentage >=75:
    print("You are close to completing your goal.")
elif progress_percentage >= 50:
    print("You are halfway there.")
else:
    print("Keep going.")


"""Calculate skill level."""

def classify_skill_level(score:int) -> str:
    """Determain the skill level based on scores"""
    if score >10 or score <0:
        return "Invalid score"
    
    if score>=8:
        return "Advanced"
    elif score >= 6:
        return "Intermediate"
    elif score >= 3:
        return "Beginner"
    else:
        return "Needs improvment"
    
print("\n--- Skil-level Classifier---")

skill_name: str = input("Enter skill name: ")
skill_score: int = int(input("Enter your skill score from 0 to 10: "))

skill_level: str = classify_skill_level(skill_score)

print(f"{skill_name}: {skill_level}")


"""Calculate Average skill score"""

def claculate_average(scores:list[float]) -> float:
    """Calculate the average of a list of scores."""
    if not scores:
        return
    
    return sum(scores) / len(scores)

print ("\n--- Average Score Caluclator")

score_input: str = input("Enter your scores seperated by commas: ")

score_list: list[float] = []

for score in score_input.split(","):
    cleaned_score: str = score.strip()

    if cleaned_score:
        score_list.append(float(cleaned_score))

average_score: float = claculate_average(scores=score_list)
print(f"Scores: {score_list}")
print(f"Average score: {average_score:.2f}")


def find_missing_skills(
        current_skills: set[str],
        required_skills: set[str],
) -> set[str]:
    """Return the required skills that the user does not have."""
    return required_skills.difference(current_skills)

print("\n--- Missing skills Finder ---")

current_skils_input: str = input("Enter your current skils separated by commas: ")
required_skills_input: str = input("Enter the requied skills separated by commas: ")

current_skills: set[str] = {
    skill.strip().title()
    for skill in current_skils_input.split(",")
    if skill.strip()
    
}

required_skills: set[str] = {
    skill.strip().title()
    for skill in required_skills_input.split(",")
    if skill.strip()
}

missing_skills: set[str] = find_missing_skills(current_skills=current_skills,required_skills=required_skills)

print(f"Current skills: {sorted(current_skills)}")
print(f"Required skills: {sorted(required_skills)}")

if missing_skills:
    print(f"Skills to learn: {sorted(missing_skills)}")
else:
    print("You already have all the required skills!")