#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = HashTable(length)
    route = [None] * (length - 1)

    for i in range(0, len(tickets)):
        hash_table_insert(ht, tickets[i].source, tickets[i].destination)

    curr_layover = "NONE"
    for i in range(0, length -1):
        route[i] = hash_table_retrieve(ht, curr_layover)
        curr_layover = route[i]

    return route
