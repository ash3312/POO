class Progression:

    def __init__(self, value=0) -> None:
        self._current = value

    def _advance(self):
        self._current += 1

    def __next__(self):
        if self._current is None:
            raise StopIteration("progression stopped")
        curr = self._current
        self._advance()
        return curr

    def __iter__(self):
        return self

p = Progression(0)
print(p._current)

for i in range(5):
    print(p._current)
    next(p)
print(p._current)