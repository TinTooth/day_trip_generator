
import random

def run_list_option_randomizer():
    while True:
        options_list = list_selector()
        current_list = generate_random_list(options_list)
        print_full_randomized_list(current_list)
        finalize_randomized_list(current_list)
        if input("Do you want to randomize something else? Y / N:  ") == "N":
            print("Good-Bye")
            print()
            break

def list_selector():  # User selects which to randomize. Day Trip, Burger or their own inputs
    print("1) Day Trip options")
    print("2) Burger options")
    print("3) Your own options")
    user_choice = input("Which options do you want to randomize? 1, 2 or 3?  ")
    if user_choice == "1":
        options_list = generate_trip_categories_and_options()
        welcome = "Time to ranomize the Day Trip options!"
    elif user_choice == "2":
        options_list = generate_burger_categories_and_options()
        welcome = "Time to randomize the Burger options!"  
    else:
        options_list = user_generated_categories_and_options()
        welcome = "Time to randomize your own options!"
    print(welcome)
    print()
    return(options_list)        

def generate_trip_categories_and_options():  # returns lists of the categories and options of potential Day trips
    destinations_list = ["Milwaukee","Madison","Wisconsin Dells","Lake Geneva","Oconomowoc"]
    restaurants_list = ["Kopps","Culvers","Balistreri's", "Geneva ChopHouse",  "The Baker House", "OakFire", "The Keg & Patio", "River Walk Pup", "Ishnala Supper Club","AJ's Pub", "Mantra Indian Bistro" ]
    transportaion_list = ["Rental Car", "Uber", "Personal Vechicle", "Bicyle", "E-Scooter","Walking"]
    entertainment_list = ["River Cruise", "Kayaking","Fishing","Brewer's Game", "Bucks Game", "Bar Hopping", "Water Park", "National Parks", "Dell's Main Street", "Badger's Game"]
    total_options =[destinations_list,restaurants_list,transportaion_list,entertainment_list]
    categories =["Destinations","Restaurants","Transportation","Entertainment"]
    return [categories, total_options]

def generate_burger_categories_and_options(): # returns lists of the categories and options of potential Burgers
    buns = ['Pretzel', 'Kaiser Roll','Brioche','Sesame Seed']
    toppings_one = ['Onions','Lettuce','Carmalized Onions','Tomatoes','American Cheese','PepperJack Cheese','Swiss Cheese','Mushrooms','Fried Egg']
    toppings_two = ['Onions','Lettuce','Carmalized Onions','Tomatoes','American Cheese','PepperJack Cheese','Swiss Cheese','Mushrooms','Fried Egg']
    condiments = ['Ketchup','Yellow Mustard', 'Spicy Brown Mustard','BBQ Sauce','Stadium Sauce', 'Mayo']
    patty = ['Bison','Beef', 'Lamb', 'Duck']
    total_options = [buns,toppings_one,toppings_two,condiments,patty]
    categories = ['Buns','Toppings1', 'Toppings2','Condiments','Patties']
    return [categories, total_options]

def user_generated_categories_and_options(): # returns user generated lits of categories and options
    categories = []
    total_options =[]
    i = 0
    num_of_categories = input("Hello, how many different categories do you want? ")
    while num_of_categories.isnumeric() is False:
        num_of_categories = input("Sorry, please enter a number ")
    num_of_categories = int(num_of_categories)
   
    categories.append(input("What is the first Category? "))
    for num in range(num_of_categories-1):
        categories.append(input("What is the next Category? "))

    print()

    for num in range(num_of_categories):
        total_options.append([])
        num_of_options = (input(f"How many options do you want in {categories[num]} "))
        while num_of_options.isnumeric() is False:
            num_of_options = input("Sorry, please enter a number ")
        num_of_options = int(num_of_options) 
        total_options[i].append(input(f"What is the first item in {categories[num]}?   "))
        for num in range(num_of_options-1):
                total_options[i].append(input("Enter the next item  "))
        i +=1
        print()

    return [categories,total_options]
                
def generate_random_list(categories_and_options_list): # returns the category and options lists provided with an additional list that contains 1 random selection of the options for each category
    result_list = categories_and_options_list.copy()
    options_list = categories_and_options_list[1]
    ran_list =[]
    for num in range(len(categories_and_options_list[0])):
        ran_list.append(random.choice(options_list[num]))
    result_list.append(ran_list)    
    return result_list

def print_full_randomized_list(categories_options_and_randomlist_list): # prints the categories names with the randomly selected option for each
    categories = categories_options_and_randomlist_list[0]
    random_list = categories_options_and_randomlist_list[2]
    for num in range(len(categories)):
        print(f"{categories[num]}:  {random_list[num]}")
    print()

def change_option(categories_options_and_randomlist_lists): # prompts user to select a category to change the randomly selected option for and then changes that option
    categories = categories_options_and_randomlist_lists[0]
    options = categories_options_and_randomlist_lists[1]
    random_list = categories_options_and_randomlist_lists[2]
    print()
    print_categories(categories)
    print()    
    change = input("Which of the above categories do you want to change? ")
    print()
    while change not in categories:             # validation that user input is in categories list
        print_categories(categories)
        print()
        change = input('Sorry, please choose one of the above options ')
        print()
    for num in range(len(categories)):
        if change == categories[num]:
            random_list[num] = random.choice(options[num])
    return [categories,options,random_list]

def print_categories(categories): 
    for num in range(len(categories)):
        print(f'\'{categories[num]}\'', end = " " )

def finalize_randomized_list(categories_options_and_randomlist_list):# prompts user to finalize or change a option until satisfied with options
    categories = categories_options_and_randomlist_list[0]
    random_list = categories_options_and_randomlist_list[2]
    complete = ''
    while complete != "Y":
        complete = input("Are you satisfied with your random selections? Y or N  ")
        if complete != "Y":
            categories_options_and_randomlist_list = change_option(categories_options_and_randomlist_list)
            print_full_randomized_list(categories_options_and_randomlist_list)
        else:
            print()
            print("Thank You. Here are your finalized random selections: ")
            print_full_randomized_list(categories_options_and_randomlist_list)

run_list_option_randomizer()



