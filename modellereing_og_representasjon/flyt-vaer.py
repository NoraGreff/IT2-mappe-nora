grader = int(input("Hor mange grader er det ute?"))

if grader < 15:
    print("Ta på deg jakke")
    type = input("Regner det?")
    if type.lower == "ja":
        print("ta med paraply!")
else :
    print("Kos deg i varmen")