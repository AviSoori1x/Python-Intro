name= 'Zed A. Shaw'
age= 35 #not a lie
height=74 #inches
weight= 180 #lbs
eyes='Blue'
teeth='White'
hair='Brown'
weight_kg=round(weight/2.24)
height_cm=round(height*2.54)

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"His teeth are usually {teeth} depending on the coffee")
#This line is tricky, try to get it exactly right
total= age+height+weight
print(f"If I add {age}, {weight} and {height}, I get {total}")
print(f"If I add {age}, {weight_kg} and {height_cm}, once rounded is", age+weight_kg+height_cm )
#I think I got it right on my own terms
