
def bubble_sort(a)
  (0...a.length).each {|i|
    swapped = false
    (i...a.length).reverse_each {|j|
      if a[j - 1] > a[j]
        a[j - 1], a[j] = a[j], a[j - 1]
        swapped = true
      end
    }
    break unless swapped
  }
end

def bubble_sort2(a)
  (0...a.length).each {|i|
    swapped = false
    (0...a.length - i - 1).each {|j|
      if a[j] > a[j + 1]
        a[j], a[j + 1] = a[j + 1], a[j]
        swapped = true
      end
    }
    break unless swapped
  }
end

def bubble_sort3(a)
  cur = 0
  loop {
    swapped = false
    (a.size - 2).downto(cur) do |i|
      if a[i + 1] < a[i]
        a[i + 1], a[i] = a[i], a[i + 1]
        swapped = true
      end
    end
    break unless swapped
  }
  a
end

if __FILE__ == $PROGRAM_NAME

  a = [6, 3, 5, 1, 8, 7, 6, 9, 4, 2]
  bubble_sort(a)
  p a

  a = [6, 3, 5, 1, 8, 7, 6, 9, 4, 2]
  bubble_sort2(a)
  p a

  a = [6, 3, 5, 1, 8, 7, 6, 9, 4, 2]
  bubble_sort3(a)
  p a

end