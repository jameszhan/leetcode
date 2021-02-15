#  LCG(linear congruential generator)
# => The heart of an LCG is the following formula
# =>  X(i+1) = (a * X(i) + c) mod M
# =>  where
# =>    M is the modulus.         M > 0.
# =>    a is the multiplier,      0 <= a < M.
# =>    c is the increment,       0 <= c < M.
# =>    X(0) is the seed value,   0 <= X(0) < M.
# =>    i is the iterator.        i < M
def lcg_rand(m = 8)
  a = 5
  c = 3
  x = 1
  lambda do
    x = (a * x + c) % m
    x
  end
end

if __FILE__ == $PROGRAM_NAME
  rand = lcg_rand
  (1..20).each { |_i| p rand.call }
end


