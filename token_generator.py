import random

print(""" ▒█████   ███▄ ▄███▓▓█████   ▄████  ▄▄▄           ▄████ ▓█████  ███▄    █ ▓█████  ██▀███   ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███  
▒██▒  ██▒▓██▒▀█▀ ██▒▓█   ▀  ██▒ ▀█▒▒████▄        ██▒ ▀█▒▓█   ▀  ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
▒██░  ██▒▓██    ▓██░▒███   ▒██░▄▄▄░▒██  ▀█▄     ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
▒██   ██░▒██    ▒██ ▒▓█  ▄ ░▓█  ██▓░██▄▄▄▄██    ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  ░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
░ ████▓▒░▒██▒   ░██▒░▒████▒░▒▓███▀▒ ▓█   ▓██▒   ░▒▓███▀▒░▒████▒▒██░   ▓██░░▒████▒░██▓ ▒██▒ ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
░ ▒░▒░▒░ ░ ▒░   ░  ░░░ ▒░ ░ ░▒   ▒  ▒▒   ▓▒█░    ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
  ░ ▒ ▒░ ░  ░      ░ ░ ░  ░  ░   ░   ▒   ▒▒ ░     ░   ░  ░ ░  ░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░  ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░▒ ░ ▒░
░ ░ ░ ▒  ░      ░      ░   ░ ░   ░   ░   ▒      ░ ░   ░    ░      ░   ░ ░    ░     ░░   ░   ░   ▒    ░      ░ ░ ░ ▒    ░░   ░ 
    ░ ░         ░      ░  ░      ░       ░  ░         ░    ░  ░         ░    ░  ░   ░           ░  ░            ░ ░     ░     
                                                                                                                              
	Omega Generator - Discord Token Generator
        Author: Idk_#0979 | https://github.com/Mxmoun																													  
																															  
																															  """)



number_tokens = int(input("How many tokens you want to generate?: "))

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

for i in range(number_tokens):
	first = ''.join((random.choice(chars) for i in range(24)))
	second = ''.join((random.choice(chars) for i in range(6)))
	third = ''.join((random.choice(chars) for i in range(27)))

	result = first + "." + second + "." + third

	output = open("output.txt", "a")
	output.write(result + "\n")

print("Tokens generated.")
print("Please check the output.txt")