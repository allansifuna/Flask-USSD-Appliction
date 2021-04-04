from ..models import Grade, Subject
from somo import create_app
app = create_app()
app.app_context().push()
grds = Grade.query.all()
grades = {}
for i, j in enumerate(grds):
    grades[i + 1] = j.name
subs = Subject.query.all()
subjects = {}
for i, j in enumerate(subs):
    subjects[i + 1] = j.name
# grades = {
#     1: "One",
#     2: "Two",
#     3: "Three",
#     4: "Four",
#     5: "Five",
#     6: "Six",
#     7: "Seven",
#     8: "Eight"
# }

# subjects = {
#     1: "Mathematics",
#     2: "English",
#     3: "Kiswahili",
#     4: "Science",
#     5: "Social Studies",
#     6: "CRE",
#     7: "IRE",
# }
