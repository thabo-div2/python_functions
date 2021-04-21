# Handout Exercise
# defining Hotel Cost
def hotel_cost(nights):
    return 140 * nights


# defining Plane Ride Cost
def plane_ride_cost(city):
    if city == "Cape Town":
        return 2500
    elif city == "Durban":
        return 2300
    elif city == "JHB":
        return 2000
    elif city == "BFN":
        return 1800


# defining Rental Car Cost
# in rands
def rental_car_cost(days):
    car_cost = 40 * days
    if days >= 7:
        car_cost = car_cost - 50
    elif days >= 3 and days < 7:
        car_cost = car_cost - 20
    return car_cost


# defining Trip cost

def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money


# input from the user
location = input("Where did you go?: ")
holiday = int(input("How many days did you spend there?: "))
extra = float(input("How much money did you spend?: "))


print(trip_cost(location, holiday, extra))
