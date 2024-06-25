# Task 1
restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

restaurant_menu["Beverages"] = {"Coke": 1.5, "Sweet Tea": 1.5}
restaurant_menu["Main Course"]["Steak"] = 17.99

del restaurant_menu["Starters"]["Bruschetta"]
print(restaurant_menu)


# Task 2
# Given
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def open_ticket(ticket_id, customer, issue):
    if ticket_id in service_tickets:
        print(f"Ticket ID {ticket_id} already exists.")
    else:
        service_tickets[ticket_id] = {"Customer": customer, "Issue": issue, "Status": "open"}
        print(f"Ticket {ticket_id} opened for {customer}.")

def close_ticket(ticket_id):
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["Status"] = "closed"
        print(f"Ticket {ticket_id} has been closed.")
    else:
        print(f"Ticket ID {ticket_id} not found.")

def display_tickets():
    for ticket_id, details in service_tickets.items():
        print(f"{ticket_id}: {details}")
    print()

def filter_tickets_by_status(status):
    filtered_tickets = {ticket_id: details for ticket_id, details in service_tickets.items() if details["Status"] == status}
    return filtered_tickets

open_ticket("Ticket003", "Charlie", "Refund issue")
close_ticket("Ticket001")
display_tickets()

open_tickets = filter_tickets_by_status("open")
print("Open Tickets:")
for ticket_id, details in open_tickets.items():
    print(f"{ticket_id}: {details}")
print()

closed_tickets = filter_tickets_by_status("closed")
print("Closed Tickets:")
for ticket_id, details in closed_tickets.items():
    print(f"{ticket_id}: {details}")
