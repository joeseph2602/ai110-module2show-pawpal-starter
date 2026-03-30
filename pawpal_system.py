from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime
from typing import Optional, List


class HealthStatus(Enum):
    """Enumeration for pet health status levels."""
    EXCELLENT = "Excellent"
    GOOD = "Good"
    FAIR = "Fair"
    POOR = "Poor"
    CRITICAL = "Critical"


class TaskStatus(Enum):
    """Enumeration for task status."""
    PENDING = "Pending"
    COMPLETED = "Completed"


@dataclass
class Task:
    """Represents a single pet care task."""
    id: int
    description: str
    time: str
    frequency: str
    status: TaskStatus = TaskStatus.PENDING

    def mark_complete(self) -> None:
        """Mark the task as completed."""
        self.status = TaskStatus.COMPLETED

    def get_details(self) -> dict:
        """Return task details."""
        return {
            "id": self.id,
            "description": self.description,
            "time": self.time,
            "frequency": self.frequency,
            "status": self.status.value
        }


@dataclass
class Pet:
    """Stores pet details and a list of tasks."""
    id: int
    name: str
    species: str
    age: int
    weight: float
    health: HealthStatus = HealthStatus.GOOD
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to the pet."""
        self.tasks.append(task)

    def remove_task(self, task_id: int) -> None:
        """Remove a task by id."""
        self.tasks = [task for task in self.tasks if task.id != task_id]

    def view_details(self) -> dict:
        """Return pet details."""
        return {
            "id": self.id,
            "name": self.name,
            "species": self.species,
            "age": self.age,
            "weight": self.weight,
            "health": self.health.value,
            "task_count": len(self.tasks)
        }


@dataclass
class Owner:
    """Manages multiple pets and provides access to all their tasks."""
    id: int
    name: str
    email: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to the owner."""
        self.pets.append(pet)

    def remove_pet(self, pet_id: int) -> None:
        """Remove a pet by id."""
        self.pets = [pet for pet in self.pets if pet.id != pet_id]

    def get_all_tasks(self) -> List[Task]:
        """Get all tasks from all pets."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.tasks)
        return all_tasks


@dataclass
class Scheduler:
    """Organizes and manages tasks across all pets."""
    owner: Owner

    def get_all_tasks(self) -> List[Task]:
        """Retrieve all tasks from the owner's pets."""
        return self.owner.get_all_tasks()

    def get_pending_tasks(self) -> List[Task]:
        """Return only pending tasks."""
        return [task for task in self.get_all_tasks() if task.status == TaskStatus.PENDING]

    def get_completed_tasks(self) -> List[Task]:
        """Return only completed tasks."""
        return [task for task in self.get_all_tasks() if task.status == TaskStatus.COMPLETED]

    def mark_task_complete(self, task_id: int) -> bool:
        """Mark a task complete by id."""
        for task in self.get_all_tasks():
            if task.id == task_id:
                task.mark_complete()
                return True
        return False