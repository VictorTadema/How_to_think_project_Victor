class SMS_store:
    """"Point class represents and manipulates x, y coordinates."""

    def __init__(self):
        self.list_of_messages = []

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        """ Create new SMS tuple """
        self.has_been_viewed = False
        self.from_number = from_number
        self.time_arrived = time_arrived
        self.text_of_SMS = text_of_SMS


    def message_count(self):
        return len(self.list_of_messages)

    def get_unread_indexes(self):
        unread = []
        for index, ()

    def get_message(i):

    def delete(i):

    def clear():
