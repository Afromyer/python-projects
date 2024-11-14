#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
def RetrieveNames(filepath):
    with open(filepath) as names:
        names = names.readlines()
        new_names = []
        for name in names:
            new_name = name.strip()
            new_names.append(new_name)
        return new_names

def CreateLetter(name):
    with open("./Input/Letters/starting_letter.txt") as letter:
        lines = letter.readlines()
        greet = lines[0]
        new_greet = greet.replace("[name]", name)
        lines[0] = new_greet
        new_string = ""
        for line in lines:
            new_string += line
        return new_string


names = RetrieveNames("./Input/Names/invited_names.txt")

for name in names:
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as file:
        file.write(CreateLetter(name))


