class WorkoutAction:
    def __init__(self, utterance):
        self.resource = 0
        self.words = utterance

    def get_keywords(self):
        self.words = ""
        # mycroft.util.parse.normalize(text, lang=None, remove_articles=True)
        # then get rid of pronouns verbs propositions ....

    def score_likelihood(self):
        self.words = ""
        scores = []
        # mycroft.util.parse.match_one(query, choices)
        return scores

    def select_most_likely(self):
        self.get_keywords()
        self.resource = max(self.score_likelihood())
