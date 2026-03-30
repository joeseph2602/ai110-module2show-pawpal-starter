import pytest
from datetime import datetime
from pawpal_system import Pet, Task, Owner, HealthStatus, TaskStatus


class TestPet:
    """Test cases for the Pet class."""

    def test_pet_creation_and_view_details(self):
        """Test creating a pet and viewing its details."""
        # Create a pet
        pet = Pet(
            id=1,
            name="Buddy",
            species="Dog",
            age=3,
            weight=25.5,
            health=HealthStatus.GOOD
        )

        # Verify pet attributes
        assert pet.id == 1
        assert pet.name == "Buddy"
        assert pet.species == "Dog"
        assert pet.age == 3
        assert pet.weight == 25.5
        assert pet.health == HealthStatus.GOOD

        # Test viewdetails method
        details = pet.viewdetails()
        assert details["name"] == "Buddy"
        assert details["species"] == "Dog"
        assert details["age"] == 3
        assert details["weight"] == 25.5
        assert details["health"] == "Good"
        assert details["tasks_count"] == 0

    def test_pet_validation(self):
        """Test that pet validation works correctly."""
        # Test negative age raises error
        with pytest.raises(ValueError, match="Age cannot be negative"):
            Pet(id=1, name="Test", species="Dog", age=-1, weight=10.0)

        # Test zero weight raises error
        with pytest.raises(ValueError, match="Weight must be positive"):
            Pet(id=1, name="Test", species="Dog", age=1, weight=0.0)

        # Test empty name raises error
        with pytest.raises(ValueError, match="Pet name cannot be empty"):
            Pet(id=1, name="", species="Dog", age=1, weight=10.0)


class TestTask:
    """Test cases for the Task class."""

    def test_task_creation_and_completion(self):
        """Test creating a task and marking it complete."""
        # Create a task
        task = Task(
            id=1,
            description="Take Buddy for a walk",
            pet_id=1,
            status=TaskStatus.PENDING
        )

        # Verify task attributes
        assert task.id == 1
        assert task.description == "Take Buddy for a walk"
        assert task.pet_id == 1
        assert task.status == TaskStatus.PENDING
        assert task.completed_at is None

        # Complete the task
        result = task.complete_task()
        assert "completed" in result
        assert task.status == TaskStatus.COMPLETED
        assert task.completed_at is not None

        # Verify completion timestamp is recent
        time_diff = datetime.now() - task.completed_at
        assert time_diff.seconds < 10  # Completed within last 10 seconds

    def test_task_validation(self):
        """Test that task validation works correctly."""
        # Test empty description raises error
        with pytest.raises(ValueError, match="Task description cannot be empty"):
            Task(id=1, description="")


class TestPetTaskRelationship:
    """Test cases for Pet-Task relationships."""

    def test_adding_task_increases_pet_task_count(self):
        """Test that adding a task to a pet increases the pet's task count."""
        # Create a pet
        pet = Pet(
            id=1,
            name="Max",
            species="Cat",
            age=2,
            weight=12.0,
            health=HealthStatus.EXCELLENT
        )

        # Initially no tasks
        assert len(pet.tasks) == 0
        details = pet.viewdetails()
        assert details["tasks_count"] == 0

        # Create and add a task
        task = Task(
            id=1,
            description="Feed Max breakfast",
            pet_id=None  # Will be set by add_task
        )

        pet.add_task(task)

        # Verify task was added and count increased
        assert len(pet.tasks) == 1
        assert pet.tasks[0].description == "Feed Max breakfast"
        assert pet.tasks[0].pet_id == 1  # Should be set to pet's id

        # Verify through viewdetails
        details = pet.viewdetails()
        assert details["tasks_count"] == 1

    def test_complete_task_changes_status(self):
        """Test that completing a task actually changes its status."""
        # Create a task
        task = Task(
            id=1,
            description="Walk the dog",
            status=TaskStatus.PENDING
        )

        # Verify initial status
        assert task.status == TaskStatus.PENDING
        assert task.completed_at is None

        # Complete the task
        result = task.complete_task()

        # Verify status changed and timestamp was set
        assert task.status == TaskStatus.COMPLETED
        assert task.completed_at is not None
        assert "completed" in result

        # Verify task details reflect completion
        task_details = task.get_details()
        assert task_details["status"] == "Completed"
        assert task_details["completed_at"] is not None
