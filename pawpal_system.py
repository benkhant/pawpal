from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class Task:
    title: str
    duration_minutes: int
    priority: str
    description: str = ""
    preferred_time: str = ""
    frequency: str = "daily"
    required: bool = False
    completed: bool = False

    def is_high_priority(self) -> bool:
        """Return True when the task priority is high."""
        return self.priority.lower() == "high"

    def mark_complete(self) -> None:
        """Mark this task as completed."""
        self.completed = True

    def reset_completion(self) -> None:
        """Reset completion status."""
        self.completed = False


@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to this pet's task list."""
        self.tasks.append(task)

    def remove_task(self, task_title: str) -> None:
        """Remove a task by title from this pet's task list."""
        self.tasks = [t for t in self.tasks if t.title != task_title]

    def get_tasks(self) -> List[Task]:
        """Return all tasks for this pet."""
        return self.tasks

    def get_incomplete_tasks(self) -> List[Task]:
        """Return only incomplete tasks for this pet."""
        return [t for t in self.tasks if not t.completed]


@dataclass
class Owner:
    name: str
    available_minutes: int
    preferences: List[str] = field(default_factory=list)
    pets: List[Pet] = field(default_factory=list)

    def add_preference(self, pref: str) -> None:
        """Add a planning preference for this owner."""
        if pref not in self.preferences:
            self.preferences.append(pref)

    def update_available_minutes(self, minutes: int) -> None:
        """Update daily available minutes for planning."""
        self.available_minutes = max(0, minutes)

    def add_pet(self, pet: Pet) -> None:
        """Attach a pet profile to this owner."""
        if pet not in self.pets:
            self.pets.append(pet)

    def remove_pet(self, pet_name: str) -> None:
        """Remove a pet profile by name."""
        self.pets = [p for p in self.pets if p.name != pet_name]

    def get_all_incomplete_tasks(self) -> List[Task]:
        """Retrieve all incomplete tasks from all pets owned by this owner."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.get_incomplete_tasks())
        return all_tasks

    def get_pets(self) -> List[Pet]:
        """Return list of all pets owned by this owner."""
        return self.pets


class Scheduler:
    def get_all_tasks_for_owner(self, owner: Owner) -> List[Task]:
        """Helper: query owner for all tasks across all owned pets."""
        return owner.get_all_incomplete_tasks()

    def build_daily_plan(self, owner: Owner, pet: Pet = None) -> List[Task]:
        """Build an ordered daily plan ranked by priority and owner constraints."""
        if pet:
            tasks = pet.get_incomplete_tasks()
        else:
            tasks = self.get_all_tasks_for_owner(owner)

        # Rank tasks and return ordered plan
        return self.rank_tasks(tasks, owner)

    def rank_tasks(self, tasks: List[Task], owner: Owner) -> List[Task]:
        """Return tasks ordered by score so scoring/sorting is centralized."""
        if not tasks:
            return []
        
        # Score each task and sort by score descending
        scored_tasks = [(task, self.score_task(task, owner)) for task in tasks]
        scored_tasks.sort(key=lambda x: x[1], reverse=True)
        return [task for task, score in scored_tasks]

    def score_task(self, task: Task, owner: Owner) -> int:
        """Calculate a ranking score based on priority, required status, and available time."""
        score = 0
        
        # Priority-based scoring
        if task.is_high_priority():
            score += 100
        elif task.priority.lower() == "medium":
            score += 50
        else:
            score += 10
        
        # Required tasks get a bonus
        if task.required:
            score += 50
        
        # Prefer tasks that fit available time
        if task.duration_minutes <= owner.available_minutes:
            score += 20
        
        return score

    def explain_plan(self, plan: List[Task]) -> str:
        """Return a human-readable explanation for the generated plan."""
        if not plan:
            return "No tasks scheduled for today."
        
        explanation = "Today's Plan:\n" + "-" * 40 + "\n"
        total_minutes = 0
        
        for i, task in enumerate(plan, 1):
            priority_str = task.priority.upper() if task.priority else "NORMAL"
            explanation += f"{i}. {task.title}\n"
            explanation += f"   Duration: {task.duration_minutes} min | Priority: {priority_str}\n"
            if task.description:
                explanation += f"   {task.description}\n"
            total_minutes += task.duration_minutes
        
        explanation += "-" * 40 + "\n"
        explanation += f"Total Time: {total_minutes} minutes\n"
        return explanation
