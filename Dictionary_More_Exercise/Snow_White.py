

data_dict = {}

while True:
    command = input()
    found = False

    if command == "Once upon a time":
        break

    dwarf_name, dwarf_hat_color, dwarf_physics = command.split(" <:> ")
    dwarf_physics = int(dwarf_physics)

    if dwarf_hat_color not in data_dict.keys():
        data_dict[dwarf_hat_color] = {dwarf_name: dwarf_physics}
    else:
        data_dict[dwarf_hat_color][dwarf_name] = dwarf_physics


print(data_dict)



