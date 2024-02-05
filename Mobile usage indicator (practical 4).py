# Mobile usage indicator (Practical 4 )
mobile_time=int(input("How much time did you use the mobile? (minute) "))
if mobile_time>60:
    result=mobile_time-60
    print(f"You waste {result} minutes on mobile :(")
else:
    print("Congratulations, you don't waste much time on your mobile")