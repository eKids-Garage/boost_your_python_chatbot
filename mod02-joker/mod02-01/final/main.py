def say(chatbot_name, user_name, phrase):
    return chatbot_name + ": Yes, " + user_name + ", " + phrase

def communicate (chatbot_name, user_name, bye_phrase):
    phrase = input(chatbot_name + ": What do you think? ")
    phrase = phrase.lower()
    
    if phrase.find(bye_phrase.lower()) == -1:
        responce = say(chatbot_name, user_name, phrase)
        print(responce)
        
        communicate(chatbot_name, user_name, bye_phrase)
    else:
        print("Bye, " + user_name + "!")
        return

chatbot_name = "Garik"
bye_phrase = "bye"

user_name = input("Hello! What's you name? ")
communicate(chatbot_name, user_name, bye_phrase)
