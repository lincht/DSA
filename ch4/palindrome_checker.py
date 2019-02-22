import re


def is_palindrome(s):
    """Return True if the string is a palindrome, False otherwise."""
    
    # Remove non-word characters and change to lowercase
    s = re.sub(r'\W', '', s).lower()
    
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and is_palindrome(s[1:-1])


def main():
    
    phrases = ['madam i’m adam',
               'kayak',
               'aibohphobia',
               'Live not on evil',
               'Reviled did I live, said I, as evil I did deliver',
               'Go hang a salami; I’m a lasagna hog.',
               'Able was I ere I saw Elba',
               'Kanakanak',
               'Wassamassaw']
    
    for p in phrases:
        print(p, ':', is_palindrome(p))


if __name__ == '__main__':
    main()