from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class Task:
    title: str
    duration_minutes: int
    priority: str
    preferred_time: str = ""
    required: bool = False

    def is_high_priority(self) -> bool:
        """Return True when the task priority is high."""
        raise NotImplementedError


@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to this pet's task list."""
        raise NotImplementedError

    def remove_task(self, task_title: str) -> None:
        """Remove a task by title from this pet's task list."""
        raise NotImplementedError


@dataclass
class Owner:
    name: str
    available_minutes: int
    preferences: List[str] = field(default_factory=list)

    def add_preference(self, pref: str) -> None:
        """Add a planning preference for this owner."""
        raise NotImplementedError

    def update_available_minutes(self, minutes: int) -> None:
        """Update daily available minutes for planning."""
        raise NotImplementedError


class Scheduler:
    def build_daily_plan(self, owner: Owner, pet: Pet) -> List[Task]:
        """Build an ordered daily plan from owner constraints and pet tasks."""
        raise NotImplementedError

    def score_task(self, task: Task, owner: Owner) -> int:
        """Calculate a ranking score for a task."""
        raise NotImplementedError

    def explain_plan(self, plan: List[Task]) -> str:
        """Return a human-readable explanation for the generated plan."""
        raise NotImplementedError
