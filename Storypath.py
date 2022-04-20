from Market import market
from Forest import forest


def game_over():
    print("Well... that's unfortunate. I'm afraid this is the end of the line.")
    exit()


class Quest:
    def __init__(self, complete, available, prompt, launch):
        Quest.completion = complete
        Quest.available = available
        Quest.prompt = prompt
        Quest.launch = launch

    def make_available(self):
        Quest.available = True


class StoryPath:
    def __init__(self):
        StoryPath.market = Quest(False, True, "MARKET - Go to the market", market())
        StoryPath.forest = Quest(False, True, "FOREST - Go to the forest", forest())


'''AS THE PC COMPLETES QUESTS, COMPLETION BECOMES TRUE AND AVAILABLE BECOMES FALSE. THE HOME FUNCTION, what_do_you_do
CALLS ON THE QUEST ATTRIBUTE TO PROMPT THE PLAYER INTO THE QUEST.'''
