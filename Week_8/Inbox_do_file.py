from Week_8.EX_11_1_12_6 import SMS_store

my_inbox = SMS_store()

my_inbox.add_new_arrival("0611060547", "5 uur", "ej lul")
print(my_inbox)

print(my_inbox.message_count())