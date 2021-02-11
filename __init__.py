from mycroft import MycroftSkill, intent_file_handler


class ProgrammingSupport(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('support.programming.intent')
    def handle_support_programming(self, message):
        self.speak_dialog('support.programming')


def create_skill():
    return ProgrammingSupport()

