import random


def run_day_trip_generator():
    current_trip = generate_trip()
    print_full_trip(current_trip)
    
    

        
            



def change_option(current_trip,list_of_options):
    current_trip = 0


def random_selector(list1):
    return random.choice(list1)


def generate_trip():
    destinations_list = ["Milwaukee","Madison","Wisconsin Dells","Lake Geneva","Oconomowoc"]
    restaurants_list = ["Kopps","Culvers","Balistreri's", "Geneva ChopHouse", 
    "The Baker House", "OakFire", "The Keg & Patio", "River Walk Pup", "Ishnala Supper Club",
    "AJ's Pub", "Mantra Indian Bistro" ]
    transportaion_list = ["Rental Car", "Uber", "Personal Vechicle", "Bicyle", "E-Scooter","Walking"]
    entertainment_list = ["River Cruise", "Kayaking","Fishing","Brewer's Game", "Bucks Game", "Bar Hopping", "Water Park", 
    "National Parks", "Dell's Main Street", "Badger's Game"]
    result_list =[]
    result_list.append(random_selector(destinations_list))
    result_list.append(random_selector(restaurants_list))
    result_list.append(random_selector(transportaion_list))
    result_list.append(random_selector(entertainment_list))
    return result_list

def print_full_trip(trip_list):
    print()
    print("The follow is your potential Day Trip!")
    print(f"Destination:   {trip_list[0]}")
    print(f"Restaurant:    {trip_list[1]}")
    print(f"Transportaion: {trip_list[2]}")
    print(f"Entertainment: {trip_list[3]}")
    print()


run_day_trip_generator()


