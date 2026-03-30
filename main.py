from pawpal_system import Owner, Pet, Task, Scheduler, TaskStatus

# Create owner
owner = Owner(id=1, name="Joeseph", email="joe@email.com")

# Create pets
pet1 = Pet(id=1, name="Buddy", species="Dog", age=3, weight=25.0)
pet2 = Pet(id=2, name="Milo", species="Cat", age=2, weight=10.0)

# Add pets to owner
owner.add_pet(pet1)
owner.add_pet(pet2)

# Create tasks
task1 = Task(id=1, description="Morning Walk", time="8:00 AM", frequency="Daily")
task2 = Task(id=2, description="Feed", time="12:00 PM", frequency="Daily")
task3 = Task(id=3, description="Vet Visit", time="3:00 PM", frequency="One-time")

# Assign tasks to pets
pet1.add_task(task1)
pet1.add_task(task2)
pet2.add_task(task3)

# Create scheduler
scheduler = Scheduler(owner)

# Print today's schedule
print("=== Today's Schedule ===")

for task in scheduler.get_all_tasks():
    print(f"{task.time} - {task.description} ({task.status.value})")