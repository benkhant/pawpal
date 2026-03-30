from pawpal_system import Task, Pet, Owner, Scheduler

def main():
    # Create tasks intentionally out of chronological order.
    task1 = Task(
        title="Feed the dog",
        description="Give the dog its morning meal",
        duration_minutes=15,
        priority="high",
        preferred_time="08:30",
        required=True,
    )
    task2 = Task(
        title="Walk the dog",
        description="Take the dog for a 30-minute walk",
        duration_minutes=30,
        priority="high",
        preferred_time="07:00",
    )
    task5 = Task(
        title="Brush the dog",
        description="Quick brushing session",
        duration_minutes=10,
        priority="low",
        preferred_time="07:00",
    )
    task3 = Task(
        title="Play with the cat",
        description="Spend 20 minutes playing with the cat",
        duration_minutes=20,
        priority="medium",
        preferred_time="18:00",
    )
    task4 = Task(
        title="Clean litter box",
        description="Quick litter refresh",
        duration_minutes=10,
        priority="medium",
        preferred_time="08:30",
    )

    # Create pets and assign tasks
    dog = Pet(name="Buddy", species="Dog", age=5)
    cat = Pet(name="Whiskers", species="Cat", age=3)

    dog.add_task(task1)
    dog.add_task(task2)
    dog.add_task(task5)
    cat.add_task(task3)
    cat.add_task(task4)

    # Mark one task complete to demonstrate status filtering.
    task3.mark_complete()

    # Create an owner and add pets
    owner = Owner(name="Alice", available_minutes=120)
    owner.add_pet(dog)
    owner.add_pet(cat)

    # Generate today's schedule using the Scheduler
    scheduler = Scheduler()
    schedule = scheduler.build_daily_plan(owner)
    all_tasks = owner.get_all_tasks()
    sorted_tasks = scheduler.sort_by_time(all_tasks)
    buddy_incomplete = scheduler.filter_tasks(owner, completed=False, pet_name="Buddy")
    completed_tasks = scheduler.filter_tasks(owner, completed=True)
    conflict_warnings = scheduler.detect_time_conflicts(owner)
    
    # Print the readable schedule
    print(f"\n{'='*50}")
    print(f"PawPal+ Daily Plan for {owner.name}")
    print(f"{'='*50}")
    print(scheduler.explain_plan(schedule))

    print(f"\n{'='*50}")
    print("Tasks Sorted By Time")
    print(f"{'='*50}")
    for task in sorted_tasks:
        print(f"- {task.preferred_time or 'N/A'} | {task.title} | completed={task.completed}")

    print(f"\n{'='*50}")
    print("Filtered: Incomplete Tasks For Buddy")
    print(f"{'='*50}")
    for task in buddy_incomplete:
        print(f"- {task.title} ({task.preferred_time or 'N/A'})")

    print(f"\n{'='*50}")
    print("Filtered: Completed Tasks (All Pets)")
    print(f"{'='*50}")
    for task in completed_tasks:
        print(f"- {task.title} ({task.preferred_time or 'N/A'})")

    print(f"\n{'='*50}")
    print("Conflict Warnings")
    print(f"{'='*50}")
    if not conflict_warnings:
        print("No scheduling conflicts detected.")
    else:
        for warning in conflict_warnings:
            print(f"- {warning}")

if __name__ == "__main__":
    main()