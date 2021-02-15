
def reverse_input
  c = gets
  reverse_input if c != "\n"
  p c
end

reverse_input if __FILE__ == $PROGRAM_NAME