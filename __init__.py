from mycroft import MycroftSkill, intent_file_handler


class Decodicon(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('decodicon.intent')
    def handle_decodicon(self, message):
        self.speak_dialog('decodicon')


def create_skill():
    return Decodicon()

