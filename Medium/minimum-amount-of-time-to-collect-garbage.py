# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        # Calculate travel time per garbage type, by keeping track of max index
        m_max = p_max = g_max = 0
        
        # Iterate all houses, iterating each garbage bag, adding time to each respective truck
        m_time = p_time = g_time = 0
        for i, garbage_bag in enumerate(garbage):
            for garbage_type in garbage_bag:
                if garbage_type == "M":
                    m_time += 1
                    m_max = i
                elif garbage_type == "P":
                    p_time += 1
                    p_max = i
                else:
                    g_time += 1
                    g_max = i
        
        # Add travel time to each
        for i, time in enumerate(travel):
            if i < m_max:
                m_time += time
            if i < p_max:
                p_time += time
            if i < g_max:
                g_time += time
        
        return m_time + p_time + g_time

# Because all other trucks have to idle whilst the last truck does anything, 
# this problem simply comes down to summing over the amount of time each truck 
# has to take to finish its job.