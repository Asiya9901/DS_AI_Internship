student=input("Enter student name:")

marks=[]
while True:
    ip=(input("Enter your marks and type 'done' to finish: "))
    if ip=="done":
        break
    marks.append(int(ip))
print("avg of marks is",(sum(marks)/len(marks)))
print("marks",marks)
def grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "Fail"
print("Grade:",grade(sum(marks)/len(marks)))