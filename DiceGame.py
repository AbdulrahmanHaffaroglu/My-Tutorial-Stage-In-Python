import random

dice = {
    1: (
        "┏─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"
    ),
    
    2: (
        "┏─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"        
    ),

    3: (
        "┏─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"        
    ),
    4: (
        "┏─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"        
    ),
    5: (
        "┏─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"        
    ),
    6: (
        "┏─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"        
    )
}

dice_quantity = int(input("Type how many dices do you want: "))

dices = []

for i in range(0,dice_quantity):
    dice_choice = random.randint(1, dice.__len__())
    dices.append(dice_choice)

for i in range(0,5):
    for line in dices:
        print(dice.get(line)[i], end="")
    print() 