import pyttsx3
friend = pyttsx3.init()
speech = raw_input("HEY!!! I am your Assistant , Say Something")
friend.say(speech)
friend.runAndWait()