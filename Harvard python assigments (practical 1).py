# Harvard python assigments (Practical 1)
harvard_assigment={
    "Week 0 Function,Variables":{"2/5/2024":"Indoor Voice",
        "3/5/2024":"Playback Speed",
        "4/5/2024":"Making Faces",
        "5/5/2024":"Einstein",
        "6/5/2024":"Tip Calculator"},
    "Week 1 Conditionals":{"7/5/2024":"Deep Thought",
        "8/5/2024":"Home Federal Savings Bank",
        "9/5/2024":"File Extensions",
        "10/5/2024":"Math Interpreter",
        "11/5/2024":"Meal Time"},
    "Week 2 Loops":{"12/5/2024":"camelCase",
        "13/5/2024":"Coke Machine",
        "14/5/2024":"Just setting up my twttr",
        "15/5/2024":"Vanity Plates",
        "16/5/2024":"Nutrition Facts"},
    "Week 3 Exception":{"17/5/2024":"Fuel Gauge",
        "18/5/2024":"Felipe’s Taqueria",
        "19/5/2024":"Grocery List",
        "20/5/2024":"Outdated"},
    "Week 4 Libraries":{"21/5/2024":"Emojize",
        "22/5/2024":"Frank, Ian and Glen’s Letters",
        "23/5/2024":"Adieu, Adieu",
        "24/5/2024":"Guessing Game",
        "25/5/2024":"Little Professor",
        "26/5/2024":"Bitcoin Price Index"}
    }
date=input("Date (dd/mm/yyyy): ")
for i in harvard_assigment:
    for key,values in harvard_assigment[i].items():
        if key==date:
            print(f'On this date {date} you should submit your assigment "{values}" in "{i}"')
