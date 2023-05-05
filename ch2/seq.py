from abc import ABCMeta, abstractmethod # need these definitions

class Sequence(metaclass=ABCMeta):
    """Our own version of collections.Sequence abstract base class."""

    @abstractmethod
    def __len__ (self):
        """Return the length of the sequence."""

    @abstractmethod
    def __getitem__ (self, j):
        """Return the element at index j of the sequence."""

    def __contains__ (self, val):
        """Return True if val found in the sequence; False otherwise."""
        for j in range(len(self)):
            if self[j] == val: # found match
                return True
        return False
    
    def __index__(self, val):
        """Return leftmost index at which val is found (or raise ValueError)."""
        for j in range(len(self)):
            if self[j] == val: # leftmost match
                return j
        raise ValueError( "value not in sequence" ) # never found a match
        
    def __count__(self, val):
        """Return the number of elements equal to given value."""
        k = 0
        for j in range(len(self)):
            if self[j] == val: # found a match
                k += 1
        return k
    

class Word(Sequence):

    def __init__(self, phrase) -> None:
        super().__init__()
        self.phrase = phrase

    def __len__(self):
        return  len(str.split( self.phrase, " "))
    
    def __getitem__(self, j):
        words = str.split( self.phrase, " ")
        return words[j]
    

phrase = Word("this is my first phrase")

print(len(phrase))
print(phrase[1])