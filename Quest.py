from Market import market
from Forest import forest


class Quest:
    def __init__(self, prompt, complete, available):
        Quest.prompt = prompt
        Quest.complete = complete
        Quest.available = available

    def toggle_available(self, bool):
        self.available = bool

    def toggle_complete(self, bool):
        self.complete = bool

    def go_on_quest(self, home, inventory, sheet, storypath):
        if "MARKET" in self.prompt:
            market(home, inventory, sheet, storypath)
        if "FOREST" in self.prompt:
            forest(home, inventory, sheet, storypath)