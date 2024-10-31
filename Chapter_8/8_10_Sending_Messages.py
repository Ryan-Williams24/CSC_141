def send_messages(messages, sent_messages):
    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)

messages = ["Hello", "Good morning", "How are you?"]
sent_messages = []

send_messages(messages[:], sent_messages) 
print("Messages:", messages)
print("Sent messages:", sent_messages)