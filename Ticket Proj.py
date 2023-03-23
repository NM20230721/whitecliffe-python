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

    def getStatus(self):
        print("-----Ticket Status-----")
        print("Ticket Number:   ",self.ticket_number)
        print("Ticket Creator:  ",self.ticket_creator_name)
        print("Staff Id:        ", self.staff_id)
        print("Email Address:   ", self.contact_email)
        print("Description:     ", self.desc)
        print("Response:        ", self.feedback)
        print("Ticket Status:   ", self.solved)







ticketList = []

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


for i in range(len(ticketList)):
    print(ticketList[i].getStatus())



