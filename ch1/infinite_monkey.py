import string
import numpy as np


GOAL = 'methinks it is like a weasel'
LETTERS = list(string.ascii_lowercase) + [' ']


def generate():
    """Generate a random string the same length as the goal string."""
    return ''.join(np.random.choice(LETTERS, len(GOAL)))


def generate_rand_letter():
    """Generate a random letter."""
    return np.random.choice(LETTERS)
    
    
def score(s, other):
    """Score the given string by comparing to another string."""
    matches = [i for i in range(len(s)) if s[i] == other[i]]
    score = len(matches) / len(s)
    return score


def main():
    """Simulation of the infinite monkey theorem."""

    counter = 0
    best_str = None
    best_score = 0
    
    while best_score < 1:
        
        # Generate random string at first iteration
        if best_str is None:
            best_str = generate()
        else:
            # Find indices of incorrect letters
            incorrect = [i for i in range(len(GOAL)) if best_str[i] != GOAL[i]]
            # Modify one letter
            best_str_ls = list(best_str)
            best_str_ls[incorrect[0]] = generate_rand_letter()
            best_str = ''.join(best_str_ls)
        
        # Compute score
        best_score = score(best_str, GOAL)
        
        # Print progress
        counter += 1
        if not counter % 1000:
            print('Best string after {} trials : {}'.format(counter, best_str))
            print('Score :', best_score)
    
    print('Generated goal string "{}" in {} trials'.format(best_str, counter))


if __name__ == '__main__':
    main()
