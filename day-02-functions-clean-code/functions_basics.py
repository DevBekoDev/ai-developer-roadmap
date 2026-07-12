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