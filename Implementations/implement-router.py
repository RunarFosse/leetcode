class Router:

    def __init__(self, memoryLimit: int):
        # Keep track of the memory limit
        self.memoryLimit = memoryLimit

        # And store all packets in a deque, and in a set
        self.packets, self.seen = deque([]), set()

        # Also, for each destination, keep track of packet times
        self.times = defaultdict(deque)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        # If the packet already exists, don't add it
        packet = (source, destination, timestamp)
        if packet in self.seen:
            return False

        # If the Router is filled, remove the oldest packet
        if len(self.packets) == self.memoryLimit:
            self.forwardPacket()
        
        # Otherwise, store the packet
        self.packets.append(packet)
        self.seen.add(packet)
        self.times[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        # Forward the oldest packet, if one exists
        if not self.packets:
            return []
        
        packet = self.packets.popleft()
        self.seen.remove(packet)
        self.times[packet[1]].popleft()
        return packet

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        # Given the destination, count packets within the time interval
        start = bisect_left(self.times[destination], startTime)
        end = bisect_right(self.times[destination], endTime)
        return end - start
            

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)