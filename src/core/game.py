class Game:
    def __init__(self, game_data: dict):
        self.id: str = game_data["id"]
        self.ruleset: dict = game_data["ruleset"]
        self.map: str = game_data["map"]
        self.source: str = game_data["source"]
        self.timeout: int = game_data["timeout"]
