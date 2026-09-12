# write your program here!

#write your functions here

import json

# Show the welcome screen defined in the earlier task.
a = len("==================================================")
print("="*a)
print("|", end="")
print(" "*7, end="")
print("* USYD Club and Societies Finder *", end="")
print(" "*7, end="")
print("|")
print("="*a)
print("|", end="")
print(" "*9, end="")
print("* Find your people on campus *", end="")
print(" "*9, end="")
print("|")
print("="*a)

def is_alpha(string):
    if " " in string and not string.isspace():
        if string.replace(" ", "").isalpha():
            return True
    elif string.isalpha():
        return True
    else:
        return False

# Ask the student to create a valid profile.
metadata = []
def create_profile():
    global metadata
    name = input("Enter your full name: ")
    department = input("Enter your study area: ")
    year = input("Enter your year of study: ")
    output = True

    # once one warning output is produced, don't need to show the rest
    if not (is_alpha(name) and len(name) > 0 and len(name) < 26):
        output = False
        print("Incorrect name: Please enter a name between 1 and 25 characters.")
    elif not (is_alpha(department) and len(department) > 0 and len(department) < 26):
        output = False
        print("Incorrect study area: Please enter a study area using letters and spaces only.")
    elif not (year.isdigit() and int(year) > 0 and int(year) < 7):
        output = False
        print("Incorrect year: Please enter a year between 1 and 6.")
    if output:
        metadata.append(name)
        metadata.append(department)
        metadata.append(year)
        print(
f"""==================================================
|                Profile created!                |
==================================================
| Field         | Your Details                   |
==================================================
| Name          | {name:<25}      |
| Study Area    | {department:<25}      |
| Year of Study | {year}                              |
==================================================""")
        return metadata
    else:
        return output

def request_style():
    social_score = 0
    skill_score = 0
    valid_interest = ["academic", "creative", "volunteering", "culture", "sport", "social"]

    interest = input("What is your main interest area? ")
    if interest.lower() in valid_interest:
        hobby = input("What are your hobbies? ")
        is_social = input("Do you want to meet new people? ")
        is_inquisitive = input("Do you want to build new skills? ")
        if interest.lower() in valid_interest[3:]:
            social_score += 20
        else:
            skill_score += 20
        if is_social.lower()=="yes":
            social_score += 60
        if is_inquisitive.lower()=="yes":
            skill_score += 60
        # print(f"Your club style is: {interest.lower()}")
        # print(f"Social score: {social_score}")
        # print(f"Skill score: {skill_score}")
        return [interest.lower(), hobby, social_score, skill_score]
    else:
        print("Please enter a valid interest area.")
        return False

# Ask the club style questions and create the student dictionary.
def create_student(academic, personal):
    global social_score, skill_score
    if isinstance(academic, list) and isinstance(personal, list):
        student = {
        "name": academic[0],
        "study_area": academic[1],
        "year": int(academic[2]),
        "main_interest": personal[0],
        "social_score": personal[2],
        "skill_score": personal[3],
        "hobbies": personal[1].split(",")
        }
        return student
    else:
        return False

# Ask "Where is your club data file? ".
# Read the club data from the file. 
# If the file is invalid, print "Invalid club file." and finish the program.


test = """Sydney Computing Society,academic,coding|study|career
InstaSociety,doomscrolling,sleeping|eating
Board Games Society,social,games|social|beginner"""

valid_interest = ["academic", "creative", "volunteering", "culture", "sport", "social"]

def read_clubs(filename):
    with open(filename) as f:
        file_text = f.read()
    if file_text[-1]=="\n":
       file_text = file_text[:-1]
    clubs = file_text.split("\n")
    clubs_list = []
    for club in clubs:
        sep = club.split(",")
        category = sep[1]
        if category in valid_interest:
            # print(sep)
            info = {
                "name": sep[0],
                "category": category,
                "keywords": sep[2].split("|"),
            }
            clubs_list.append(info)
    return clubs_list

