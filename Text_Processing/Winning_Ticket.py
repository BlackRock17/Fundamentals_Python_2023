import re

text = input()

tickets = re.split(r"[\s,\s]+", text)

regex = r"[$]{6,}|[#]{6,}|[@]{6,}|[\^]{6,}"

for ticket in tickets:
    if not ticket:
        continue

    if len(ticket) != 20:
        print("invalid ticket")
        continue

    first_half = ticket[0:10]
    second_half = ticket[10:]

    match_1 = "".join(re.findall(regex, first_half))
    match_2 = "".join(re.findall(regex, second_half))

    if len(match_1) > len(match_2):
        match_1 = match_1[0:len(match_2)]
    elif len(match_2) > len(match_1):
        match_2 = match_2[0:len(match_1)]

    if match_1 != match_2 or not match_1:
        print(f'ticket "{ticket}" - no match')

    elif len(match_1) < 10:
        print(f'ticket "{ticket}" - {len(match_1)}{match_1[0]}')

    else:
        print(f'ticket "{ticket}" - {len(match_1)}{match_1[0]} Jackpot!')
