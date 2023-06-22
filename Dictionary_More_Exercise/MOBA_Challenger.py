def check_players_availabe(players_list, name_1, name_2):
    finder = False
    if name_1 in players_list.keys() and name_2 in players_list.keys():
        finder = True
    return finder


def check_player_list(player_list, name, points):
    if name not in player_list.keys():
        player_list[name] = points
    else:
        player_list[name] += points
    return player_list

players_stats = {}
players_total = {}

while True:
    command = input()

    if command == "Season end":
        break

    if "->" in command:
        player, position, skill = command.split(" -> ")
        skill = int(skill)

        if player not in players_stats.keys():
            players_stats[player] = {position: skill}
            check_player_list(players_total, player, skill)

        else:
            if position not in players_stats[player]:
                players_stats[player][position] = skill
                check_player_list(players_total, player, skill)

            elif skill > players_stats[player][position]:
                players_total[player] += skill - players_stats[player][position]
                players_stats[player][position] = skill

    elif "vs" in command:
        player_1, player_2 = command.split(" vs ")

        if not check_players_availabe(players_stats, player_1, player_2):
            continue

        duel_valid = False
        for pos_1 in players_stats[player_1]:
            for pos_2 in players_stats[player_2]:
                if pos_1 != pos_2:
                    continue
                if players_stats[player_1][pos_1] == players_stats[player_2][pos_2]:
                    continue
                else:
                    if players_stats[player_1][pos_1] > players_stats[player_2][pos_2]:
                        del players_stats[player_2]
                        del players_total[player_2]
                    else:
                        del players_stats[player_1]
                        del players_total[player_1]
                    duel_valid = True
                if duel_valid:
                    break
            if duel_valid:
                break

sorted_by_points = dict(sorted(players_total.items(), key=lambda x: (-x[1], x[0])))

for name, points_ in sorted_by_points.items():
    print(f"{name}: {points_} skill")
    sorted_current_name = sorted(players_stats[name].items(), key=lambda x: (-x[1], x[0]))
    for player, points__ in sorted_current_name:
        print(f"- {player} <::> {points__}")

