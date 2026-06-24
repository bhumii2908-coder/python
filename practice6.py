# mange a to do list
# create a to do list to keep track of tasks
to_do_list=["learning lesson of coding","learning english","coching classes","watch youtube channle"]
# adding to task
to_do_list.append("house work")
to_do_list.append("house cleaning")

# removinga complete task
to_do_list.remove("house cleaning")

# checking if a task is in the list
if "learing english" in to_do_list:
    print("don't forget to learning english")
    
print("to do list remaining")
for task in to_do_list:
    print(f"-{task}")