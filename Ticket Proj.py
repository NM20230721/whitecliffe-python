class Ticket():
    #Counting Tickets
    total_tickets = 0
    open_tickets = 0
    closed_tickets = 0

    #methods for retrieving ticket analytics
    @classmethod
    def getTickets(cls):
        return Ticket.open_tickets

    @classmethod
    def getOpenTickets(cls):
        return Ticket.open_tickets
    @classmethod
    def getClosedTickets(cls):
        return Ticket.closed_tickets

    @classmethod
    def displayTicketStats(cls):
        print("-------STATS--------")
        print("Total Tickets: ",Ticket.total_tickets)
        print("Open Tickets: ", Ticket.open_tickets)
        print("Closed Tickets: ", Ticket.closed_tickets)
        print("--------------------")

    #intialising the ticket object
    def __init__(self, staff_id, ticket_creator_name, contact_email, desc):
        Ticket.total_tickets += 1
        Ticket.open_tickets += 1
        self.ticket_number = Ticket.total_tickets + 2000
        self.staff_id = staff_id
        self.ticket_creator_name = ticket_creator_name
        self.contact_email = contact_email
        self.desc = desc
        self.desc = self.desc.lower()

        self.solved = False
        self.password = ""

        self.feedback = "No Response Yet"
        #Password problems are automated
        if ((self.desc.find("password change") != -1) or (self.desc.find("passwordchange") != -1)):
            Ticket.open_tickets -= 1
            Ticket.closed_tickets += 1
            self.solved = True
            self.password = self.staff_id[:3] + self.ticket_creator_name[:3]
            self.feedback = ("Password Changed to: " + self.password)

    def getStatus(self):
        print("-----Ticket Status-----")
        print("Ticket Number:   ",self.ticket_number)
        print("Ticket Creator:  ",self.ticket_creator_name)
        print("Staff Id:        ", self.staff_id)
        print("Email Address:   ", self.contact_email)
        print("Description:     ", self.desc)
        print("Response:        ", self.feedback)
        print("Ticket Status:   ", self.solved)
        print("-----------------------")







ticketList = []

def submitTicket():
    print("-----SUBMITTING TICKETS-----")
    while 1 == 1:
        temp_object = Ticket(input("Input the Staff Id: "),
                            input("Input the Ticket Creator Name: "),
                            input("Input the Contact email: "),
                            input("Input the Description of the Event: "))
        ticketList.append(temp_object)
        print("---------------")
        check = input("Another Ticket? n for no, any for yes:  ")
        if check == "n":
            break

def viewTickets():
    print("-----VIEWING TICKETS-----")
    for i in range(len(ticketList)):
        print(ticketList[i].getStatus())
        input("Input anything to continue")


def addFeedback():
    print("-----ADDING FEEDBACK-----")
    inputId = input("What was the ID of the ticket")
    inputId = int(inputId)
    newFeedback = input("Input an update to the ticket: ")
    ticketList[inputId].feedback = newFeedback
    if input("Would you like to close this ticket? y for yes").lower == "y":
        ticketList[inputId].solved = True

def openTicket():
    print("-----OPEN CLOSED TICKET-----")
    inputId = input("What was the ID of the ticket")
    inputId = int(inputId)
    ticketList[inputId].solved = False
    Ticket.open_tickets += 1
    Ticket.closed_tickets -= 1

allPaths = {"submit" : submitTicket,
            "respond" : addFeedback,
            "open" : openTicket,
            "view" : viewTickets,
            "analytics" : Ticket.displayTicketStats}

print("----------TICKETING SYSTEM------------")
print("ALL PATHS")
print("Submit Ticket          | submit")
print("Respond to a Ticket    | respond")
print("Open a closed Ticket   | open")
print("View ticket info       | view")
print("Print analytics        | analytics")

while 1 == 1:

    selector = input("What do you want to do? ")
    try:
        doPath = allPaths[selector]
    except:
        print("The input: ",selector," Is not valid")
    else:
        doPath()



