from linear_data_structure import Queue


class RadixSortingMachine:
    """Implementation of the radix sorting algorithm."""
    
    def __init__(self):
        
        self.main_bin = Queue()
        for i in range(10):
            self.__dict__['digit_bin_' + str(i)] = Queue()
    
    def _get_digit_bin(self, num):
        """Method to access digit bins.
        
        Parameters
        ----------
        num : int
            Bin number from 0 to 9.
        """
        return self.__dict__['digit_bin_' + str(num)]
    
    @staticmethod
    def get_digit(n, digit):
        """Return the digit in the specified digit place, e.g. passing digit=0 will
        return the ones digit, digit=1 the tens digit, digit=2 the hundreds digit,
        and so on.
        
        Parameters
        ----------
        digit : int
            Exponent of 10, e.g. digit=0 corresponds to the ones digit.
        """
        return n // 10**digit % 10
    
    def _distribute(self, digit):
        """Move values from the main bin to a digit bin corresponding to the digit
        being considered.
        
        Parameters
        ----------
        digit : int
            Exponent of 10, e.g. digit=0 corresponds to the ones digit.
        """
        while not self.main_bin.is_empty():
            n = self.main_bin.dequeue()
            d = self.get_digit(n, digit)
            self._get_digit_bin(d).enqueue(n)
    
    def _collect(self):
        """Collect all values from the digit bins and place them back in the main
        bin.
        """
        for i in range(10):
            b = self._get_digit_bin(i)
            while not b.is_empty():
                self.main_bin.enqueue(b.dequeue())
    
    def sort(self, ls):
        """Radix sort a list of non-negative integers.
        
        Parameters
        ----------
        ls : list-like
            List of non-negative integers.
        """
        
        for n in ls:
            self.main_bin.enqueue(n)
        
        # Find maximum number of digits
        max_ = max(ls)
        max_digit = 0
        while max_ // 10**max_digit > 0:
            max_digit += 1
        
        for digit in range(max_digit):
            self._distribute(digit)
            self._collect()
        
        return self.main_bin.items


def main():
    a = [170, 45, 75, 90, 2, 802, 2, 66]
    print('Input array :', a)
    radix = RadixSortingMachine()
    print('Radix sorted :', radix.sort(a))


if __name__ == '__main__':
    main()