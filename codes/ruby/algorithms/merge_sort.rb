def merge_sort(a)
  merge = lambda {|a, l, m, r|
    i, j, t, k = l, m + 1, [], 0
    while i <= m && j <= r
      if a[i] > a[j]
        t[k] = a[j]
        k, j = k + 1, j + 1
      else
        t[k] = a[i]
        k, i = k + 1, i + 1
      end
    end
    if i > m
      while j <= r
        t[k] = a[j]
        k, j = k + 1, j + 1
      end
    else
      while i <= m
        t[k] = a[i]
        k, i = k + 1, i + 1
      end
    end
    i, k = l, 0
    while i <= r
      a[i] = t[k]
      k, i = k + 1, i + 1
    end
  }
  sort = lambda {|a, l, r|
    if l < r
      m = (l + r) / 2
      sort.call(a, l, m)
      sort.call(a, m + 1, r)
      merge.call(a, l, m, r)
    end
  }
  sort.call(a, 0, a.length - 1)
end

def merge_sort2(a)
  merge = lambda {|src, dst, k|
    s1, s2, m, n = 0, k, 0, src.length
    while s1 + k < n
      e1, e2 = s2, (s2 + k < n) ? s2 + k : n
      i, j = s1, s2
      while i < e1 && j < e2
        if src[i] <= src[j]
          dst[m] = src[i]
          i += 1
        else
          dst[m] = src[j]
          j += 1
        end
        m += 1
      end
      while i < e1
        dst[m] = src[i]
        m, i = m + 1, i + 1
      end
      while j < e2
        dst[m] = src[j]
        m, j = m + 1, j + 1
      end
      s1 = e2
      s2 = s1 + k
    end
    dst.each_with_index {|e, i|src[i] = e}
  }
  k = 1
  while k < a.length
    merge.call(a, [], k)
    k <<= 1
  end
end

if __FILE__ == $PROGRAM_NAME
  a = [6, 3, 5, 1, 8, 7, 6, 9, 4, 2]
  merge_sort(a)
  p a

  a = [6, 3, 5, 1, 8, 7, 6, 9, 4, 2]
  merge_sort2(a)
  p a
end
