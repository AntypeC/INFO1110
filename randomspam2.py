counts = 6
scores = 0
possession = True
# fuck you comment
user_entry = int(input("""
Enter what happened:
  1) tac
  2) try
  3) con
  >> """))
if user_entry == 1:
    counts -= 1
    if counts == 0:
        possession = False
if user_entry == 2:
    scores += 4
if user_entry == 3:
    scores += 2
print(f"Add {scores} to the total!")