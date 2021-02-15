def ackerman(m, n)
  if m.zero?
    n + 1
  elsif n.zero?
    ackerman(m - 1, 1)
  else
    ackerman(m - 1, ackerman(m, n - 1))
  end
end


if __FILE__ == $PROGRAM_NAME
  puts(ackerman(3, 3))
  puts(ackerman(3, 4))
end

