def convert_10_to_2(num, ret)
  return if num.zero?

  convert_10_to_2(num / 2, ret)
  ret << num % 2
end

if __FILE__ == $PROGRAM_NAME
  ret = []
  convert_10_to_2(10, ret)
  p ret.join('')
end
