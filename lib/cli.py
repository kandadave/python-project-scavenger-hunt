import click
from lib.crud import *
from lib.utils import validate_location, draw_ascii_map
from lib.helpers import format_object

QUEST_TYPES = ("Adventure", "Mystery", "History")

def display_main_menu():
    click.echo("\n=== Urban Quest Creator ===")
    click.echo("1. Manage Users")
    click.echo("2. Manage Quests")
    click.echo("3. Show ASCII Map")
    click.echo("4. Exit")

def user_menu():
    while True:
        click.echo("\n=== User Menu ===")
        click.echo("1. Create User")
        click.echo("2. Delete User")
        click.echo("3. List Users")
        click.echo("4. Find User by ID")
        click.echo("5. Back")
        choice = click.prompt("Choose option (1-5)", type=int)
        try:
            if choice == 1:
                name = click.prompt("Name")
                email = click.prompt("Email", default="")
                preferences = click.prompt("Preferences", default="")
                user_id = create_user(name, email if email else None, preferences if preferences else None)
                click.echo(f"User created: ID {user_id}")
            elif choice == 2:
                user_id = click.prompt("User ID", type=int)
                delete_user(user_id)
                click.echo("User deleted")
            elif choice == 3:
                users = get_all_users()
                for user in users:
                    click.echo(format_object(user))
            elif choice == 4:
                user_id = click.prompt("User ID", type=int)
                user = find_user_by_id(user_id)
                click.echo(format_object(user))
            elif choice == 5:
                break
            else:
                click.echo("Invalid choice")
        except ValueError as e:
            click.echo(f"Error: {e}")

def quest_menu():
    while True:
        click.echo("\n=== Quest Menu ===")
        click.echo("1. Create Quest")
        click.echo("2. Delete Quest")
        click.echo("3. List Quests")
        click.echo("4. Find Quest by ID")
        click.echo("5. View Quest's Creator")
        click.echo("6. Back")
        choice = click.prompt("Choose option (1-6)", type=int)
        try:
            if choice == 1:
                name = click.prompt("Quest name")
                creator_id = click.prompt("Creator ID", type=int)
                location = click.prompt("Location")
                type = click.prompt(f"Type {QUEST_TYPES}")
                clue = click.prompt("Clue")
                find_user_by_id(creator_id)
                quest_id = create_quest(name, creator_id, location, type, clue)
                click.echo(f"Quest created: ID {quest_id}")
            elif choice == 2:
                quest_id = click.prompt("Quest ID", type=int)
                delete_quest(quest_id)
                click.echo("Quest deleted")
            elif choice == 3:
                quests = get_all_quests()
                for quest in quests:
                    click.echo(format_object(quest))
            elif choice == 4:
                quest_id = click.prompt("Quest ID", type=int)
                quest = find_quest_by_id(quest_id)
                click.echo(format_object(quest))
            elif choice == 5:
                quest_id = click.prompt("Quest ID", type=int)
                quest = find_quest_by_id(quest_id)
                creator = quest.creator
                click.echo(format_object(creator))
            elif choice == 6:
                break
            else:
                click.echo("Invalid choice")
        except ValueError as e:
            click.echo(f"Error: {e}")

@click.command()
def main():
    while True:
        display_main_menu()
        choice = click.prompt("Choose option (1-4)", type=int)
        try:
            if choice == 1:
                user_menu()
            elif choice == 2:
                quest_menu()
            elif choice == 3:
                location = click.prompt("Location")
                valid, _ = validate_location(location)
                if valid:
                    click.echo(draw_ascii_map(location))
                else:
                    click.echo("Invalid location")
            elif choice == 4:
                click.echo("Goodbye!")
                break
            else:
                click.echo("Invalid choice")
        except ValueError as e:
            click.echo(f"Error: {e}")

if __name__ == "__main__":
    main()