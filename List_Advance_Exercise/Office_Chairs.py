n_rooms = int(input())

enough = True
free_chairs = 0

for room in range(1, n_rooms + 1):
    chairs, visitors = input().split(" ")
    visitors = int(visitors)

    if len(chairs) >= visitors:
        free_chairs += len(chairs) - visitors
    else:
        print(f"{visitors - len(chairs)} more chairs needed in room {room}")
        enough = False

if enough:
    print(f"Game On, {free_chairs} free chairs left")