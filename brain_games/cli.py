import prompt


def welcome_user():
    """Welcome to the game"""
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name?')
    print(f"Hello, {name}!")
