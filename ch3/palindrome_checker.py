from linear_data_structure import Deque


def is_palindrome(s):
    """Return a boolean indicating where the input string is a palindrome.
    Whitespaces are ignored.
    """
    
    d = Deque()
    
    for char in s.replace(' ', ''):
        d.add_rear(char)
    
    while d.size() > 1:
        first = d.remove_front()
        last = d.remove_rear()
        if first != last:
            return False
    
    return True


def main():
    for s in ['lsdkjfskf', 'radar', 'I PREFER PI']:
        print('Checking "{}"... Result : {}'.format(s, is_palindrome(s)))


if __name__ == '__main__':
    main()