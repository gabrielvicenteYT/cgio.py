# cgio.py
Utility for testing [code-golf.io](https://code-golf.io) python solutions using python's [unittest](https://docs.python.org/3/library/unittest.html) framework.

## Examples

[Divisors hole](https://code-golf.io/divisors):

```python
from cgio import TestCase, answers

class DivisorsTest(TestCase):
    def test(self):
        with self.assertOutput(answers.divisors):
            for i in range(1, 101):
                print(' '.join(str(j) for j in range(1, i + 1) if i % j == 0))
```

[Quine hole](https://code-golf.io/quine):

```python
from cgio import TestCase

class QuineTest(TestCase):
    def test(self):
        self.assertQuine("""w="print('w='+chr(34)+w+chr(34)+chr(10)+w)"
print('w='+chr(34)+w+chr(34)+chr(10)+w)""")
```
