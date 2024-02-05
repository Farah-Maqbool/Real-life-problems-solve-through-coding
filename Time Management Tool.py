#Time Management Tool
"""Time Management Tool: Develop a tool to track time spent on various activities. Use variables to 
store task names and durations. Write expressions to calculate total time spent on each task and 
identify areas for improvement."""
ideal_duration={"mobile":"1 hour","coding":"2 hour","arabic class":"1 video"}
task_duration={}

for i in range(3):
    task_name=input("Task name: ").lower()
    duration=input("Duration: ").lower()
    task_duration[task_name]=duration
complete_task={}
uncomplete_task={}
for key, values in ideal_duration.items():
    for key1, values1 in task_duration.items():
        if key==key1:
            if values==values1:
                complete_task[key1]=values1
            elif    values!=values1:
                uncomplete_task[key1]=values1
print("Task you complete in a specific duration") 
for key, values in complete_task.items():
    print(key,":",values)
print("A task you don't complete within a specific duration. You need improvement in these task") 
for key, values in uncomplete_task.items():
    print(key,":",values)
