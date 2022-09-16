import random

def run_day_trip_generator():
    options_list = generate_trip_options()
    current_trip = generate_trip(options_list)
    print_full_trip(current_trip)
    satitisfied(current_trip,options_list)

      

def satitisfied(current_trip,options_list):
    complete = ""
    while complete !="Y":
        complete = input("Are you satisifed with your trip? Y or N? ")
        if complete != "Y":
            current_trip = change_option(current_trip,options_list)
            print_full_trip(current_trip)
        else:
            print("Thank You. Here is your finalized trip: ")
            print_full_trip(current_trip)


def change_option(current_trip, options_list):
    change = input("Which would you like to change? 'Destination'  'Restaurant'  'Transportation' or 'Entertainment'   ")
    if change == "Destination":
        current_trip[0] = random_selector(options_list[0])
    elif change == "Restaurant":
        current_trip[1] = random_selector(options_list[1])
    elif change == "Transportaion":
        current_trip[2] = random_selector(options_list[2])   
    elif change == "Entertainment":
        current_trip[3] = random_selector(options_list[3])
    return current_trip



def random_selector(list1):
    return random.choice(list1)

def generate_trip_options():
    destinations_list = ["Milwaukee","Madison","Wisconsin Dells","Lake Geneva","Oconomowoc"]
    restaurants_list = ["Kopps","Culvers","Balistreri's", "Geneva ChopHouse",  "The Baker House", "OakFire", "The Keg & Patio", "River Walk Pup", "Ishnala Supper Club","AJ's Pub", "Mantra Indian Bistro" ]
    transportaion_list = ["Rental Car", "Uber", "Personal Vechicle", "Bicyle", "E-Scooter","Walking"]
    entertainment_list = ["River Cruise", "Kayaking","Fishing","Brewer's Game", "Bucks Game", "Bar Hopping", "Water Park", "National Parks", "Dell's Main Street", "Badger's Game"]
    result_list = [destinations_list,restaurants_list,transportaion_list,entertainment_list]
    return result_list

def generate_trip(options_list):
    result_list =[]
    result_list.append(random_selector(options_list[0]))
    result_list.append(random_selector(options_list[1]))
    result_list.append(random_selector(options_list[2]))
    result_list.append(random_selector(options_list[3]))
    return result_list

def print_full_trip(trip_list):
    print()
    print(f"Destination:   {trip_list[0]}")
    print(f"Restaurant:    {trip_list[1]}")
    print(f"Transportaion: {trip_list[2]}")
    print(f"Entertainment: {trip_list[3]}")
    print()


run_day_trip_generator()


