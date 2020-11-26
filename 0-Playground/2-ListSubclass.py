# We made swap an shift functions in the past, which were simple operations swapping the first and last element of a
# list, or putting the last element first and shifting all other elements one to the side. I wondered:
# Can I make a subclass of a list that has these methods?
class SpecList(list):
    def __init__(self, lst=()):
        super().__init__(lst)

    # Damn. This actually works.
    def swap(self):
        """
        Swaps first and last element of the list.
        :return:
        """
        # if len == 0 -> Error
        # if len == 1 -> no effect
        if len(self) > 1:
            self[0], self[-1] = self[-1], self[0]

    # Since the shift method basically makes an entirely new variable for self, it's gonna be a little more difficult.
    # Attempting to reassign to self doesn't work (self = ... creates new variable)
    def shift(self):
        if len(self) > 1:
            self[:] = SpecList([self[-1]] + self[0:-1])  # this somehow works. let's check the time.


def main():
    # testing swap and print of SpecList
    new_thingy = SpecList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    new_thingy.swap()
    print(new_thingy)

    # testing print of empty SpecList
    empty_thingy = SpecList()
    print(empty_thingy)

    # testing shift and time it takes
    shift_thingy = SpecList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    from time import time
    start = time()

    amount_of_tries = 10000001
    for i in range(amount_of_tries):
        shift_thingy.shift()
    stop = time()
    total_time = stop - start
    print(shift_thingy, "(took", round(total_time, 3), "seconds for", amount_of_tries, "iterations)")
    # takes about 2 seconds for 1'000'000 iterations, about 20 seconds for 10'000'000 iterations. Seems linear.


main()