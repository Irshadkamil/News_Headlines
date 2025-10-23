import random

subjects=[
    "Narendra Modi",
    "Arvind Kejriwal",
    "Ranveer Singh",
    "Amit Shah",
    "Shah Rukh Khan"
]
Activity=[
    "Seen Practicing Dialogues",
    "Launches Wi-Fi-Powered Rickshaw Service",
    "Spotted Playing Chess with Security Guards",
    "Opens a ‘Confusion Counseling Center’",
    "Announces Plan to Open Yoga Classes"
]
locations=[
    "on the Moon",
    "in Bengaluru Tech Park",
    "in Pune",
    "at Marine Drive",
    "at India Gate"
]

while True:
    sub=random.choice(subjects)
    act=random.choice(Activity)
    loc=random.choice(locations)

    print("\n",f"{sub} {act} {loc}")

    user_input=input("Do you wand to print another fake headline ? (Yes/No):").strip().lower()

    if user_input=="no":
        print("\n","I hope you had fun! Good bye ")
        break
