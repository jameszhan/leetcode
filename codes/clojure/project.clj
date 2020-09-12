(defproject leetcode "0.1.0-SNAPSHOT"
  :description "LeetCode Online Judge"
  :url "https://github.com/jameszhan/leetcode"
  :license {:name "Eclipse Public License"
            :url "http://www.eclipse.org/legal/epl-v10.html"}
  :dependencies [[org.clojure/clojure "1.6.0"]]
  :main ^:skip-aot leetcode.core
  :target-path "target/%s"
  :profiles {:uberjar {:aot :all}})

