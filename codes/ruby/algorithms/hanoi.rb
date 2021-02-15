def hanoi(n, src, dst, mid, &handle)
  if n > 1
    hanoi(n - 1, src, mid, dst, &handle)
    handle.call(n, src, dst)
    hanoi(n - 1, mid, dst, src, &handle)
  else
    handle.call(n, src, dst)
  end
end

if __FILE__ == $PROGRAM_NAME
  puts '==========>'
  hanoi(6, 'A', 'C', 'B'){|n, src, dst| puts "move #{n} from #{src} to #{dst}"}
  i = 0
  hanoi(6, 'A', 'C', 'B'){|n, src, dst| i += 1}
  puts i
  puts '==========>'
  hanoi(3, 'A', 'C', 'B'){|n, src, dst| puts "move #{n} from #{src} to #{dst}"}
  i = 0
  hanoi(3, 'A', 'C', 'B'){|n, src, dst| i += 1}
  puts i
end
