with open("./Input/Names/invited_names.txt", mode="r") as invited_names:
    for name in invited_names.readlines():
        with open("./Input/Letters/starting_letter.txt", mode="r") as starting_letter:
            default_text = starting_letter.readlines()
            name = name.strip("\n")
            default_text[0] = default_text[0].replace("[name]", f"{name}")
            with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="a") as output:
                for line in default_text:
                    output.write(line)
