#Restaurant Recommender
#
#PLAN: Make keyword vertices to store in a treenode with the keyword as the root with restaurants with the keyword as child
#Program will search if the typed keyword exists then display the restaurants under that keyword
#Imports:
from restaurantData import types
from restaurantData import restaurant_data

#Didn't use since the data is already stored in a list and it only allows for one keyword per restaurant
#If the data were stored in a different way it would be easier to use nodes

#Classes:
    #Will want to make a node class
    #Will want to make a treenode class
#class Node:
#    def __init__(self, type, price, rating, address):
#        self.type = type
#        self.price = price
#        self.rating = rating
#        self.address = address

#class TreeNode:
#    def __init__(self):
#        self.restaurants = []
    
#    def add_child(self, node):
#        self.restaurants.append(node)

#Tree Variables:
    #Is there a way to create nodes automatically with while loop running over the array of arrays for data?
    #Is there a way to create treenodes automatically with while loop running over array of types?


#Functions:
def main():
    print("Welcome to the restaurant recommender!")
    user_keyword = input("What would you like to eat today? ")
    while user_keyword not in types:
        print()
        user_keyword = autocomplete(user_keyword)
    recommended_restaurants = recommended(user_keyword)
    formatter(recommended_restaurants)

def autocomplete(user_keyword):
    user_keyword_length = len(user_keyword)
    possible_type = []
    for type in types:
        if user_keyword == type[:user_keyword_length]:
            possible_type.append(type)
    if possible_type == []:
        print("No matches were found based on what you typed.")
        new_keyword = input("Please try again. ")
        print()
    else:
        print("We have found {0} possible matches based on what you typed:".format(str(len(possible_type))))
        print(possible_type)
        new_keyword = input("Please type one of the choices above. ")
    return new_keyword

def recommended(user_keyword):
    rec_restaurants = []
    for restaurant in restaurant_data:
        if user_keyword == restaurant[0]:
            rec_restaurants.append(restaurant)
    return rec_restaurants

def formatter(restaurant_list):
    print("We recommend these restaurants:")
    print()
    for restaurant in restaurant_list:
        print("*****************")
        print(restaurant[1])
        print("Price rating: {0}/5".format(restaurant[2]))
        print("Food rating: {0}/5".format(restaurant[3]))
        print("Address: {0}".format(restaurant[4]))



main()