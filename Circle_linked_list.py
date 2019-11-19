class Node:
    def __init__(self, val, prev, next):
        self.val = val
        self.prev = prev
        self.next = next


class Circle_linked_list:
    has_popped = False

    def __init__(self):
        # for push pop
        self.header = None
        self.tail = None
        # for iter
        self.curr = None

    def push(self, val):
        new = Node(val, None, None)
        if self.header is None:
            # init
            self.header = new
            self.tail = new
            self.curr = new
            new.next = new
            new.prev = new
        else:
            new.prev = self.tail
            new.next = self.header
            # modify tail
            self.tail.next = new
            self.tail = new
            # modify header
            self.header.prev = new

    def pop(self):
        self.has_popped = True

        if self.header is self.tail:
            if self.curr is not None:
                # last item is going to be popped
                r = self.curr.val
                # restart everything
                self.__init__()
                return r
            else:
                # vacant
                return None
        else:
            c = self.curr
            if c is self.header:
                self.header = c.next
            elif c is self.tail:
                self.tail = c.prev
            # normally node
            c.next.prev = c.prev
            c.prev.next = c.next
            # set curr
            self.curr = c.next
            return c.val

    def __iter__(self):
        while True:
            if self.curr is not None:
                yield self.curr.val
                if self.has_popped is True:
                    self.has_popped = False
                else:
                    # normally iter
                    self.curr = self.curr.next
            else:
                # there is no item anymore.
                yield None
