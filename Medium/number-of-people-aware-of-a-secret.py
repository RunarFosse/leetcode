# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    mod = int(1e9 + 7)
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        # Using sliding window
        knowers, awares = [1] + [0] * (n - 1), 1
        snitches = 0

        # First, iterate the initial person's secret period
        for day in range(delay, forget):
            # Expand the snitches by people who are now ready to talk
            snitches += knowers[day - delay]

            # And count how many new people thus learns the secret
            knowers[day] = snitches
            awares = (awares + snitches) % self.mod
        
        # Then, iterate the rest of the days
        for day in range(forget, n):
            # Adding new snitches, removing those who forget
            forgetters = knowers[day - forget]
            snitches += knowers[day - delay] - forgetters

            # And count how many new people thus learns the secret
            knowers[day] = snitches

            # But remove people who have now forgotten
            awares = awares = (awares + snitches - forgetters) % self.mod

        # Finally, return the total amount of people aware of the secret at day n
        return awares


# We call the people spreading a secret a snitch.
# A person remains a snitch from (day + delay) to (day + forget).

# By storing how many people gets to know a secret at a given day,
# we can compute the current running sum of snitches, helping us compute the new
# number of knowers each day. We also ensure people forget after the given time.