def quick_sort(a)
  pivot = lambda {|a, min, max|
    t = a[min]
    l = min
    r = max - 1
    while l < r
      while l < r && a[r] > t
        r -= 1
      end
      if l < r
        a[l] = a[r]
        l += 1
      end
      while l < r && a[l] < t
        l += 1
      end
      if l < r
        a[r] = a[l]
        r -= 1
      end
    end
    a[l] = t
    l
  }
  _sort = lambda {|a, l, r|
    return if l >= r

    mid = pivot.call(a, l, r)
    _sort.call(a, l, mid)
    _sort.call(a, mid + 1, r)
  }
  _sort.call(a, 0, a.length)
end

if __FILE__ == $PROGRAM_NAME
  a = [6, 3, 5, 1, 8, 7, 6, 9, 4, 2]
  quick_sort(a)
  p a
end