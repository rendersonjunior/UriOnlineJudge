#Fuel Spent
consume_car = 12
spent_time_trip = int(input())
average_speed_trip = int(input())

liters_need = (average_speed_trip/12)*spent_time_trip

print(format(liters_need,'.3f'))