def gcd(m, n):
    """Find the greatest common divisor with the Euclidean algorithm."""
    
    while m%n != 0:
        r = m % n
        m = n
        n = r
    return n


class Fraction:
    """Implementation of fraction."""
    
    def __init__(self, num, den):
        
        # Check that numerator and denomenator are both integers
        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError('Both numerator and denominator must be integers')
        
        # Handle negative denomenator
        if den < 0:
            self.num = -num
            self.den = -den
        else:
            self.num = num
            self.den = den
        
        # Reduce fraction
        common = gcd(self.num, self.den)
        self.num //= common
        self.den //= common
    
    def __repr__(self):
        return 'Fraction({}, {})'.format(self.num, self.den)
    
    def __str__(self):
        return '{}/{}'.format(self.num, self.den)
    
    def get_num(self):
        """Return numerator of the fraction."""
        return self.num
    
    def get_den(self):
        """Return denomenator of the fraction."""
        return self.den
    
    def __add__(self, other):
        """Addition operator."""
        newnum = self.num*other.den + self.den*other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)
    
    def __radd__(self, other):
        """Reversed addition operator."""
        return self.__add__(other)
    
    def __iadd__(self, other):
        """In-place addition operator."""
        self = self.__add__(other)
        return self
    
    def __sub__(self, other):
        """Subtraction operator."""
        newnum = self.num*other.den - self.den*other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)
    
    def __mul__(self, other):
        """Multiplication operator."""
        newnum = self.num * other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)
    
    def __truediv__(self, other):
        """Division operator."""
        newnum = self.num * other.den
        newden = self.den * other.num
        return Fraction(newnum, newden)
    
    def __gt__(self, other):
        """Greater than operator."""
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum > secondnum
    
    def __ge__(self, other):
        """Greater than or equal to operator."""
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum >= secondnum
    
    def __lt__(self, other):
        """Less than operator."""
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum < secondnum
    
    def __le__(self, other):
        """Less than or equal to operator."""
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum <= secondnum
    
    def __eq__(self, other):
        """Equality operator."""
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum
    
    def __ne__(self, other):
        """Not equal to operator."""
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum != secondnum


def main():
    
    f1_num = input('Enter numerator of LEFT operand: ')
    f1_den = input('Enter denominator of LEFT operand: ')
    f2_num = input('Enter numerator of RIGHT operand: ')
    f2_den = input('Enter denominator of RIGHT operand: ')
    
    f1 = Fraction(int(f1_num), int(f1_den))
    f2 = Fraction(int(f2_num), int(f2_den))
    
    print('f1 = {}, f2 = {}'.format(f1, f2))
    print('f1 + f2 =', f1 + f2)
    print('f1 - f2 =', f1 - f2)
    print('f1 * f2 =', f1 * f2)
    print('f1 / f2 =', f1 / f2)
    print('f1 > f2 :', f1 > f2)
    print('f1 >= f2 :', f1 >= f2)
    print('f1 < f2 :', f1 < f2)
    print('f1 <= f2 :', f1 <= f2)
    print('f1 == f2 :', f1 == f2)
    print('f1 != f2 :', f1 != f2)


if __name__ == '__main__':
    main()
