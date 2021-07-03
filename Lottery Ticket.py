maxTicketAvailable=5
Participants=[]
for i in range(maxTicketAvailable):
    Participants.append(input("enter your name"))
import random
n=random.randint(0,maxTicketAvailable-1)
print(Participants[n])
