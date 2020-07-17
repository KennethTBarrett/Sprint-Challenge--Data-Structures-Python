class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if node is not None:  # If the node exists...
            next = node.next_node  # Store `next` as our next node.
            # This is where we're gonna prepare to go backwards.
            node.next_node = prev  # Set the next node to `prev` one.
            # Set `prev` to be our node...
            prev = node
            # ... and `node` to be `next` (we're shifting backwards).
            node = next
            self.reverse_list(node, prev)  # Recursion is your friend.
        else:  # If the node doesn't exist...
            self.head = prev  # Make the head our `prev` value.

        # Okay, this was pretty tricky, but spending such an immense amount
        # of time trying to understand the fundamentals behind linked lists
        # in combination with UPER DEFINITELY made this doable, whereas I'm
        # not sure I would have been able to do this if I didn't - cheers to
        # putting in the time and effort! :D (also, to drawing on paper xD)
