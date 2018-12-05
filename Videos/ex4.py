my_name = 'Fred Wright'
my_age = '18'
my_height = '1.84'
my_weight = '231'
My_weight = 600
my_eyes = 'Brown'
my_hair = 'Brown'
my_height_in_centi = '184'
my_weight_kg = float(my_weight) / 1.6


print(f"Let's talk about {my_name}.")
print(f"He is {my_height} meters tall.")
print(f"He's {my_weight} pounds.")
print(f"Which is {my_weight_kg} in kg.")
if My_weight > 500:
    print("is obese.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")

sum = float(my_height) + float(my_weight) + float(my_age)
print(f"If i add my weight, height and age i get {sum}.")
