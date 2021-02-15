def pi(n)
  k = 0
  n.times {
    x = Random.rand
    y = Random.rand
    k += 1 if x * x + y * y <= 1
  }
  4 * k * 1.0 / n
end

if __FILE__ == $PROGRAM_NAME
  [1_000_000, 10_000_000, 100_000_000].each{ |i| p pi(i) }
end
