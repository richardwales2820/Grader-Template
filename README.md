# Speed Grader Feedback Template
Create, update, and use grading feedback templates online for speed grading sessions

## Features/Idea List
### MVP
- Home page with list of assignments, linking to their own respective page.
- Assignment page has feedback template with rubric-style sheet. Checking off something will automatically add text to a comment sheet pertaining to the relevant material (Just like eustis grader).
- Items in template can be created, updated, modified (add roles? Professor only one to be able to delete?)
- Point values set so that a final score value can be updated as points are given/taken away.

### Down the Road
- Have code from student open in window adjacent to the template for easy viewing (Easier than manually opening in two separate windows?)
- Use Canvas API to automatically post the final comments to the student's assignment submission, along with updating their score.

## Thoughts

- Models
    - Assignment Table
        - Unique ID
        - Name
        - Total Score
        - Instructions for the assignment grading
    - Feedback Comment Table
        - Unique ID
        - Assignment ID that it pertains to
        - How many points this comment removes from final score
        - The actual comment that should appear in the final message