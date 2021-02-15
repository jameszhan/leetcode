# 猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾就多吃了一个。
# 第二天早上又将剩下的桃子吃了一半，还是不过瘾又多吃了一个。
# 以后每天都吃前一天剩下的一半再加一个。到第10天刚好剩一个。问猴子第一天摘了多少个桃子？
# f(n)/2 -1 = f(n + 1) => f(n) = (f(n + 1) + 1) * 2
def sum_peach(day, total)
  if day == 1
    total
  else
    sum_peach(day - 1, 2 * total + 2)
  end
end

if __FILE__ == $PROGRAM_NAME
  puts sum_peach(10, 1)
  puts sum_peach(20, 1)
end
