from collections import defaultdict

# --------------------------------------------
# LMS DATA
# --------------------------------------------

students = [
    {"name": "Rahul", "course": "Python Full Stack"},
    {"name": "Sneha", "course": "Python Full Stack"},
    {"name": "Arjun", "course": "Data Science"},
    {"name": "Meena", "course": "Data Science"},
    {"name": "Kiran", "course": "Django"},
]

assignments = [
    {"title": "Variables Task", "subject": "Python"},
    {"title": "Loops Practice", "subject": "Python"},
    {"title": "HTML Page", "subject": "Frontend"},
    {"title": "CSS Flexbox", "subject": "Frontend"},
    {"title": "SQL Queries", "subject": "Database"},
]

notifications = [
    {"message": "Assignment Uploaded", "type": "Assignment"},
    {"message": "New Course Added", "type": "Course"},
    {"message": "Exam Tomorrow", "type": "Exam"},
    {"message": "Project Submission Date", "type": "Assignment"},
    {"message": "Holiday Announcement", "type": "General"},
]


# --------------------------------------------
# 1. GROUPING STUDENTS BY COURSE
# --------------------------------------------

course_students = defaultdict(list)

for student in students:
    course_students[student["course"]].append(student["name"])
print(course_students)

print("------ Students Grouped By Course ------")

for course, student_list in course_students.items():
    print(f"{course} --> {student_list}")
    # pass


# --------------------------------------------
# 2. GROUPING ASSIGNMENTS BY SUBJECT
# --------------------------------------------
"""
subject_assignments = defaultdict(list)

for assignment in assignments:
    subject_assignments[assignment["subject"]].append(assignment["title"])

print("\n------ Assignments Grouped By Subject ------")

for subject, assignment_list in subject_assignments.items():
    print(f"{subject} --> {assignment_list}")


# --------------------------------------------
# 3. CATEGORIZING NOTIFICATIONS
# --------------------------------------------

notification_category = defaultdict(list)

for notice in notifications:
    notification_category[notice["type"]].append(notice["message"])

print("\n------ Notifications Categorized ------")

for category, messages in notification_category.items():
    print(f"{category} --> {messages}")
"""
