from gpt import get_response


def main():
    team_name = input("Choose a team: \n")
    response = get_response(team_name)
    print(response)


if __name__ == '__main__':
    main()

