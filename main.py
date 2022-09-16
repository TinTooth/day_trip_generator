import random
destinations_list = ["Milwaukee","Madison","Wisconsin Dells","Lake Geneva","Oconomowoc"]
restaurants_list = ["Kopps","Culvers","Balistreri's", "Geneva ChopHouse", 
"The Baker House", "OakFire", "The Keg & Patio", "River Walk Pup", "Ishnala Supper Club",
"AJ's Pub", "Mantra Indian Bistro" ]
transportaion_list = ["Rental Car", "Uber", "Personal Vechicle", "Bicyle", "E-Scooter","Walking"]
entertainment_list = ["River Cruise", "Kayaking","Fishing","Brewer's Game", "Bucks Game", "Bar Hopping", "Water Park", 
"National Parks", "Dell's Main Street", "Badger's Game"]

def random_selector(list1):
    return random.choice(list1)

destination = random_selector(destinations_list)
restaurant = random_selector(restaurants_list)
transportaion = random_selector(transportaion_list)
entertainment = random_selector(entertainment_list)
complete = ""

while complete != "Yes":
    print()
    print("The follow is your potential Day Trip!")
    print(f"Destination:   {destination}")
    print(f"Restaurant:    {restaurant}")
    print(f"Transportaion: {transportaion}")
    print(f"Entertainment: {entertainment}")
    print()
    complete = input("Are you happy with this trip, and would like to complete the reservation? 'Yes' or 'No'?  ")
    if complete != "Yes":
        change = input("Which would you like to change? 'Destination'  'Restaurant'  'Transportation' or 'Entertainment'   ")
        if change == "Destination":
            destination = random_selector(destinations_list)
        elif change == "Restaurant":
            restaurant = random_selector(restaurants_list)
        elif change == "Transportaion":
            transportaion = random_selector(transportaion_list)   
        elif change == "Entertainment":
             entertainment = random_selector(entertainment_list)
    else:
        print("Thank you for selcting this day trip! Goodbye ")
        
                 


