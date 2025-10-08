from src.models.user_model import create_user, verify_user

from src.utils.logger import log_info, log_error


def list_games():
    print("🎮 Current games:")
    games = get_all_games()
    print_table(games)

def move_player():
    game_id = input("Game ID: ")
    new_loc = input("New location code: ")
    update_location(game_id, new_loc)
    print(f"✅ Game {game_id} moved to {new_loc}")
