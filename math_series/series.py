def fibonacci(num):
  """
  Arguments:
  num - user-selected sequence value from the Fibonacci sequence to be calculated by the funciton

  Returns:
  Calculated value from the sequence
  """

  if num <= 0:
    print('Value too small.')
  elif num == 1:
    return 0 
  elif num == 2:
    return 1
  else:
    return fibonacci(num-1) + fibonacci(num-2)

def lucas(num):
  """
  Arguments:
  num - user-selected sequence value from the Lucas sequence to be calculated by the funciton

  Returns:
  Calculated value from the sequence
  """
  if num == 0:
    return 2
  if num == 1:
    return 1
  return lucas(num-1) + lucas(num-2)

def series_calc(num, x=0, y=1):
  """
  Arguments:
  num - user-selected sequence value from the special number sequence (e.g. Fibonacci, Lucas) to be calculated by the funciton
  x - the lower bound number calculating the progression of the special number sequence
  y - the upper bound number calculating the progression of the special number sequence
  Returns:
  Calculated value from the sequence
  """
  if x == 0 and y == 1:
    if num - 1 == 0:
      return x
    if num - 1 == 1:
      return y
    return series_calc(num - 1, x, y) + series_calc(num - 2, x, y)
  else:
    if num == 0:
      return x
    if num == 1:
      return y
    return series_calc(num - 1, x, y) + series_calc(num - 2, x, y)