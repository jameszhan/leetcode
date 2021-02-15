
def bin_search(a, l, r, data)
  search = lambda{|a, l, r, data|
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
  search.call(a, l, r, data)
end

def bin_search2(a, l, r, data)
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
  -1
end

if __FILE__ == $PROGRAM_NAME

  a = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9]
  p bin_search(a, 0, 9, 3)
  p bin_search2(a, 0, 9, 3)
end
