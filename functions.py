#contains the functions for the rest app
import time

import os
async def CustomTimer():
    time.sleep(2)

async def runCommand(command):
    os.system(command)

def getEmails():
    lines = []
    with open("results/emails.txt") as file:
        lines= file.readlines()
    return lines

def getTwitter():
    lines = []
    with open("results/twitter.txt") as file:
        lines= file.readlines()
    return lines

def getLinkedin():
    lines = []
    with open("results/linkedin.txt") as file:
        lines= file.readlines()
    return lines
