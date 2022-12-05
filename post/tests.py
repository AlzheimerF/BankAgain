class BinarySearch():

    def search_iterative(self, list, item):
        # low and high keep track of which part of the list you'll search in.
        low = 0
        high = len(list) - 1
        x = 0
        # While you haven't narrowed it down to one element ...
        if list[-1] == item:
            return list[-1]

        while low <= high:
            # ... check the middle element
            mid = (low + high) // 2
            guess = list[mid]
            x += 1
            # Found the item.
            if guess == item:
                return x
            # The guess was too high.
            if guess > item:
                high = mid - 1

            # The guess was too low.
            else:
                low = mid + 1


        # Item doesn't exist
        return None

    def search_recursive(self, list, low, high, item):
        # Check base case
        if high >= low:

            mid = (high + low) // 2
            guess = list[mid]

            # If element is present at the middle itself
            if guess == item:
                return mid

                # If element is smaller than mid, then it can only
            # be present in left subarray
            elif guess > item:
                return self.search_recursive(list, low, mid - 1, item)

                # Else the element can only be present in right subarray
            else:
                return self.search_recursive(list, mid + 1, high, item)

        else:
            # Element is not present in the array
            return None


if __name__ == "__main__":
    # We must initialize the class to use the methods of this class
    bs = BinarySearch()
    my_list = [x for x in range(1, 258, 1)]

    print(bs.search_iterative(my_list, 127))  # => 1
    print(my_list[63])
    # 'None' means nil in Python. We use to indicate that the item wasn't found.
    print(bs.search_iterative(my_list, 9))  # => None

