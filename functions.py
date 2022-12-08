#contains the functions for the rest app

def getEmails():
    lines = []
    with open("results/emails.txt") as file:
        lines.append(file.readlines())

    return lines
