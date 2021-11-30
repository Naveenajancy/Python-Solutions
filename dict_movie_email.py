'''
movies = {"Master : 11.00 am", "Despicable Me : 1.00 pm", "The Grinch : 3.00 pm"}
for shows in movies:
    print (shows)
'''

# create dict inside list
#create a contact and send a mail to all the subcribers

Subscribers = {"Total Number" : 10,
               "Contacts" : [
    {"name":"Pete the cat", "email" : "pete@example.com"},
    {"name":"Emma", "email":"emma@example.com"},
    {"name":"Kate", "email":"kate@example.com"}]
               }

for subscriber in Subscribers["Contacts"]:
    print (subscriber['email'])
