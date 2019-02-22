def reverse(s):
    """Return a new string that is the reverse of the input string."""
    
    if len(s) == 1:
        return s
    else:
        return reverse(s[1:]) + s[0]


def main():
    s = 'The quick brown fox jumps over the lazy dog'
    print('Input :', s)
    print('Output :', reverse(s))


if __name__ == '__main__':
    main()