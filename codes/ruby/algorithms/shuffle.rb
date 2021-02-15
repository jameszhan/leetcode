def shuffle(a)
  n = a.length
  (0...n).each do |i|
    j = Random.rand(i...n)
    a[i], a[j] = a[j], a[i]
  end
end

if __FILE__ == $0
  a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
  shuffle(a)
  p a
end

