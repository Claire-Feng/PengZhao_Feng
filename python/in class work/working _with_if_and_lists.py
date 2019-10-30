#groceries = {"Apple", "Orange", "Steak", "Chiken"}

#if "Pineapple" not in groceries:
  #  print("We have apples")
#else:
 #   print("We do not have apples")


age = 15

if age < 2:
    print("Baby")
else:
    if age < 4:
        print("Toddler")
    else:
        if age < 14:
            print("Kids")
        else:
            if age < 20:
                print("Teenagers")
            else:
                if age < 65:
                    print("Adults")
                else:
                    print("Elder")

#alternative way
if age < 2:
    print("Baby")
elif age < 4:
    print("Toddler")
elif age < 14:
    print("Kids")
elif age < 20:
    print("Teenagers")
elif age < 65:
    print("Adults")
else:
    print("Elder")


            