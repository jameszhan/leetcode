def permutation(a, n)
  if n.zero?
    p a
  else
    n.times do |i|
      a[n - 1], a[i] = a[i], a[n - 1]
      permutation(a, n - 1)
      a[n - 1], a[i] = a[i], a[n - 1]
    end
  end
end

if __FILE__ == $PROGRAM_NAME
  permutation([1, 2, 3], 3)
  permutation([1, 2, 3, 4], 4)
end