def sum_of_cubes(a, b)
  x = a
  sum = 0 
  while x <= b
    sum = sum + (x*x*x)
    x = x + 1
  end
  return sum
end