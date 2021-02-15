# LCG 算法数学上基于公式：
# X(n+1) = (a * X(n) + c) % m
# 其中，各系数为：
# 模m, m > 0
# 系数a, 0 < a < m
# 增量c, 0 <= c < m
# 原始值(种子) 0 <= X(0) < m
# 其中参数c, m, a比较敏感，或者说直接影响了伪随机数产生的质量。
# 一般而言，高LCG的m是2的指数次幂(一般2^32或者2^64)，因为这样取模操作截断最右的32或64位就可以了。多数编译器的库中使用了该理论实现其伪随机数发生器rand()。
# 如果以下三个条件都满足，则可以让该随机数序列的周期等于M
# c和M互质。
# 对于M的任何一个质因子P，a-1能被P整除。
# 如果4是M的因子，则a除以4余1。
# 
def rand(m)
  r = 1
  a = 5
  c = 7
  lambda {
    r = (r * a + c) % m
  }
end

if __FILE__ == $PROGRAM_NAME
  rnd = rand(16)
  1000.times { print rnd.call, ',' }
end
