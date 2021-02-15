package com.zizhizhan.leetcode;

import java.util.*;

public class LC146 {

    public static void main(String[] args) {
        int[][] operators = new int[][]{
                {1, 1, 1},
                {1, 2, 2},
                {1, 3, 2},
                {2, 1},
                {1, 4, 4},
                {2, 2}
        };
        int[] result = LRU(operators, 3);
        System.out.println(Arrays.toString(result));
    }

    public static int[] LRU(int[][] operators, int k) {
        List<Integer> ans = new ArrayList<>();
        LRUCache cache = new LRUCache(k);
        for (int[] operator : operators) {
            if (operator.length == 3 && operator[0] == 1) {
                cache.put(operator[1], operator[2]);
            } else if (operator.length == 2 && operator[0] == 2) {
                ans.add(cache.get(operator[1]));
            } else {
                System.err.println("Unexpected operator: " + Arrays.toString(operator));
            }
        }

        int[] res = new int[ans.size()];
        for (int i = 0; i < res.length; i++) {
            res[i] = ans.get(i);
        }
        return res;
    }

    public static class LRUCache extends LinkedHashMap<Integer, Integer> {

        private final int capacity;

        public LRUCache(int capacity) {
            super(capacity, 0.75F, true);
            this.capacity = capacity;
        }

        @Override
        public Integer get(Object key) {
            return super.getOrDefault(key, -1);
        }

        @Override
        public Integer put(Integer key, Integer value) {
            return super.put(key, value);
        }

        @Override
        protected boolean removeEldestEntry(Map.Entry<Integer, Integer> eldest) {
            return this.size() > this.capacity;
        }
    }
}