student = {
  "name": "antype",
  "study_area": "Engineering",
  "year": 2,
  "main_interest": "academic",
  "social_score": 60,
  "skill_score": 80,
  "hobbies": ["games", "social", "beginner"]
}

clubs = [
  {
    "name": "Sydney Computing Society",
    "category": "academic",
    "keywords": ["coding", "study", "career"]
  },
  {
    "name": "Board Games Society",
    "category": "social",
    "keywords": ["games", "social", "beginner"]
  }
]

# Calculate the top two club matches.
def match_clubs(student, clubs):
    score_list = []
    score = 0
    for club in clubs:
      if club["category"]==student["main_interest"]:
        score += 3
      if student["social_score"] >= 60 and "social" in club["keywords"]:
        score += 1
      if list(set(club["keywords"]).intersection(["skills", "career", "study"])) != [] and student["skill_score"] >= 60: # if [] is falsey
        score += 1
      for hobby in student["hobbies"]:
        if hobby in club["keywords"]:
          score += 1
      score_list.append(score)
      score = 0
    # [3, 2, 5, 3, 4, 5, 2]
    # [2, 2, 3, 3, 4, 5, 5]
    #  0  1  2  3  4  5  6
    l_sorted = sorted(score_list)
    first = score_list.index(l_sorted[-1])
    second = score_list.index(l_sorted[-2])
    if l_sorted[-1] == l_sorted[-2]:
      # since last 2 elem are equal, .index() only select the first instance 5 showed up and not the second, meaning first and second are both the same index on score_list
      both_scores = l_sorted[-1]
      # print("same score:", both_scores)
      all_instances = []
      for index, elem in enumerate(score_list):
        if elem==both_scores:
          all_instances.append(index)
      # print("all instances of same scores:", all_instances)
      for char in "abcdefghijklmnopqrstuvwxyz":
        if clubs[all_instances[0]]["name"][0].lower() == char:
          # print(clubs[all_instances[0]]["name"][0].lower())
          first = all_instances[0]
          second = all_instances[1]
          break
        elif clubs[all_instances[1]]["name"][0].lower() == char:
          # print(clubs[all_instances[1]]["name"][0].lower())
          first = all_instances[1]
          second = all_instances[0]
          break
    output = f"""First Club Recommendation
Name: "{clubs[first]["name"]}"
Score: {l_sorted[-1]}

Second Club Recommendation
Name: "{clubs[second]["name"]}"
Score: {l_sorted[-2]}"""
    with open(f"{student['name']}.txt", "w", encoding="utf-8") as f:
      f.write(output+"\n") # that extra \n almost made me give up wtf :/
    return [clubs[first]["name"], clubs[second]["name"]], [l_sorted[-1], l_sorted[-2]]

profile = None
while isinstance(profile, list)==False:
  profile = create_profile()

styles = None
file_path = ""
while True:
  while isinstance(styles, list)==False: # step 3 here "update"
    styles = request_style()

  student = create_student(profile, styles)
  if not file_path:
    file_path = input("Where is your club data file? ") # step 4 here "recommend"
  try:
     data = read_clubs(filename=file_path)
  except FileNotFoundError as e:
     print("Invalid club file.")
     break
  if data:
      #  print(student, data)
      recommendations = match_clubs(student, data)
      print(f"""Top matches:
1. {recommendations[0][0]} (score: {recommendations[1][0]})
2. {recommendations[0][1]} (score: {recommendations[1][1]})""")
      option = input("Choose an option: ")
      if option =="exit":
        break
      elif option =="update":
        styles = None
      elif option=="recommend":
        file_path = ""
  else:
    print("Invalid club file.")
    break
   

# Display the top matches in order, including their scores.
# Ask the user to choose an option: update, recommend or exit:

# If the user chooses "update", repeat the steps from (3) (This lets the user change their club style)

# If the user chooses "recommend", repeat the steps from (4) (This lets the user change the club file)

# If the user chooses "exit", finish the program



