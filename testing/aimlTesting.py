import aiml

kernal = aiml.Kernal()
kernal.learn("testing.xml")
kernal.respond("load aiml b")

while True:
    print(kernal.respond(input("Enter your message >> ")))