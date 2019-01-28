from linear_data_structure import Stack, Queue


class HTMLTag:
    """Represents an HTML tag."""
    
    def __init__(self, name, closing):
        """
        Parameters
        ----------
        name : str
            Tag name.
        
        closing : bool
            Whether the tag is a closing tag or not.
        """
        
        self.name = name
        self.closing = closing


class HTMLChecker:
    """Class that checks an HTML document for proper opening and closing tags."""
    
    def __init__(self):
        
        # Stack to store characters
        self.c_stack = Stack()
        # Stack to store tags
        self.t_stack = Stack()
    
    def check(self, html):
        
        # Scan the HTML from left to right
        for c in html:
            
            # Upon seeing a greater than sign, pop character stack until the
            # corresponding less than sign is removed
            if c == '>':
                top_char = self.c_stack.pop()
                tmp = Queue()
                while top_char not in '</':
                    tmp.enqueue(top_char)
                    top_char = self.c_stack.pop()
                # Create tag name
                name = ''.join(tmp.items)
                
                # If start tag, push to tag stack
                if top_char == '<':
                    tag = HTMLTag(name, False)
                    self.t_stack.push(tag)
                # If end tag, pop the last tag and check whether tag names match
                else:
                    last_tag = self.t_stack.pop()
                    if name != last_tag.name:
                        return False
            
            else:
                self.c_stack.push(c)
        
        return True


def main():
    
    html = """
<html>
  <head>
    <title>
      Example
    </title>
  </head>

  <body>
    <h1>Hello, world</h1>
  </body>
</html>
"""
    
    checker = HTMLChecker()
    print('Checking HTML :\n', html)
    print('Result :', checker.check(html))


if __name__ == '__main__':
    main()