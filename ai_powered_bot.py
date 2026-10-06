from openai import OpenAI

key = "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"

messages = []

client = OpenAI(
    api_key=key,  # This is the default and can be omitted
)

def completion(message):
    global messages
    messages.append(
        {
            "role": "user",
            "content": message
        }
    )

    chat_completion = client.chat.completions.create( messages=messages,
                        model="gpt-4o"
                        )
    
    # print(chat_completion)
    message = {
        "role": "assistant",
        "content": chat_completion.choices[0].message.content
    }
    messages.append(message)
    print(f"Jarvis: {message["content"]}")

if __name__ == "__main__":
    print(f"Jarvis: Hi I am Jarvis, How may I help you\n")
    while True:
        user_question = input()
        print(f"User: {user_question}")
        completion(user_question)