class SMS_store:
    """"Point class represents and manipulates x, y coordinates."""

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        """ Create new SMS tuple """
        self.has_been_viewed = False
        self.from_number = from_number
        self.time_arrived = time_arrived
        self.text_of_SMS = text_of_SMS

    def __str__(self):
        return "({}, {}, {}, {})".format(self.has_been_viewed, self.from_number, self.time_arrived, self.text_of_SMS)

    _counter = 0
    def message_count(self):
            SMS_store._counter += 1
            self.id = SMS_store._counter

    def get_unread_indexes(self):
        for message in SMS_store:
            if message.has_been_viewed == False:
                return self

    def get_message(i):

    def delete(i):

    def clear():
