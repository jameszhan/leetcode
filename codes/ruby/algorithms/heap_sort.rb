def heap_sort(a)
  parent = ->(i) { (i - 1) / 2 }
  left = ->(i) { 2 * i + 1 }
  right = ->(i) { 2 * i + 2 }

  adjust = lambda { |a, i, n|
    k, j = a[i], left.call(i)
    while j < n
      if j < n - 1 && a[j + 1] > a[j]
        j += 1
        #if we want adjust it to minimal root heap, just change condition to a[j + 1] < a[j]
      end

      if k < a[j]
        a[parent.call(j)] = a[j]
        #find max child element and put it to parent node.
        j = left.call(j)
      else
        break
      end
    end
    a[parent.call(j)] = k
  }

  n = a.length
  (0..parent.call(n - 1)).reverse_each { |i|
    adjust.call(a, i, n)
  }

  #Big root heap stragegy
  (1...n).reverse_each { |i|
    a[i], a[0] = a[0], a[i]
    adjust.call(a, 0, i)
  }

  #Small root heap stragegy
  #    (1...n).each{|i|
  #      adjust.call(++a, 0, n - i)
  #How can us deal with ++pointer in ruby.
  #    }
end

if __FILE__ == $PROGRAM_NAME

  a = [6, 3, 5, 1, 8, 7, 6, 9, 4, 2]
  heap_sort(a)
  p a

end