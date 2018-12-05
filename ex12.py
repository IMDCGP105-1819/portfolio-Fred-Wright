print("Where do you want to go out of these 4 places:")
print("NewYork, Auckland, Venice, Glasgow")
where = input()
if where == 'NewYork':
    plane_ticket_cost = 2000
if where == 'Auckland':
    plane_ticket_cost = 790
if where == 'Glasgow':
    plane_ticket_cost = 65
if where == 'Venice':
    plane_ticket_cost = 154

print("How many nights do you wish to spend here?")
nights = float(input())

print("What class do you wish to use?")
print("Economy, PremiumEconomy, BusinessClass or FirstClass?")
trip_class = str(input())
if trip_class == 'Economy':
    class_mmultiplier = 1
if trip_class == 'PremiumEconomy':
    class_mmultiplier = 1.3
if trip_class == 'BusinessClass':
    class_mmultiplier = 1.6
if trip_class == 'FirstClass':
    class_mmultiplier = 1.9

days = nights + 1
car_rental_cost = days * 30
if days > 3:
    car_rental_cost = car_rental_cost - 30
if days > 7:
    car_rental_cost = car_rental_cost - 50

plane_cost = plane_ticket_cost * class_mmultiplier
total_cost = car_rental_cost + plane_cost

print("This trip will cost", total_cost)
