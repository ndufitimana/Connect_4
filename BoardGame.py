"""
This board game base class was obtained from Professor Lisa Meeden
of Swarthmore College Computer Science Department.
https://www.cs.swarthmore.edu/~meeden/  
"""

RED = u"\033[1;31m"
YELLOW = u"\033[1;33m"
RESET = u"\033[0;0m"
CIRCLE = u"\u25CF"

RED_DISK = RED + CIRCLE + RESET
YELLOW_DISK = YELLOW + CIRCLE + RESET


class _base_game:
    def __repr__(self):
        if self._repr is None:
            self._repr = "\n".join(" ".join(map(self._print_char, row)) for row in self.board)
            self._repr += "   " + self._print_char(self.turn) + " to move\n"
        return self._repr

    def __hash__(self):
        if self._hash is None:
            self._hash = hash(repr(self))
        return self._hash

    def _print_char(self, i):
        if i > 0:
            return YELLOW_DISK
        if i < 0:
            return RED_DISK
        return u'\u00B7'  # empty cell