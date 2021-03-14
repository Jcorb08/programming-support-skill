from mycroft.util.parse import normalize, match_one
from mycroft import MycroftSkill
import json


class WorkoutAction:

    resource = ""
    words = ""
    #word_dict = dict()

    def __init__(self, utterance, data):
        self.words = utterance
        self.select_most_likely()
        self.word_dict = data

    def get_keywords(self):
        self.words = normalize(self.words)
        # then get rid of pronouns verbs propositions ....

        # NEEDED?
        # not_keywords = word_dict["non_key"]
        # self.words = [x for x in self.words if x != not_keywords]

    def score_likelihood(self):
        resources = self.word_dict["resources"]
        # get from json
        scores = []
        for resource in resources:
            # json(resource) is to a list of words for stack wiki etc.
            # add json with these phrases (2/3 for proof of concept)
            scores += [resource, list(match_one(self.words, resources[resource]))]
        return scores

    def determine_resource(self):
        scores = self.score_likelihood()
        best_choice = max([score[2] for score in scores])
        if best_choice > .5:
            for score in scores:
                if score[2] == best_choice:
                    return score[0]
        else:
            return "ddg"

    def select_most_likely(self):
        self.get_keywords()
        self.resource = self.determine_resource()
        self.words = self.words.replace(' ', '+')
