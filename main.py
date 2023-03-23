class Ticket():

    open_tickets = 0
    closed_tickets = 0

    @classmethod
    def getOpenTickets(cls):
        return Ticket.open_tickets
    @classmethod
    def getClosedTickets(cls):
        return Ticket.closed_tickets

    def __init__(self, staff_id, ticket_creator_name, contact_email, desc):
        Ticket.open_tickets = Ticket.open_tickets + 1
        self.staff_id = staff_id
        self.ticket_creator_name = ticket_creator_name
        self.contact_email = contact_email
        self.desc = desc
        self.desc = self.desc.lower()
        self.solved = False
        self.password = ""
        if ((self.desc.find("password change") != -1) or (self.desc.find("passwordchange") != -1)):
            Ticket.open_tickets -= 1
            Ticket.closed_tickets += 1
            self.solved = True
            self.password = self.staff_id[:3] + self.ticket_creator_name[:3]

    def getStatus(self):
        return self.solved

test = Ticket("20230721", "Nathaniel", "Email", "password change")
test1 = Ticket("20230721", "Nathaniel", "Email", "aaaa")
test2 = Ticket("20230721", "Nathaniel", "Email", "aaaa")
test3 = Ticket("20230721", "Nathaniel", "Email", "aaaa")
test4 = Ticket("20230721", "Nathaniel", "Email", "aaaa")

print(test.password)
print(Ticket.getOpenTickets())
