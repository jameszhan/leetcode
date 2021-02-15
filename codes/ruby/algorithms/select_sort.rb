
def select_sort(a)
  (0...a.length).each{|i|
    k = i
    (i + 1...a.length).each{|j|
      k = j if a[k] > a[j]
    }

    a[k], a[i] = a[i], a[k] if k != i
  }
end

def selection_sort(a)
  (0...a.length).reverse_each{|i|
    k = i
    (0...i).each{|j|
      k = j if a[k] < a[j]
    }

    a[k], a[i] = a[i], a[k] if k != i
  }
end


if __FILE__ == $PROGRAM_NAME
  a = [6, 3, 5, 1, 8, 7, 6, 9, 4, 2]
  select_sort(a)
  p a

  a = [6, 3, 5, 1, 8, 7, 6, 9, 4, 2]
  selection_sort(a)
  p a
end
