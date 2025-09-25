#Get supply data from user
countdown = input("How many seconds to launch?\n> ")
oxygen_tanks = input("How many oxygen tanks are packed?\n> ")
water_packs = input("How many water packs are packed?\n> ")
food_packs = input("How many food packs are packed?\n> ")

#Display supply data to user
print("----------SUPPLY CHECKLIST----------")
print("Countdown: " + countdown)
print("Oxygen Tanks: " + oxygen_tanks)
print("Water Packs: " + water_packs)
print("Food Packs: " + food_packs)

#Double check oxygen tank quantity
print("CONFIRM OXYGEN TANKS")
oxygen_tanks = input("> ")

#Display final supply data
print("-------FINAL SUPPLY CHECKLIST-------")
print("Countdown: " + countdown)
print("Oxygen Tanks: " + oxygen_tanks)
print("Water Packs: " + water_packs)
print("Food Packs: " + food_packs)