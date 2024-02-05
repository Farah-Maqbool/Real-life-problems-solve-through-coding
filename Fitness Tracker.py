#Fitness Tracker
"""Fitness Tracker: You're building a fitness tracker app. Create variables to store daily steps, 
distance walked, and calories burned. Write expressions to calculate average steps per week 
and total distance covered in a month"""
print("Fitness Tracker")
daily_step=int(input("Daily Steps (For an average healthy individual, walking 10,000 steps daily is considered a good target.): "))
distance_walked=int(input("Distance (Km): "))
calories_burned=int(input("Calories you Burned: "))
average_step=(daily_step*7)/7
distance_month=distance_walked*30
print(f"The distance you covered in a month is {distance_month} km, and the average number of steps is {average_step}.")