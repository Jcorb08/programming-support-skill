from mycroft.skills.common_query_skill import CommonQuerySkill, CQSMatchLevel
from .action import WorkoutAction
from .resource import GetResource
from .output import Output
import json


def get_action(utterance, data):
    return WorkoutAction(utterance.lower(), data)


def get_resource(workout_action):
    return GetResource(workout_action)


def get_output(resource_):
    return Output(resource_)


class ProgrammingSupport(CommonQuerySkill):
    word_dict = None

    def __init__(self):
        super(ProgrammingSupport, self).__init__()

    def initialize(self):
        data_file = self.file_system.open("data.json", "r")
        self.word_dict = json.load(data_file)

    def CQS_match_query_phrase(self, utt):
        # utt: the question

        # ensures question is for the support skill
        # checks programming.voc for specific utterance word
        # i.e. "programming" "java" etc.
        if self.voc_match(utt, 'programming'):
            # gets an action based on utterance
            action_ = get_action(utt, self.word_dict)
            # if can't find an action
            if action_.resource == 0:
                self.speak("Cannot find action")
                return None
            else:
                # gets the resource based on action
                resource_ = get_resource(action_.resource, action_.words)
                if resource_.link == "":
                    self.speak("Cannot find Resource")
                    return None
                else:
                    # gets and outputs the resource to the user
                    get_output(resource_.link)
                    return utt, CQSMatchLevel.LEVEL, 'Support found, see your web browser'
        else:
            self.speak("Please Repeat that")
            return None


def create_skill():
    return ProgrammingSupport()
