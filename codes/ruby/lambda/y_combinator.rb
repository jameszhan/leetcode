# Define the Y combinator
module YCombinator
  def y_comb(&gen)
    proc { |f|
      proc { |*args|
        gen.call(f.call(f)).call(*args)
      }
    }.call(proc { |f|
      proc { |args|
        gen.call(f.call(f)).call(*args)
      }
    })
  end

  def y(&gen)
    lambda {|g| g[g] }.call(lambda{|f| lambda {|*args| gen[f[f]][*args] }})
  end


  def y_combinator(&gen)
    lambda {|&u| u.call(&u)}.call do |&f|
      gen.call(&lambda {|*args| f.call(&f).call(*args)})
    end
  end
end

# Give the y_comb function to all objects
class Object
  include(YCombinator)
end


hash = y_comb { |callback|
  proc {
    Hash.new { |h, k| h[k] = callback.call }
  }
}.call

# Now this will work:
hash['a']['b']['c']['d']['e']['f']['g'] = 1

# And hash looks like:
puts hash   # => {"a"=>{"b"=>{"c"=>{"d"=>{"e"=>{"f"=>{"g"=>1}}}}}}}


ret = y_combinator do |&fab|
  lambda {|n| n.zero? ? 1: n * fab[n-1]}
end[10]
puts ret

factorial = y do |recurse|
  lambda do |x|
    x.zero? ? 1 : x * recurse[x-1]
  end
end
puts factorial.call(10)

fac = y_combinator do|&f|
  lambda{|n| n.zero? ? 1 : n * f.call(n - 1)}
end
puts fac.call(10)
