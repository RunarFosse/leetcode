# Author: Runar Fosse
# Time complexity: O(mlog(mn))
# Space complexity: O(m + n)

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # Using greedy
        meetings.sort()
        
        # Store meetings had per room and heaps of available meeting rooms
        meetings_had = [0] * n
        free_rooms, next_available = [i for i in range(n)], []
        heapify(free_rooms)
        heapify(next_available)

        room_max, meetings_max = 0, 0
        for start, end in meetings:
            # Add all rooms which are empty to free_rooms
            while next_available and next_available[0][0] <= start:
                _, room = heappop(next_available)
                heappush(free_rooms, room)
            
            # If there are no free rooms, wait until the next is free
            if not free_rooms:
                time, room = heappop(next_available)
                end += time - start
            # If there is, pick the smallest one
            else:
                room = heappop(free_rooms)

            # Assign this meeting to the room
            heappush(next_available, (end, room))
            meetings_had[room] += 1
            
            # Update (lowest) room with most meetings
            if meetings_had[room] >= meetings_max:
                if room < room_max or meetings_had[room] > meetings_max:
                    room_max = room
                meetings_max = meetings_had[room]
        
        print(meetings_had)
        
        # Find the room with the most meetings
        return room_max


# Sort meetings by start time, and greedily assign rooms until all are filled.
# Then, set the time of each room when they next are free, meaning another
# meeting could take place. Storing this in a min-heap means we can always
# have control over which room next will be free. Then we assign all meetings,
# and count which room has had the most meetings. This is the one we return.
# As we assign meetings to the current lowest free room, we need another heap
# keeping track over all the rooms which are free.