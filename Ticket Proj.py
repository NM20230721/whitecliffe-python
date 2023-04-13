class Ticket:
    # Counting Tickets
    total_tickets = 0
    open_tickets = 0
    closed_tickets = 0

    # methods for retrieving ticket analytics
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
        print("Total Tickets: ", Ticket.total_tickets)
        print("Open Tickets: ", Ticket.open_tickets)
        print("Closed Tickets: ", Ticket.closed_tickets)
        print("--------------------")

    # intialising the ticket object
    def __init__(self, staff_id, ticket_creator_name, contact_email, desc):
        Ticket.total_tickets += 1
        Ticket.open_tickets += 1
        self.ticket_number = Ticket.total_tickets + 2000
        self.staff_id = staff_id
        self.ticket_creator_name = ticket_creator_name
        self.contact_email = contact_email
        self.desc = desc
        self.desc = self.desc.lower()

        self.status = "Not Solved"
        self.password = ""

        self.feedback = "No Response Yet"
        # Password problems are automated
        if (
            (self.desc.find("password change") != -1)
            or (self.desc.find("passwordchange") != -1)
            or (self.desc.find("change password") != -1)
            or (self.desc.find("changepassword") != -1)
        ):
            Ticket.open_tickets -= 1
            Ticket.closed_tickets += 1
            self.status = "Solved"
            self.password = self.staff_id[:3] + self.ticket_creator_name[:3]
            self.feedback = "Password Changed to: " + self.password

    def getStatus(self):
        print("-----Ticket Status-----")
        print("Ticket ID:   ", self.ticket_number)
        print("Ticket Creator:  ", self.ticket_creator_name)
        print("Staff Id:        ", self.staff_id)
        print("Email Address:   ", self.contact_email)
        print("Description:     ", self.desc)
        print("Response:        ", self.feedback)
        print("Ticket Solved:   ", self.status)
        print("-----------------------")



ticketList = [] #keeps all the tickets, object type = Ticket

def submitTicket():
    print("-----SUBMITTING TICKETS-----")
    x = True #I discovered that python exits all loops when you use break, I needed a loop breaker variable
    while 1 == 1:
        while x == True:
            inputStaff = input("Input the Staff Id: ")
            if inputStaff.isnumeric():
                x = False
            else:
                print("Staff ID must only contain Numbers")

        x = True
        while x == True:
            inputName = input("Input the Name: ")
            if inputName.isalpha():
                x = False
            else:
                print("Name must only contain Letters")

        x = True
        while x == True:
            inputEmail = input("Input the Contact email: ")
            if inputEmail.find("@") != -1:
                x = False
            else:
                print("Email must include @")

        x = True #resets loop breaker
        inputDesc = input("Input the description of the event: ")

        tempTicket = Ticket(inputStaff, inputName, inputEmail, inputDesc) #creates a Ticket Object
        ticketList.append(tempTicket) #inserts Ticket Object into List

        print("---------------")
        check = input("Another Ticket? n for no, any for yes:  ")
        if check == "n":
            break


def getTicket():
    while 1 == 1:
        i = 0
        listSize = len(ticketList)
        foundId = False
        inputId = input("What was the ID of the ticket: ")
        while i < listSize:
            if ticketList[i].ticket_number == int(inputId):
                foundId = True
                listSize = 0  # gets out of for loop
            else:
                i += 1

        if foundId == False:
            print("The Ticket ID: ", inputId, " Does not Exist")
        else:
            return i



def viewTickets():
    print("-----VIEWING TICKETS-----")
    for i in range(len(ticketList)):
        print(ticketList[i].getStatus())
        input("Input anything to continue")


def addFeedback():
    print("-----ADDING FEEDBACK-----")
    index = getTicket()
    newFeedback = input("Input an update to the ticket: ")
    ticketList[index].feedback = newFeedback
    if input("Would you like to close this ticket? y for yes: ") == "y":
        print("TICKET SOLVED!!!!!")
        ticketList[index].solved = "Solved"


def openTicket():
    print("-----OPEN CLOSED TICKET-----")
    index = getTicket()
    Ticket.open_tickets += 1
    Ticket.closed_tickets -= 1
    ticketList[index].status = "Reopened"
    print("Ticket reopened")


def main():
    allPaths = {
        "submit": submitTicket,
        "respond": addFeedback,
        "reopen": openTicket,
        "view": viewTickets,
        "analytics": Ticket.displayTicketStats,
    }

    print("----------TICKETING SYSTEM------------")
    print("ALL PATHS")
    print("Submit Ticket          | submit")
    print("Respond to a Ticket    | respond")
    print("Open a closed Ticket   | reopen")
    print("View ticket info       | view")
    print("Print analytics        | analytics")

    while 1 == 1:
        print("-----MAIN-----")
        selector = input("What do you want to do? ")
        try:
            doPath = allPaths[selector.lower()]
        except:
            print("The input: ", selector, " Is not valid")
        else:
            doPath()


main()
