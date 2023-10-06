from socket import *
from threading import *
import random

serverPort = 9

def handleClient(clientSocket, addr):
     ask =f"choose add number space number or substract number space number, or random number space number"
     clientSocket.send(ask.encode())
    
     while True:
        sentence = clientSocket.recv(2048).decode()
        if not sentence:
            break  # Afslut løkken, hvis der ikke er modtaget nogen besked fra klienten
        
        splitterText = sentence.split()
        Text = ""
        if splitterText[0].lower() == "add":
            talx = int(splitterText[1])
            taly = int(splitterText[2])
            Text = f"{talx}+{taly}= {(talx + taly)}"
        elif splitterText[0].lower() == "substract":
            talx = int(splitterText[1])
            taly = int(splitterText[2])
            Text = f"{talx}-{taly}= {(talx - taly)}"
        elif splitterText[0].lower() == "random":
            talx = int(splitterText[1])
            taly = int(splitterText[2])
            Text = f" {random.randint(talx, taly)}"
        else:
            Text = f"understøtter ikke metoden {splitterText[0]}"
        
        clientSocket.send(Text.encode())

     clientSocket.close()

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)
print("The server is up and running on port", serverPort)

while True:
    connectionSocket, addr = serverSocket.accept()
    print("forbundet til en Client fra adressen", addr)
    Thread(target=handleClient, args=(connectionSocket, addr)).start()
