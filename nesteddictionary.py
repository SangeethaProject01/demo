#nested dictionary

##student={
##"student_1":{
##    "name":"mugilan",
##    "year":18,
##    "course":"python"
##    },
##"student_2":{
##    "name":"thiru murugan",
##    "year":18,
##    "course":"python"
##    }
##    }
##
##print(student)
#seperate dictionary

##student1={"name":"jai","age":22}
##student2={"name":"kishore","age":22}
##student3={"name":"kumaran","age":22}
##
##student={
##"student1":student1,
##"student2":student2,
##"student3":student3
##
##    }
##print(student)



##x = ('course1', 'course2', 'course3')
##y = "python"
##
##thisdict = dict.fromkeys(x, y)
##
##
##print(thisdict)


tasks_with_answers = {
    "Task 1": {
        "Description": "Calculate the sum of two numbers",
        "Inputs": {
            "a": 5,
            "b": 3
        },
        "Answer": 5 + 3
    },
    "Task 2": {
        "Description": "Find the maximum of two numbers",
        "Inputs": {
            "a": 10,
            "b": 15
        },
        "Answer": max(10, 15)
    },
    }

##print(tasks_with_answers)
for task, details in tasks_with_answers.items():
    print(f"{task}:")
    for key, value in details.items():
        print(f"  {key}: {value}")
    print()
