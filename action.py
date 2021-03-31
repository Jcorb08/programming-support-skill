from mycroft.util.parse import normalize, match_one
from mycroft.util.log import LOG
import json


class WorkoutAction:

    resource = ""
    words = ""

    def __init__(self, utterance, word_dict):
        self.words = utterance
        self.select_most_likely(word_dict)

    def get_keywords(self):
        self.words = normalize(self.words)
        # then get rid of pronouns verbs propositions ....

        # NEEDED?
        # not_keywords = word_dict["non_key"]
        # self.words = [x for x in self.words if x != not_keywords]

    def score_likelihood(self, word_dict):
        resources = word_dict["resources"]
        # get from json
        scores = []
        for resource in resources:
            # json(resource) is to a list of words for stack wiki etc.
            # add json with these phrases (2/3 for proof of concept)
            scores += [[resource, list(match_one(self.words, resources[resource]))]]
        return scores

    def determine_resource(self, word_dict):
        scores = self.score_likelihood(word_dict)
        LOG.debug(scores, "scores")
        best_choice = max([score[1][1] for score in scores])
        if best_choice > .5:
            for score in scores:
                if score[1][1] == best_choice:
                    if score[0] == "api":
                        self.words = score[1][0]
                    return score[0]
        else:
            return "ddg"

    def select_most_likely(self, word_dict):
        self.get_keywords()
        self.resource = self.determine_resource(word_dict)
        self.words = self.words.replace(' ', '+')
