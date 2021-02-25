from mycroft.util.parse import normalize
from mycroft.util.parse import match_one


class WorkoutAction:
    def __init__(self, utterance):
        self.resource = 0
        self.words = utterance

    def get_keywords(self):
        self.words = normalize(self.words)
        # then get rid of pronouns verbs propositions ....
        not_keywords = []
        self.words = [x for x in self.words if x != not_keywords]

    def score_likelihood(self):
        self.words = ""
        resources = ""
        # get from json
        scores = []
        for resource in resources:

            # json(resource) is to a list of words for stack wiki etc.
            # add json with these phrases (2/3 for proof of concept)
            scores.append(match_one(self.words, resource))
        return [x[1] for x in scores]

    def select_most_likely(self):
        self.get_keywords()
        self.resource = max(self.score_likelihood())
