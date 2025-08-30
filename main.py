import sys
from bare_cli.bare_cli import BareCLI


def demo():
    # Bread and butter
    io = BareCLI()
    io.title("Welcome to the BareCLI Demo")
    name = io.ask("What is your name?")
    likes_cli = io.confirm(f"Do you like command line interfaces, {name}?")

    if likes_cli:
        io.success("Glad to hear it!")
    else:
        io.error("That's too bad!")

    # Bells and whistles
    from bare_cli.invalid_choice_error import InvalidChoiceError
    from bare_cli.enums import Color

    io.success("Optional modules imported")

    io = BareCLI(Color.CYAN)
    io.info(f"Set accent color to {Color.CYAN.value}")
    try:
        choices = ["Noodles", "Burgers", "Street Meat", "Tacos", "Cheesecake"]
        choice = io.choice("What is your favorite food?", choices, exit_early=False)
        io.info(f"Chose {choice[0]}: {choice[1]}")
        io.success("Adios amigo!")
    except InvalidChoiceError:
        io.error("Adios amigo!")
    finally:
        sys.exit(0)


if __name__ == "__main__":
    demo()
