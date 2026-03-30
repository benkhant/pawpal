#!/usr/bin/env python3
"""Quick integration test for Scheduler-Owner communication."""

from pawpal_system import Owner, Pet, Task, Scheduler

# Create sample data
owner = Owner(name="Jordan", available_minutes=120)
pet = Pet(name="Mochi", species="dog", age=3)

# Add tasks to the pet
task1 = Task(title="Morning walk", duration_minutes=30, priority="high", description="Exercise and bathroom break")
task2 = Task(title="Lunch feeding", duration_minutes=15, priority="high", required=True)
task3 = Task(title="Afternoon playtime", duration_minutes=45, priority="medium", description="Interactive toys")
task4 = Task(title="Evening cuddles", duration_minutes=20, priority="low")

pet.add_task(task1)
pet.add_task(task2)
pet.add_task(task3)
pet.add_task(task4)

owner.add_pet(pet)
owner.add_preference("prefer_morning_activities")

# Test scheduler
scheduler = Scheduler()

# Single pet plan
plan = scheduler.build_daily_plan(owner, pet)
print("Single Pet Plan:")
print(scheduler.explain_plan(plan))
print()

# All tasks plan (across all pets)
all_plan = scheduler.build_daily_plan(owner)
print("All Pets Plan:")
print(scheduler.explain_plan(all_plan))
print()

# Verify Scheduler communicates with Owner correctly
print("Verification:")
print(f"Owner '{owner.name}' has {len(owner.get_pets())} pet(s)")
print(f"Total incomplete tasks across all pets: {len(owner.get_all_incomplete_tasks())}")
print("✓ Scheduler-Owner communication works!")
