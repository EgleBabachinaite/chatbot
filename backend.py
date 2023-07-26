import openai


def reading_key():
    with open("api_key", "r") as file:
        content = file.read()
        return content


class Chatbot:
    def __init__(self):
        openai.api_key = reading_key()

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.5
        ).choices[0].text
        return response


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write a joke about books")
    print(response)