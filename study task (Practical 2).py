# study task (Practical 2)
study_dict=["revise your Functional english lecture today","revise Computer Fundamental lecture today","practice coding today"]
day_task=[]
for i in study_dict:
    task=input(f"Did you {i} ? (y or n) ")
    day_task.append(task)
count_y_n=day_task.count("n")
if count_y_n>0:
    print(f"{count_y_n} task remaining")
else:
    print(f"Congratulations you completed your all task")