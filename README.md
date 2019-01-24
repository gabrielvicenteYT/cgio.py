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
