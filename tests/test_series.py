from math_series import __version__
from math_series.series import fibonacci, lucas, series_calc

def test_version():
  assert __version__ == '0.1.0'

def test_fibonacci():
  actual = fibonacci(9)
  expected = 21
  assert actual == expected
  
def test_lucas():
  actual = lucas(9)
  expected = 76
  assert actual == expected

def test_series_calc():
  actual = series_calc(9, 2, 1)
  expected = 76
  assert actual == expected
  