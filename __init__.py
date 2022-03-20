from mycroft import MycroftSkill, intent_file_handler


class HalloSager(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('sager.hallo.intent')
    def handle_sager_hallo(self, message):
        self.speak_dialog('sager.hallo')


def create_skill():
    return HalloSager()

