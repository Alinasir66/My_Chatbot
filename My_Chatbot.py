# pakistan_chatbot.py
# Offline friendly chatbot with basic knowledge about Pakistan

import datetime

print("🤖 PakistanBot is online! Type 'bye' to exit.\n")

knowledge_base = {
    "capital of pakistan": "The capital of Pakistan is Islamabad.",
    "largest city of pakistan": "The largest city of Pakistan is Karachi.",
    "founder of pakistan": "The founder of Pakistan is Quaid-e-Azam Muhammad Ali Jinnah.",
    "national language of pakistan": "The national language of Pakistan is Urdu.",
    "official language of pakistan": "The official language of Pakistan is English.",
    "independence day of pakistan": "Pakistan celebrates Independence Day on 14th August 1947.",
    "currency of pakistan": "The currency of Pakistan is the Pakistani Rupee (PKR).",
    "national animal of pakistan": "The national animal of Pakistan is the Markhor.",
    "national flower of pakistan": "The national flower of Pakistan is Jasmine.",
    "national poet of pakistan": "The national poet of Pakistan is Allama Muhammad Iqbal.",
    "provinces of pakistan": "Pakistan has four provinces: Punjab, Sindh, Khyber Pakhtunkhwa, and Balochistan.",
    "famous place in pakistan": "Some famous places are Hunza Valley, Skardu, Lahore Fort, Badshahi Mosque, and Faisal Mosque.",
    "president of pakistan": "You can check the latest president from news, as this bot works offline.",
    "prime minister of pakistan": "You can check the latest prime minister from news, as this bot works offline.",
}

greetings = ["hi", "hello", "assalamualaikum", "salam", "hey"]
how_are_you = ["how are you", "kaise ho", "how r u"]
thanks_words = ["thanks", "thank you", "shukriya"]

def get_time():
    return datetime.datetime.now().strftime("%I:%M %p")

def chatbot_response(user_input):
    text = user_input.lower().strip()

    # Greetings
    if any(word in text for word in greetings):
        return "Hello! 😊 I am your friendly PakistanBot. Ask me anything about Pakistan."

    # How are you
    if any(word in text for word in how_are_you):
        return "I'm doing great! Thanks for asking. How can I help you today?"

    # Time
    if "time" in text:
        return f"The current time is {get_time()}."

    # Thanks
    if any(word in text for word in thanks_words):
        return "You're most welcome! 😊"

    # Knowledge base search
    for key in knowledge_base:
        if key in text:
            return knowledge_base[key]

    # Default reply
    return "I'm not sure about that yet, but I'm learning! Try asking about Pakistan's history, cities, or culture."

# Chat loop
while True:
    user = input("You: ")
    if user.lower() == "bye":
        print("PakistanBot: Goodbye! Allah Hafiz 👋")
        break

    reply = chatbot_response(user)
    print("PakistanBot:", reply)

