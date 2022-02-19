from playsound import playsound

n=input("Enter the song :")
a="C:\\Users\\Satyam\\Music\\songs\\bekhudi.mp3" # The path of the song I wanted to play . 
b="C:\\Users\\Satyam\\Downloads\\Jarico - Island.mp3" # The path of the song I wanted to play . 
c="C:\\Users\\Satyam\\Downloads\\Piano Sad Emotional.mp3" # The path of the song I wanted to play . 

if n == "a":
    playsound(a)
if n == "b":
    playsound(b)
if n=="c":
    playsound(c)



