from mycroft.util.parse import normalize
from mycroft.util.parse import match_one
import json


class WorkoutAction:
    def __init__(self, utterance):
        self.resource = ""
        self.words = utterance
        self.select_most_likely()

    def get_keywords(self, word_dict):
        self.words = normalize(self.words)
        # then get rid of pronouns verbs propositions ....
        not_keywords = word_dict["non_key"]
        self.words = [x for x in self.words if x != not_keywords]

    def score_likelihood(self, word_dict):
        resources = word_dict["resources"]
        # get from json
        scores = []
        for resource in resources:
            # json(resource) is to a list of words for stack wiki etc.
            # add json with these phrases (2/3 for proof of concept)
            scores += [resource, list(match_one(self.words, resources[resource]))]
        return scores

    def determine_resource(self, word_dict):
        scores = self.score_likelihood(word_dict)
        best_choice = max([score[2] for score in scores])
        if best_choice > .5:
            for score in scores:
                if score[2] == best_choice:
                    return score[0]
        else:
            return "ddg"

    def select_most_likely(self):
        in_file = open('files/data.json', 'r')
        # dict with all non keywords and key phrases
        word_dict = json.load(in_file)
        self.get_keywords(word_dict)
        self.resource = self.determine_resource(word_dict)
