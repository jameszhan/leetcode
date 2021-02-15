# encoding: UTF-8

# 百钱买百鸡的问题算是一套非常经典的不定方程的问题，
# 题目很简单：
# 公鸡5文钱一只，母鸡3文钱一只，小鸡3只一文钱，用100文钱买一百只鸡,其中公鸡，母鸡，小鸡都必须要有，问公鸡，母鸡，小鸡要买多少只刚好凑足100文钱。

# (5x + 3y + z/3) = 100
# (x + y + z) = 100
# 0 < x < 20, 0 < y < 33, z > 0
def count_chicken
  (1...20).each do |x|
    (1...33).each do |y|
      z = 100 - x - y
      puts "x = #{x}, y = #{y}, z = #{z}" if 5 * x + 3 * y + z * 1.0 / 3 == 100
    end
  end
end

# (x + y + z) = 100       ①
# (5x + 3y + z/3) = 100   ②
# 3②-① => 7x + 4y = 100 => y = 25 - 7x/4
# We can set x = 4k => y = 25 - 7k && z = 75 + 3k
# 0 < x, y, z < 100 => 1 <= k <= 3
def count_chickens
  (1..3).each do |k|
    x = 4 * k
    y = 25 - 7 * k
    z = 75 + 3 * k
    puts "x = #{x}, y = #{y}, z = #{z}"
  end
end

if __FILE__ == $PROGRAM_NAME
  count_chicken
  count_chickens
end
