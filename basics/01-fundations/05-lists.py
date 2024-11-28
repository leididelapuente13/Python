my_list = ["banana", "cherry", "strawberry", "coconut", "lemon"]

print(len(my_list))

if "kiwi" in my_list:
    print("Kiwi")

# insert an element in an specific index
my_list.insert(len(my_list), "kiwi")

# insert item at the end of the list
my_list.append("orange")
print(my_list)

# how to add a list, tuple, dictionaries inside another
tasks_day = ["commute", "work", "drink water", "code"]
tasks_night = ["commute", "rest", "eat", "work", "sleep"]
tasks_day.extend(tasks_night)
procrastination_tasks = ("scroll in twitter", "scroll in youtube")
tasks_day.extend(procrastination_tasks)
print(tasks_day)

# remove items
tasks_day.remove("scroll in youtube")

# remove by index
tasks_day.pop(len(tasks_day)-1)
print(tasks_day)

# remove last item
tasks_night.pop()

# remove first element
del tasks_night[0]

# clear list content
tasks_night.clear()

# delete all the list
del tasks_night

# loop a list
for task in tasks_day:
    print(task)

[print(task) for task in tasks_day]

# sort list
tasks_day.sort()
tasks_day.sort(reverse=True)
print(tasks_day)

# copy a list
new_day_tasks = tasks_day.copy()
tasks_night = list(tasks_day)
tasks_day = new_day_tasks[:]
print(new_day_tasks, tasks_night)

# join lists
full_day_tasks = tasks_day + tasks_night
print(full_day_tasks)