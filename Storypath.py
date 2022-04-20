from Quest import Quest


class StoryPath:
    def __init__(self):
        StoryPath.market = Quest(0, 0, 0)
        StoryPath.forest = Quest(0, 0, 0)
        StoryPath.test = Quest(0, 0, 0)

    def dev_storypath(self):
        StoryPath.market.prompt = "MARKET - Go to the market"
        StoryPath.market.completion = False
        StoryPath.market.available = True
        StoryPath.forest.prompt = "FOREST - Go to the forest"
        StoryPath.forest.completion = False
        StoryPath.forest.available = True
        StoryPath.test.prompt = "WRONG"
        StoryPath.test.completion = True
        StoryPath.test.available = False


'''AS THE PC COMPLETES QUESTS, COMPLETION BECOMES TRUE AND AVAILABLE BECOMES FALSE. THE HOME FUNCTION, what_do_you_do
CALLS ON THE QUEST ATTRIBUTE TO PROMPT THE PLAYER INTO THE QUEST. THE dev_storypath FUNCTION CREATES THE RELEVANT 
STORYPATH'''
