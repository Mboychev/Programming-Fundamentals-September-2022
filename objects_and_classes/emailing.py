"""Create class Email. The __init__ method should receive sender, receiver and a content.
It should also have a default set to False attribute called is_sent.
The class should have two additional methods:
•	send() - sets the is_sent attribute to True
•	get_info() - returns the following string: "{sender} says to {receiver}: {content}. Sent: {is_sent}"
You will receive some information (separated by a single space) until you receive the command "Stop".
The first element will be the sender, the second one – the receiver, and the third one – the content.
On the final line, you will be given the indices of the sent emails separated by comma and space ", ".
Call the send() method for the given indices of emails. For each email, call the get_info() method.
Note: submit all of your code, including the class
###################################EXAMPLES#######################################
Input:
Peter John Hi,John
John Peter Hi,Peter!
Katy Lilly Hello,Lilly
Stop
0, 2
Output:
Peter says to John: Hi,John. Sent: True
John says to Peter: Hi,Peter!. Sent: False
Katy says to Lilly: Hello,Lilly. Sent: True

Input:
Anna, Bella, Hi
Sam, Dany, Okey
Felix, Mery, Bye
Stop
0
Output:
Anna, says to Bella,: Hi. Sent: True
Sam, says to Dany,: Okey. Sent: False
Felix, says to Mery,: Bye. Sent: False
"""


class Email:

    def __init__(self, sender, reciever, content):

        self.sender = sender
        self.reciever = reciever
        self.content = content
        self.is_send = False

        # change the email index to true when called

    def send(self):
        self.is_send = True

    def get_info(self):
        return f"{self.sender} says to {self.reciever}: {self.content}. Sent: {self.is_send}"


emails = []

while True:

    command = input()

    if command == "Stop":
        break

    sender, reciever, content = command.split(" ")

    # create object with class Email and attributes sender, reciever, content
    email = Email(sender, reciever, content)

    # append object email to list emails = []
    emails.append(email)

    # splits command "0, 2" by whitespace and ,
    # turns them to integer and turns current index into True when send() invoked

# send_emails = [emails[int(x)].send() for x in input().split(", ")]
send_emails = input().split(", ")
for x in send_emails:
    x = int(x)
    emails[x].send()
    # print object email through get_info() method
for email in emails:
    print(email.get_info())