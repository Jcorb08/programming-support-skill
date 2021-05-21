from mycroft.util.parse import normalize, match_one
from mycroft.util.log import LOG


# create object using utterance of user
# and the intent dict from data.json file.
class WorkoutAction:

    resource = ""
    words = ""
    scores = ""

    def __init__(self, utterance, word_dict):
        self.words = utterance
        self.select_most_likely(word_dict)

    def score_likelihood(self, word_dict):
        resources = word_dict["resources"]
        # get from json
        scores = []
        for resource in resources:
            # returns each intent scored by how similar they are to utterance
            # resource next to them to identify scores
            scores += [[resource, list(match_one(self.words, resources[resource]))]]
        return scores

    def determine_resource(self, word_dict):
        # get the scores for each intent
        self.scores = self.score_likelihood(word_dict)
        #LOG.debug(self.scores, "scores")
        # get list of best choices for each resource category
        best_choice = max([score[1][1] for score in self.scores])
        # threshold for choice, this number after testing
        if best_choice > .45:
            for score in self.scores:
                if score[1][1] == best_choice:
                    # change the utterance to be the intent to search correctly
                    if score[0] == "api" or score[0] == "wiki":
                        self.words = score[1][0]
                    # return highest score
                    return score[0]
        else:
            return "ddg"

    # normalises utterance
    # calls function to determine the resource
    # replaces spaces with +s due to url characteristics.
    def select_most_likely(self, word_dict):
        self.words = normalize(self.words)
        self.resource = self.determine_resource(word_dict)
        self.words = self.words.replace(' ', '+')
