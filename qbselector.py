import openai
from GQBOAT import config

openai.api_key = config.openai_key
model = "gpt-3.5-turbo"

def message_prompt(team_name):
    return [{
        "role":"user",
        "content":f"Who is the greatest quarterback of the {team_name}. "
                  f"The output should ONLY include the name of ONE quarterback"
    }]

def completion_wrapper(team_name):
    completion = openai.ChatCompletion.create(
        model = model,
        temperature = 1,
        messages = message_prompt(team_name)
    )
    return completion

def main():
    team_name = input("For Which Team Do you Want the Greatest Quarterback of All Time: \n")
    completion = completion_wrapper(team_name)
    player_name = completion.choices[0].message.content

    print(f"The greatest QB of all time for the {team_name} is {player_name}")

if __name__ == "__main__":
    main()