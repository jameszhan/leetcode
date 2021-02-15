def fibonacci(n)
  sqrt5 = Math.sqrt(5)
  c1 = (1 + sqrt5) / 2
  c2 = (1 - sqrt5) / 2
  ((c1 ** n - c2 ** n) / sqrt5).floor
end

def fibonacci2(n)
  if [0, 1].include?(n)
    n
  else
    fibonacci2(n - 1) + fibonacci2(n - 2)
  end
end

def fibonacci3(n)
  if n < 2
    n
  else
    x = 1
    y = 0
    (2..n).each do |_i|
      x, y = y, x
      x += y
    end
    x
  end
end

if __FILE__ == $PROGRAM_NAME

  p Array(1..20).map { |i| fibonacci(i) }
  p Array(1..20).map { |i| fibonacci2(i) }
  p Array(1..20).map { |i| fibonacci3(i) }

end