from openai import OpenAI
from utils import create_client

MODEL = "gpt-3.5-turbo"
CLIENT = create_client()

"""
The following function chooses the system message based on the 
provided parameters. 

The system is set up to respond with only the name and choose a QB.
Can optionally choose across a specific time frame. 
"""

# TODO: Impletement the Data Parameter Function
# TODO: Shorten the System Prompt

def select_system(date=False):
    
    return {"role": "system", "content": "You are a tool helping to determine"
            " the greatest Quarterback of all time for different nfl teams." 
            "When asked, you must respond with ONLY the name of the" 
            "quarterback and nothing else"}

"""
Creates a user prompt with the given NFL Team
"""
def choose_team(team):
    return {"role": "user", "content": f"Who is the greatest quarterback of the {team}."}

"""
Makes the request to the GPT-3 API and returns the response.
"""

def get_response(team, date=False):
    completion = CLIENT.chat.completions.create(
        model=MODEL,
        messages=[select_system(date), choose_team(team)]
    )
    return completion.choices[0].message.content


def main():
    ps = get_response("pittsburgh steelers")
    nep = get_response("new england patriots")
    gbp = get_response("green bay packers")
    dc = get_response("dallas cowboys")

    print(ps)
    print(nep)
    print(gbp)
    print(dc)


if __name__ == "__main__":
    main()