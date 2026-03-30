# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

-- The initial UML design included two classes: Pet and Task. The pet class stores information like name, species, age, weight, and health, and incldes methods to update and view details. The task class represents pet related tasks. 
**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

-- Created a relationship between the class pet and the class task.

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

The scheduler considers **time constraints** (detecting when tasks are scheduled at the same time) and **pet relationships** (distinguishing same-pet vs cross-pet conflicts).

Time conflicts mattered most because you physically cannot do two tasks simultaneously, especially for pet care activities.
**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

-- The scheduler only checks for exact time matches (e.g., two tasks both scheduled at "8:00 AM") rather than detecting overlapping time durations (e.g., one task from 8:00-8:30 AM overlapping with another from 8:15-8:45 AM). This tradeoff is reasonable because the current system uses simple time strings without duration information, making exact matching more reliable and easier to implement. For a pet care scheduling system focused on daily routines, exact time conflicts are the most common and critical issues to detect.

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
