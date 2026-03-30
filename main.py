from pawpal_system import Task, Pet, Owner, Scheduler

def main():
    # Create some tasks with different priorities
    task1 = Task(title="Feed the dog", description="Give the dog its morning meal", duration_minutes=15, priority="high", required=True)
    task2 = Task(title="Walk the dog", description="Take the dog for a 30-minute walk", duration_minutes=30, priority="high")
    task3 = Task(title="Play with the cat", description="Spend 20 minutes playing with the cat", duration_minutes=20, priority="medium")

    # Create pets and assign tasks
    dog = Pet(name="Buddy", species="Dog", age=5)
    cat = Pet(name="Whiskers", species="Cat", age=3)

    dog.add_task(task1)
    dog.add_task(task2)
    cat.add_task(task3)

    # Create an owner and add pets
    owner = Owner(name="Alice", available_minutes=120)
    owner.add_pet(dog)
    owner.add_pet(cat)

    # Generate today's schedule using the Scheduler
    scheduler = Scheduler()
    schedule = scheduler.build_daily_plan(owner)
    
    # Print the readable schedule
    print(f"\n{'='*50}")
    print(f"PawPal+ Daily Plan for {owner.name}")
    print(f"{'='*50}")
    print(scheduler.explain_plan(schedule))

if __name__ == "__main__":
    main()