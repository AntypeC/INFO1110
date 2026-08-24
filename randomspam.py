import time, os

def typeit(output, delay=0.03, duration=3):
        _output = []
        for i in output:
                print(i, end="", flush=True)
                _output.append(i)
                time.sleep(delay)

        if "".join(_output) == output:
              time.sleep(duration)

def load_animation(delay=0.05, ticks=10):
    frame = ['/', '|', '\\', '—', '/', '|']
    for j in range(ticks):
        for i in range(4): os.system("clear"); print(f"{frame[i]} Loading{(i % 4)*"."}"); time.sleep(delay)

# program 1
store_item = {
        "shoe": 10,
        "computer": 100,
        "car": 250,
        "home": 1000
        }

can_afford = []

while True:
        try:
              funds = float(input("Enter your total funds (ideally 0 < x < 1000): "))
              break
        except ValueError:
              typeit("Please enter valid value. Try again.")
              os.system("clear")

for item in store_item:
        if funds >= store_item[item]:
                can_afford.append(item)

typeit(f"You can afford {", ".join(can_afford)}!")

load_animation()
print()

# program 2
counts = 6
scores = 0
possession = True

while True:
        try:
                user_entry = int(input("""
Enter what happened:
1) tac
2) try
3) con
>> """))
                break
        except ValueError:
                print("Please enter valid value. Try again.")
                os.system("clear")
if user_entry == 1:
    counts -= 1
    if counts == 0:
        possession = False
if user_entry == 2:
    scores += 4
if user_entry == 3:
    scores += 2
typeit(f"Add {scores} to the total!")

load_animation()
print()

# program 3
# user_entry = [1, 2, 3, 4, 5, 6, 7, 9]
user_entry = input("Enter a series of scores here (seperated by an empty space): ")
user_entry = user_entry.strip()
user_entry = user_entry.split(" ")
_scores = []
for x in user_entry:
        if not x.isdigit():
               continue
        if "," in x:
                x = x.replace(",", "")
        _scores.append(int(x))

# _scores = list(map(int, user_entry))

max_score = _scores[0]
min_score = _scores[-1]
for i in _scores:
        if i >= max_score:
                max_score = i
        if i <= min_score:
                mine_score = i

total_score = 0
for i in _scores: total_score += i
avg_score = total_score / len(_scores)

typeit(f"Max. score: {max_score}\n", duration=0.5)
typeit(f"Min. score {min_score}\n", duration=0.5)
typeit(f"Avg. score: {avg_score}\n", duration=0.5)