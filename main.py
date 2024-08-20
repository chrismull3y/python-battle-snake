import random
import typing


def info() -> typing.Dict:
    print("INFO")

    return {
        "apiversion": "1",
        "author": "yellum",  # TODO: Your Battlesnake Username
        "color": "#888888",  # TODO: Choose color
        "head": "default",  # TODO: Choose head
        "tail": "default",  # TODO: Choose tail
    }


def start(game_state: typing.Dict):
    print("GAME START")


def end(game_state: typing.Dict):
    print("GAME OVER\n")


def move(game_state: typing.Dict) -> typing.Dict:
    # print(game_state)

    is_move_safe = {"up": True, "down": True, "left": True, "right": True}

    head = game_state["you"]["head"] 
    neck = game_state["you"]["body"][1]  

    if neck["x"] < head["x"]: 
        is_move_safe["left"] = False

    elif neck["x"] > head["x"]:
        is_move_safe["right"] = False

    elif neck["y"] < head["y"]:
        is_move_safe["down"] = False

    elif neck["y"] > head["y"]:
        is_move_safe["up"] = False

    # TODO: Step 1 - Prevent your Battlesnake from moving out of bounds
    max_x = game_state['board']['width'] - 1
    max_y = game_state['board']['height'] - 1

    if head["x"] == max_x:
        is_move_safe["right"] = False
    if head["x"] == 0:
        is_move_safe["left"] = False
    if head["y"] == max_y:
        is_move_safe["up"] = False
    if head["y"] == 0:
        is_move_safe["down"] = False
    
 
    # TODO: Step 2 - Prevent your Battlesnake from colliding with itself
    body = game_state['you']['body']

    for segment in body[1:]:
        if segment["y"] == head["y"] and segment["x"] > head["x"]:
            is_move_safe["right"] = False
        if segment["y"] == head["y"] and segment["x"] < head["x"]:
            is_move_safe["left"] = False
        if segment["x"] == head["x"] and segment["y"] > head["y"]:
            is_move_safe["up"] = False
        if segment["x"] == head["x"] and segment["y"] < head["y"]:
            is_move_safe["down"] = False

    # TODO: Step 3 - Prevent your Battlesnake from colliding with other Battlesnakes
    opponents = game_state['board']['snakes']

    for snake in opponents:
        for segment in snake["body"]:
            if segment["y"] == head["y"] and segment["x"] > head["x"]:
                is_move_safe["right"] = False
            if segment["y"] == head["y"] and segment["x"] < head["x"]:
                is_move_safe["left"] = False
            if segment["x"] == head["x"] and segment["y"] > head["y"]:
                is_move_safe["up"] = False
            if segment["x"] == head["x"] and segment["y"] < head["y"]:
                is_move_safe["down"] = False


    # Are there any safe moves left?
    safe_moves = []
    for move, isSafe in is_move_safe.items():
        if isSafe:
            safe_moves.append(move)

    if len(safe_moves) == 0:
        print(f"MOVE {game_state['turn']}: No safe moves detected! Moving down")
        return {"move": "down"}
    
    # Choose a random move from the safe ones
    next_move = random.choice(safe_moves)

    print(f"MOVE {game_state['turn']}: {next_move}")
    return {"move": next_move}


# Start server when `python main.py` is run
if __name__ == "__main__":
    from server import run_server

    run_server({"info": info, "start": start, "move": move, "end": end})