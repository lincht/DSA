import string
from linear_data_structure import Stack


DIGITS = string.digits
ALPHABET = string.ascii_uppercase
OPERATORS = '+-*/'


def do_math(op, left, right):
    """Helper function to perform mathematical operation."""
    return eval('{} {} {}'.format(left, op, right))


def infix_to_postfix(infix):
    """Convert an infix expression to a postfix expression."""
    
    tokens = infix.split()
    
    # Precedence of operators
    prec = {'(': 1, '+': 2, '-': 2, '*': 3, '/': 3}
    
    # Check for invalid characters
    invalid = set(tokens) - set(ALPHABET + DIGITS + OPERATORS + '()')
    if invalid:
        raise ValueError('Expression contains invalid characters {}'.format(invalid))
    
    # Operator stack
    op_stack = Stack()
    # Output
    postfix = []
    
    for t in tokens:
        
        # If token is an operand
        if t in ALPHABET + DIGITS:
            postfix.append(t)
        
        elif t == '(':
            op_stack.push(t)
        
        elif t == ')':
            # Pop stack until corresponding left parenthesis is removed
            top_token = op_stack.pop()
            while top_token != '(':
                postfix.append(top_token)
                # Right parenthesis without corresponding left parenthesis
                # is unbalanced
                if op_stack.is_empty():
                    raise RuntimeError('Unbalanced parenthesis')
                top_token = op_stack.pop()
        
        # If token is an operator
        else:
            # Push on stack, but only after removing any operators already on
            # stack with higher or equal precedence
            while not op_stack.is_empty() and prec[op_stack.peek()] >= prec[t]:
                  postfix.append(op_stack.pop())
            op_stack.push(t)
    
    # Append any operators still on stack after input expression is processed
    while not op_stack.is_empty():
        top_token = op_stack.pop()
        # Any remaining left parentheses are unbalanced
        if top_token == '(':
            raise RuntimeError('Unbalanced parenthesis')
        postfix.append(top_token)
    
    return ' '.join(postfix)


def eval_postfix(postfix):
    """Evaluate input postfix expression and return the result."""
    
    tokens = postfix.split()
    
    # Check for invalid characters
    invalid = set(tokens) - set(DIGITS + OPERATORS)
    if invalid:
        raise ValueError('Expression contains invalid characters {}'.format(invalid))
    
    # Operand stack
    op_stack = Stack()
    
    for t in tokens:
        # If token is an operand
        if t in DIGITS:
            op_stack.push(int(t))
        # If token is an operator, pop twice
        else:
            # Check for invalid operators
            if op_stack.size() < 2:
                raise RuntimeError('Invalid expression. \
Operator {} requires two operands'.format(t))
            right_op = op_stack.pop()
            left_op = op_stack.pop()
            result = do_math(t, left_op, right_op)
            op_stack.push(result)
    
    # Check for invalid operands
    if op_stack.size() > 1:
        # Pop last result
        op_stack.pop()
        raise RuntimeError('Invalid expression. \
Operand {} requires an operator'.format(op_stack.pop()))
    
    return op_stack.pop()


def eval_infix(infix):
    """Direct infix evaluator that combines the functionality of infix-to-postfix
    conversion and the postfix evaluation algorithm.
    """
    
    tokens = infix.split()
    
    prec = {'(': 1, '+': 2, '-': 2, '*': 3, '/': 3}
    
    operators = Stack()
    operands = Stack()
    
    for t in tokens:
        
        # Use .isdigit() instead to allow multi-digit integers
        if t.isdigit():
            operands.push(t)
        
        elif t == '(':
            operators.push(t)
        
        elif t == ')':
            # Pop operator stack until corresponding left parenthesis is removed
            # and evaluate
            top_operator = operators.pop()
            while top_operator != '(':
                right_op = operands.pop()
                left_op = operands.pop()
                result = do_math(top_operator, left_op, right_op)
                operands.push(result)
                top_operator = operators.pop()
        
        else:
            # Push on operator stack, but only after removing any operators
            # already on stack with higher or equal precedence
            while not operators.is_empty() and prec[operators.peek()] >= prec[t]:
                op = operators.pop()
                right_op = operands.pop()
                left_op = operands.pop()
                result = do_math(op, left_op, right_op)
                operands.push(result)
            operators.push(t)
    
    while not operators.is_empty():
        op = operators.pop()
        right_op = operands.pop()
        left_op = operands.pop()
        result = do_math(op, left_op, right_op)
        operands.push(result)
    
    return operands.pop()


def main():
    infix = '( A + B ) * C - ( D - E ) * ( F + G )'
    print('Postfix equivalent of infix {} :\n{}'.format(infix,
                                                       infix_to_postfix(infix)))
    postfix = '7 8 + 3 2 + /'
    print('Result of evaluating postfix {} :\n{}'.format(postfix,
                                                        eval_postfix(postfix)))
    infix = '10 + 3 * 5 / ( 16 - 4 )'
    print('Result of evaluating infix {} :\n{}'.format(infix,
                                                      eval_infix(infix)))


if __name__ == '__main__':
    main()