class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.last_item = 0

    def append(self, item):
        # if storage is less than capacity append item
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        # if length of storage is greater than capacity
        else:
            self.storage[self.last_item] = item
            # if item is the last one, make it the first index (0) 
            if self.last_item == self.capacity - 1:
                self.last_item = 0
            else:
                self.last_item += 1

    def get(self):
        return self.storage