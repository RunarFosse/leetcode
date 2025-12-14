# Author: Runar Fosse
# Time complexity: O(n(log n + m))
# Space complexity: O(m)

class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        # Using greedy

        # First, sort events in order of ascending timestap, with OFFLINE events first
        events.sort(key=lambda e: (int(e[1]), 0 if e[0] == "OFFLINE" else 1))
        
        # Create an array of mentions per user
        mentions = [0] * numberOfUsers

        # Also store last active time per user, and a counter for ALL mentions
        active, everyone = [0] * numberOfUsers, 0

        # Then iterate the array
        for event, time, mention in events:
            # If the event is an offline, update active time
            if event == "OFFLINE":
                active[int(mention)] = int(time) + 60
                continue
            
            # Otherwise it is a message, match based on the mention string
            match mention:
                case "ALL":
                    everyone += 1
                case "HERE":
                    # If only mentioning online, iterate all, incrementing online
                    for i in range(numberOfUsers):
                        if active[i] <= int(time):
                            mentions[i] += 1
                case _:
                    # Otherwise, extract all mentioned users, incrementing all
                    for user in mention.split(" "):
                        mentions[int(user[2:])] += 1
            
        # Finally, add ALL mentions to every user
        for i in range(numberOfUsers):
            mentions[i] += everyone
            
        # And return
        return mentions
