def load_bar(num):
    loading = [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
    for i in range(int(num / 10)):
        loading[i] = "%"
    return loading


number = int(input())
result = "".join(load_bar(number))

if number == 100:
    print("100% Complete!")
    print(f"[{result}]")
else:
    print(f"{number}% [{result}]")
    print("Still loading...")


##### SECOND

def Non_full(percent):
    percent_complate = ""

    for i in range(10):
        if i < percent:
            percent_complate += "%"
        else:
            percent_complate += "."
    return percent_complate



percent = int(int(input()) / 10)

if percent == 10:
    print("100% Complete!")
    print("[%%%%%%%%%%]")
else:
    print(f"{percent * 10}% [{Non_full(percent)}]")
    print("Still loading...")

