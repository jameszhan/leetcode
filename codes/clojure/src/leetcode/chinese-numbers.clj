
(def digits-name (zipmap "0123456789" "零一二三四五六七八九"))
(def tens-name (zipmap [1 2 3] [\十 \百 \千]))
(defn digit-pos-to-name [pos]
  (cond (= pos 0) nil
    (= 0 (rem pos 8)) \亿
    (= 0 (rem pos 4)) \万
    :else (tens-name (rem pos 4))))
(def unit-rank (zipmap [nil \十 \百 \千 \万 \亿] (range 6)))

(defn append-digit [[results pending-zero last-unit] tuple]
  (let [digit (first tuple)
        this-unit (second tuple)
        this-str (digits-name digit)]
    (if (= digit \0)
      (if (> (unit-rank last-unit) (unit-rank this-unit))
        [results true last-unit]
        [(conj results this-unit) false this-unit])
      [(conj results (if pending-zero \零) this-str this-unit)
       false this-unit])))

(defn to-chinese-num [n]
  (apply str (first (reduce append-digit [[] false nil]
                      (reverse (map-indexed #(list %2 (digit-pos-to-name %1))
                                 (reverse (str n))))))))

(println (to-chinese-num 64703))
(println (to-chinese-num 6470377))
(println (to-chinese-num 500632))
(println (to-chinese-num 50063247))