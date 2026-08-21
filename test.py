import os, time
os.system("clear")

def typeit(output, delay=0.03, remain_static=False):
    os.system("clear")
    for i in output:
        print(i, end="", flush=True)
        time.sleep(delay)
    if remain_static==False:
        time.sleep(3)
        os.system("clear")
while True:
    try:
        a = int(input("Total adults: "))
        k = int(input("Total children (12 max): "))
        if  a<0 or not (0<=k<=12):
            typeit("Invalid # of participant(s), try again.")
        else:
            break
    except:
        print(Exception)
        typeit("Invalid input, try again.")
adults=a*15.50
kids=k*6.50
taxes=round((6.5/100)*(adults+kids),2)
typeit(f"Total $ for adults: ${adults:.2f}\nTotal $ for children: ${kids:.2f}\nTotal $ inclusive service tax: ${adults+kids+taxes:.2f}\n", remain_static=True)
