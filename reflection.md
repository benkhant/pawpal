# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

I am designing PawPal+, a pet care app, around four main classes: `Owner`, `Pet`, `Task`, and `Scheduler`.

I used Copilot to draft this Mermaid.js class diagram from my brainstormed attributes and methods:

```mermaid
classDiagram
	class Owner {
		+String name
		+int availableMinutes
		+List~String~ preferences
		+addPreference(pref)
		+updateAvailableMinutes(minutes)
	}

	class Pet {
		+String name
		+String species
		+int age
		+List~Task~ tasks
		+addTask(task)
		+removeTask(taskTitle)
	}

	class Task {
		+String title
		+int durationMinutes
		+String priority
		+String preferredTime
		+bool required
		+isHighPriority() bool
	}

	class Scheduler {
		+buildDailyPlan(owner, pet) List~Task~
		+scoreTask(task, owner) int
		+explainPlan(plan) String
	}

	Owner "1" --> "1..*" Pet : manages
	Pet "1" --> "0..*" Task : has
	Scheduler ..> Owner : reads constraints
	Scheduler ..> Pet : reads tasks
	Scheduler ..> Task : prioritizes
```

**Core user actions**

- A user should be able to add and manage pet profiles so the system knows which pet needs care and what kind of care is appropriate.
- A user should be able to create and prioritize daily care tasks (like feeding, walks, medication, or playtime) with time estimates.
- A user should be able to generate and view today’s plan in order, so they can quickly see what to do next and when.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
