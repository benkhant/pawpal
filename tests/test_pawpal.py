import pytest
from pawpal_system import Task, Pet, Owner, Scheduler


class TestTaskCompletion:
    """Test that task completion tracking works correctly."""
    
    def test_mark_complete_changes_status(self):
        """Verify that calling mark_complete() changes the task's completed status."""
        task = Task(
            title="Feed the dog",
            duration_minutes=15,
            priority="high",
            description="Morning meal"
        )
        
        # Initially, the task should be incomplete
        assert task.completed is False, "Task should start as incomplete"
        
        # Mark it complete
        task.mark_complete()
        
        # Now it should be marked complete
        assert task.completed is True, "Task should be marked as complete after calling mark_complete()"
    
    def test_reset_completion_clears_status(self):
        """Verify that reset_completion() clears the completed status."""
        task = Task(
            title="Walk the dog",
            duration_minutes=30,
            priority="high"
        )
        
        # Mark complete, then reset
        task.mark_complete()
        assert task.completed is True
        
        task.reset_completion()
        
        # Should now be incomplete again
        assert task.completed is False, "Task should be incomplete after reset_completion()"


class TestTaskAddition:
    """Test that adding and managing tasks on pets works correctly."""
    
    def test_adding_task_increases_pet_task_count(self):
        """Verify that adding a task to a Pet increases that pet's task count."""
        pet = Pet(name="Buddy", species="dog", age=5)
        
        # Initially, the pet should have no tasks
        assert len(pet.get_tasks()) == 0, "Pet should start with no tasks"
        
        # Add a task
        task = Task(
            title="Feed the dog",
            duration_minutes=15,
            priority="high",
            required=True
        )
        pet.add_task(task)
        
        # Now the pet should have one task
        assert len(pet.get_tasks()) == 1, "Pet should have 1 task after adding one"
        
        # Add another task
        task2 = Task(
            title="Walk the dog",
            duration_minutes=30,
            priority="high"
        )
        pet.add_task(task2)
        
        # Now the pet should have two tasks
        assert len(pet.get_tasks()) == 2, "Pet should have 2 tasks after adding two"
    
    def test_removing_task_decreases_pet_task_count(self):
        """Verify that removing a task decreases the task count."""
        pet = Pet(name="Whiskers", species="cat", age=3)
        
        # Add two tasks
        task1 = Task(title="Feed the cat", duration_minutes=10, priority="high", required=True)
        task2 = Task(title="Play with the cat", duration_minutes=20, priority="medium")
        
        pet.add_task(task1)
        pet.add_task(task2)
        
        assert len(pet.get_tasks()) == 2
        
        # Remove the first task
        pet.remove_task("Feed the cat")
        
        # Should now have only one task
        assert len(pet.get_tasks()) == 1, "Pet should have 1 task after removing one"
        
        # The remaining task should be the second one
        assert pet.get_tasks()[0].title == "Play with the cat"
