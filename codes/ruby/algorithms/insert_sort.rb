def insert_sort(a)
  (1...a.length).each { |i|
    curr = a[i]
    j = i - 1
    while j >= 0 && a[j] > curr
      a[j + 1] = a[j]
      j -= 1
    end
    a[j + 1] = curr
  }
end

def insert_sort2(a)
  (1...a.length).each { |i|
    curr = a[i]
    k = i - 1
    (0...i).reverse_each { |j|
      if a[j] > curr
        k = j
        a[j + 1] = a[j]
      else
        k = j + 1
        break
      end
    }
    a[k] = curr
  }
end

def insertion_sort(a)
  a.each_with_index do |e, i|
    j = i - 1
    while j >= 0
      break if a[j] <= e

      a[j + 1] = a[j]
      j -= 1
    end
    a[j + 1] = e
  end
  a
end

def bin_insert_sort(a)
  search = lambda { |a, l, r, data|
    if l < r
      mid = (l + r) / 2
      if data > a[mid]
        search.call(a, mid + 1, r, data)
      elsif data < a[mid]
        search.call(a, l, mid, data)
      else
        return mid
      end
    else
      l
    end
  }

  _search = lambda { |a, l, r, data|
    while l < r
      mid = (l + r) / 2
      if data > a[mid]
        l = mid + 1
      elsif data < a[mid]
        r = mid
      else
        return mid
      end
    end
    return l
  }

  (1...a.length).each { |i|
    curr = a[i]
    j = i
    index = _search.call(a, 0, i, curr)
    while j > index
      a[j] = a[j - 1]
      j -= 1
    end
    a[index] = curr
  }

end

if __FILE__ == $PROGRAM_NAME
  a = [6, 3, 5, 1, 8, 7, 6, 9, 4, 2]
  insert_sort(a)
  p a

  a = [6, 3, 5, 1, 8, 7, 6, 9, 4, 2]
  insert_sort2(a)
  p a

  a = [6, 3, 5, 1, 8, 7, 6, 9, 4, 2]
  insertion_sort(a)
  p a

  a = [6, 3, 5, 1, 8, 7, 6, 9, 4, 2]
  bin_insert_sort(a)
  p a
end