text = input()
vowels = "AaOoUuEeIi"

new_text = [char for char in text if not char in vowels]

print("".join(new_text))
