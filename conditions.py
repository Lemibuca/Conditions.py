#CS 104

#Leslie Bustamante

#conditions.py

i = 1
while i<6:
    temp =int(float(input("Please enter the current temperature: ")))
    if temp>90:
        print("wear Shorts")
    elif 90>=temp>70:
        print("Short sleeves are fine")
    elif 70>=temp>50:
        print ("Wear a jacket")
    elif 50>=temp>32:
        print ("Wear a heavy coat")
    else :
        print ("Stay Inside")
    i += 1
