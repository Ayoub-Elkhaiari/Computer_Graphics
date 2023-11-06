note = int(input("Enter grade: "))

if note <= 10:
  print("Mediocre")
elif note == 10:
  print("Fair")
elif 11 < note <= 13:
  print("Pretty good") 
elif 14 < note <= 16:
  print("Good")
elif 17 < note <= 20:
  print("Very good")