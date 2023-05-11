previos_version = input().split(".")

previos_version = int("".join(previos_version)) + 1

new_version = list(str(previos_version))

print(".".join(new_version))


### SECOND

current_version = "".join(input().split("."))
next_version = list(str(int(current_version) + 1))
print(".".join(next_version))