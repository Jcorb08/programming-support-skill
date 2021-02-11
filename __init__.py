from mycroft.skills.common_query_skill import CommonQuerySkill, CQSMatchLevel

class ProgrammingSupport(CommonQuerySkill):
    def CQS_match_query_phrase(self, utt):
       # Parsing implementation
       # [...]
       return (utt, CQSMatchLevel.LEVEL, 'answer_string')

def create_skill():
    return ProgrammingSupport()