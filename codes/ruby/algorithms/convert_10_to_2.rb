def convert_10_to_2(num, ret)
  return if num.zero?

  convert_10_to_2(num / 2, ret)
  ret << num % 2
end

ret = []
convert_10_to_2(10, ret)
p ret.join('')



if __FILE__ == $PROGRAM_NAME
  puts(ackerman(3, 3))
  puts(ackerman(3, 4))
end
