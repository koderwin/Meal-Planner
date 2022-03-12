def meal_planner():
    print("Welcome to Meal Planner!")
    print("Please enter the following factors so we can best plan out the best possible meal plan schedule for today!")
    print("A. \"What's in the fridge (Program Inventory: milk, eggs, chicken thighs, etc.)")
    print("B. \"Western or Asian cuisine?\" ")
    
def run_meal_planner():
    program_inventory=['milk','cereal','cheese','minced beef','tomato sauce', 'onions', 'garlic','lettuce','tomatoes',
                       'chicken stock','carrot','celery', 'spaghetti','hamburger buns', 'mayonaise','salt','sugar',
                       'eggs','chicken thighs', 'bacon', 'tomatoes', 'onions', 'garlic', 'ginger','salt','sugar','noodles',
                       'rice', 'garam masala','chilli powder', 'soy sauce']
    western=program_inventory[0:17]
    asian=program_inventory[17:]
    missing_items=[]
    fridge_list=[]
    meal_planner()
    while True:
        x=input("Enter an item in your fridge, if done enter STOP:")
        x=x.lower()
        if x=="stop":
            break
        elif x not in program_inventory:
            print("Please enter another item as we do not have your item in our program inventory, or if the item is in two words, please put a space in between")
            continue
        else:
            fridge_list.append(x)
            continue
    
    y=input("Western or Asian:")
    y=y.lower()
    if y=='asian':
        print("Today you can make Tomato and Eggs Noodles, Bacon Fried Rice, and Butter Chicken")
        for item in asian:
            if item not in fridge_list:
                missing_items.append(item)
        print("However you are missing these items:", ' , '.join(missing_items))
        print("Time to go grocery shopping!")
                
    elif y=='western':
        print("Today you can make Milk and Cereal, Hamburgers, and Spaghetti Bolognese")
        for item in western:
            if item not in fridge_list:
                missing_items.append(item)
        print("However you are missing these items:", ' , '.join(missing_items))
        print("Time to go grocery shopping!")
           

run_meal_planner()
    