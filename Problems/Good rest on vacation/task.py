# put your python code here
duration = int(input())
food_per_day = int(input())
flight = int(input())
hotel_per_day = int(input())

print(duration * food_per_day + flight * 2 + hotel_per_day * (duration - 1))
