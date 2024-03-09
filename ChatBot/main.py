import openai

openai.api_key="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"

def chat(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        message=[{"role":"user", "content":prompt}]
    )

    return response.choices[0].message.content.stripe()

    if __name__=="__main__":
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["quit","exit","bye"]:
                break

                response= chat(user_input)
                print("ChatBot",response)
