#set value of variable cars to 100

#The total number of cars in the environment
cars=100
#Passengers per car
space_in_a_car=4
#The total number of drivers
drivers=30
#The total number of Passengers
passengers=90
#Number of cars not driven
cars_not_driven=cars-drivers
#Number of cars driven
cars_driven=drivers
#The total number of individuals that can be ferried by carpooling
carpool_capacity=cars_driven*space_in_a_car
#The per-car head count in this case
average_passengers_per_car=passengers/cars_driven

# Sequentual calculation of the average number of passengers per car to carpool
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers, available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car ,"in each car.")
