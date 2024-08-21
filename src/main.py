from core.battlesnake import Battlesnake


def info() -> dict:
    print("INFO")

    return {
        "apiversion": "1",
        "author": "yellum",
        "color": "#888888",
        "head": "default",
        "tail": "default",
    }


def start(game_state: dict):
    print("GAME START")


def end(game_state: dict):
    print("GAME OVER\n")


def move(game_state: dict) -> dict:

    battle_snake = Battlesnake(game_state)
    next_move = battle_snake.calculate_best_move()

    print(f"MOVE {game_state['turn']}: {next_move}")
    return {"move": next_move}


# Start server when `python main.py` is run
if __name__ == "__main__":
    from api.server import run_server

    run_server({"info": info, "start": start, "move": move, "end": end})
