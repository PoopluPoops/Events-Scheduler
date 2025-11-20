# 3. Event Scheduler
# Design a simple event scheduler where users can add, remove, and list upcoming events.
# Each event has a name, date, and optional description.
# Events should be stored persistently (in a file or simple database).
# The program should display the next upcoming event when launched.
#Start with comments


events_date = []
while True:
    print("1.Append events")
    print("2.Remove events")
     
    choice = int(input("enter the choice from 1 or 2 "))

    if choice ==1:
        name = input("enter the event")
        date = input("enter the date")

        event = (name, date)
        events_date.append(event)
        print(events_date)

    elif choice == 2:
            name = input("enter the event to remove ")
            for event in events_date:
                if name in event:
                    events_date.remove(event)
            print(events_date)
