import random
destinations_list = ["Milwaukee","Madison","Wisconsin Dells","Lake Geneva","Oconomowoc"]
restaurants_list = ["Kopps","Culvers","Balistreri's", "Geneva ChopHouse", 
"The Baker House", "OakFire", "The Keg & Patio", "River Walk Pup", "Ishnala Supper Club",
"AJ's Pub", "Mantra Indian Bistro" ]
transportaion_list = ["Rental Car", "Uber", "Personal Vechicle", "Coach Bus"]
entertainment_list = ["River Cruise", "Kayaking","Fishing","Brewer's Game", "Bucks Game", "Bar Hopping", "Water Park", 
"National Parks", "Dell's Main Street", "Badger's Game"]

def random_selector(list1):
    return random.choice(list1)

print(random_selector(destinations_list))