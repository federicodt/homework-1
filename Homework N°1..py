# Federico Teijeiro.
# June 8, 2023.
# Homework N°1.

# How old the user is.
# If someone says they were born in the future, try asking them again (assume they'll do it right the second time).
actual_year = int(2023)
birth_year = input("Please enter your year of birth: ")
birth_year = int(birth_year)
user_age = actual_year - birth_year
user_age = int(user_age)
birth_year = int(birth_year)
while True:
  try:
    if birth_year == actual_year:
      print("You can't be writing this")
    if birth_year >= 2019 and birth_year < actual_year:
      print("You can't be writing this")
  except ValueError:
    print("Please enter a year between 1960 and 2018.")
    continue
  except birth_year < 1960:
    print("Please enter a year between 1960 and 2018.")
    continue
  else:
    break
if birth_year >= 1960 and birth_year <= 2018:
  print(user_age)

# How many times the user's heart has beaten.
human_bpm = 80
user_heartbeats = human_bpm * 60 * 24 * 365 * user_age
print(f"Your heart was beating, approximately, {round(user_heartbeats/1000000000)} billion times.")

# How many times a blue whale's heart has beaten in that time.
blue_whale_bpm = 2 #Source: https://www.vox.com/down-to-earth/2022/8/11/23291991/largest-animal-blue-whale-heartbeat
blue_whale_heartbeats = blue_whale_bpm * 60 * 24 * 365 * user_age
print(f"At the same time, the heart of a blue whale was beating, approximately, {round(blue_whale_heartbeats/1000000)} million times.")

# How many times a rabbit's heart has beaten in that time.
# If the answer to rabbit heartbeats is more than a million, say "XXX million" instead of the very long raw number.
rabbit_bpm = 160 #Source: https://www.medivet.co.uk/pet-care/pet-advice/heart-disease-in-rabbits/#:~:text=A%20rabbit's%20resting%20heart%20rate,than%20five%20beats%20a%20second).
rabbit_heartbeats = rabbit_bpm * 60 * 24 * 365 * user_age
print(f"At the same time, the heart of a rabbit was beating, approximately, {round(rabbit_heartbeats/1000000)} million times.")

# How old they are in Venus years.
earth_year = 365
venus_year = 225 #Source: https://spaceplace.nasa.gov/all-about-venus/sp/#:~:text=Debido%20a%20que%20est%C3%A1%20tan,m%C3%A1s%20largo%20que%20un%20a%C3%B1o.
venus_years = (user_age * earth_year) / venus_year
print("You are", round(venus_years, 2), "Venus years old.")

# How old they are in Neptune years.
neptune_year = (164  * earth_year) + 298 #Source: https://spaceplace.nasa.gov/all-about-neptune/sp/
neptune_years = (user_age * earth_year) / neptune_year
print("You are", round(neptune_years, 2), "Neptune years old.")

# Whether they are the same age as you, older or younger.
# If older or younger, how many years difference.
# If they were born in an even or odd year.
my_birth_year = 1980
if birth_year == my_birth_year:
  print("We are the same age.")
elif birth_year <= 1979:
  older = my_birth_year - birth_year
  print("You are", older, "older than me.")
else:
  younger = birth_year - my_birth_year
  print("You are", younger, "younger than me.")

if birth_year % 2 == 0:
    print("You were born in an even year.")
else:
    print("You were born in an odd year.")

# How many times there has been a president from the Democratic Party in office since they were born (1960 onward, and each president only counts once).
if birth_year >= 2023:
  print("There had been only one president of the Democratic Party since you were born.")
elif birth_year >= 2017:
  print("There had been two president of the Democratic Party since you were born.")  
elif birth_year >= 2001:
  print("There had been three president of the Democratic Party since you were born.")
elif birth_year >= 1981:
  print("There had been four president of the Democratic Party since you were born.")
elif birth_year >= 1969:
  print("There had been five president of the Democratic Party since you were born.")  
else:
  print("There had been six president of the Democratic Party since you were born.")  
  
# Which US President was in office when they were born (1960 onward).
if birth_year < 1961:
  print("Dwight D. Eisenhower was the President of the United States when you were born.")
elif birth_year < 1963:
  print("John F. Kennedy was the President of the United States when you were born.")
elif birth_year < 1969:
  print("Lyndon B. Johnson was the President of the United States when you were born.")
elif birth_year < 1974:
  print("Richard M. Nixon was the President of the United States when you were born.")
elif birth_year < 1977:
  print("Gerald R. Ford was the President of the United States when you were born.")
elif birth_year < 1981:
  print("Jimmy Carter was the President of the United States when you were born.")
elif birth_year < 1989:
  print("Ronald Reagen was the President of the United States when you were born.")
elif birth_year < 1993:
  print("George Bush was the President of the United States when you were born.")
elif birth_year < 2001:
  print("Bill Clinton was the President of the United States when you were born.")
elif birth_year < 2009:
  print("George W. Bush was the President of the United States when you were born.")
elif birth_year < 2017:
  print("Barack Obama was the President of the United States when you were born.")
elif birth_year < 2021:
  print("Donald J. Trump was the President of the United States when you were born.")
else:
  print("Joseph R. Biden was the President of the United States when you were born.")
