import copy
import datetime
import numpy as np


SAMPLE = np.array([[   7, None,    6, None, None,    1, None,    2,    8],
                   [None, None,    5, None,    3,    2,    9, None, None],
                   [None, None, None, None, None, None,    7, None, None],
                   [   9,    4, None,    2,    7, None, None, None,    6],
                   [   2, None,    8, None,    9, None,    3, None,    5],
                   [   6, None, None, None,    1,    3, None,    9,    4],
                   [None, None,    1, None, None, None, None, None, None],
                   [None, None,    2,    1,    4, None,    5, None, None],
                   [   3,    7, None,    5, None, None,    8, None,    9]])

NUMBERS = list(range(1, 10))


def load_sample():
    """Load a sample Sudoku."""
    return Sudoku(SAMPLE)


class Cell:
    """Represents a Sudoku cell."""
    
    def __init__(self):
        """
        Attributes
        ----------
        x : int, default: None
            x-coordinate of the cell.
        
        y : int, default: None
            y-coordinate of the cell.
        
        value : int, default: None
            Cell value.
        
        candidates : set, default: {1, 2, 3, 4, 5, 6, 7, 8, 9}
            Possible (valid) values for the cell when .value is None.
        """
        
        self.x = None
        self.y = None
        self.value = None
        self.candidates = set(NUMBERS)


class Sudoku:
    """Represents a Sudoku as a list of lists (rows)."""
    
    def __init__(self, a):
        
        """
        Parameters
        ----------
        a : NumPy array
        """
        self.array = a
        self._rows = [[Cell() for _ in range(9)] for _ in range(9)]
        self.cells = self._get_all_cells()
        
        # Write cell coordinates, value, and candidates
        for i in range(9):
            for j in range(9):
                self[i, j].x = i
                self[i, j].y = j
                if a[i, j] is not None:
                    self[i, j].value = a[i, j]
                    self[i, j].candidates.clear()
        
        self.empty_cells = self._get_empty_cells()
        self._update_all_candidates()
    
    def __repr__(self):
        return 'Sudoku({})'.format(repr(self.array))
    
    def __str__(self):
        # Replace None's with zeros for nicer look
        cp = copy.copy(self.array)
        cp[cp == None] = 0
        return str(cp)
    
    def __getitem__(self, index):
        """Implement array-like cell access."""
        return self._rows[index[0]][index[1]]
    
    def _get_all_cells(self):
        """Return all cells in the Sudoku as a flat list.""" 
        return [self[i, j] for i in range(9) for j in range(9)]
    
    def _get_empty_cells(self):
        """Return cells for which .value is None."""
        return [c for c in self.cells if c.value is None]
    
    def _get_column(self, j):
        """Return cells in the jth column."""
        return [self._rows[i][j] for i in range(9)]
    
    @staticmethod
    def _get_block_range(i):
        """Determine the range of block indices based on cell coordinate."""
        if i < 3:
            return range(0, 3)
        elif 3 <= i < 6:
            return range(3, 6)
        else:
            return range(6, 9)
    
    def _get_block(self, i, j):
        """Return the 3 x 3 block of cells the (i, j) cell belongs in."""
        row_range = self._get_block_range(i)
        col_range = self._get_block_range(j)
        return [self[i, j] for i in row_range for j in col_range]
    
    def _update_cell_candidates(self, i, j):
        """Update candidates for cell in the ith row, jth column."""
        # Get cells in the same row, column, or block
        check_cells = set(self[i, :]) | set(self._get_column(j)) | set(self._get_block(i, j))
        invalids = {c.value for c in check_cells} - {None}
        self[i, j].candidates -= invalids
    
    def _update_all_candidates(self):
        """Update candidates for all empty cells."""
        for c in self.empty_cells:
            self._update_cell_candidates(c.x, c.y)
    
    def _update_array(self):
        """Update values in .array."""
        self.array = np.array([c.value for c in self.cells]).reshape(9, 9)
    
    def solve(self):
        """Solve the Sudoku and print solution."""
        
        start = datetime.datetime.now()
        
        while self.empty_cells:
            # Find all cells with only one candidate
            one_cand_cells = [c for c in self.cells if len(c.candidates) == 1 and c in self.empty_cells]
            # If there is any, fill the cell and clear candidates
            if one_cand_cells:
                for c in one_cand_cells:
                    c.value = c.candidates.pop()
                # After filling all cells, update empty cells and candidates
                self.empty_cells = self._get_empty_cells()
                self._update_all_candidates()
            else:
                print('No cells with only one candidate')
                break
        # If successfully solved
        else:
            end = datetime.datetime.now()
            
            print('Puzzle:')
            print(self)
            
            print('Solved in {} seconds.'.format((end-start).microseconds / 1e6))
            print('Solution:')
            self._update_array()
            print(self)
