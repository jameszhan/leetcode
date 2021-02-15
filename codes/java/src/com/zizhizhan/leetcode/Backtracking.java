package com.zizhizhan.leetcode;

import java.util.Arrays;

/**
 * Created with IntelliJ IDEA.
 *
 * @author James Zhan
 * Date: 11/3/13
 * Time: 5:01 PM
 */
public class Backtracking {


    public static void dfs(char[] args, int pos) {
        for (int i = 0; i < args.length; i++) {
            char c = (char) (65 + i);
            if (check(args, c, pos)) {
                args[pos] = c;
                if (pos == args.length - 1) {
                    print(args);
                } else {
                    dfs(args, pos + 1);
                }
            }
        }
    }

    public static void backtracking(int len) {
        int[] a = new int[len];
        Arrays.fill(a, -1);
        int k = 0;
        while (k >= 0) {
            a[k]++;
            while (a[k] < len && !check(a, k)) {
                a[k]++;
            }
            if (a[k] == len) {
                k--;
            } else {
                if (k == len - 1) {
                    for (int c : a) {
                        System.out.print((char) (c + 65) + "        ");
                    }
                    System.out.println();
                } else {
                    k++;
                    a[k] = -1;
                }
            }
        }
    }

    public static boolean check(int[] a, int pos) {
        for (int i = 0; i < pos; i++) {
            if (a[pos] == a[i]) {
                return false;
            }
        }
        return true;
    }

    public static void backtracking2(int len) {
        int[] arr = new int[len];
        Arrays.fill(arr, -1);
        int pos = 0;
        while (pos >= 0) {
            arr[pos]++;
            if (!check(arr, arr[pos], pos)) {
                pos--;
            }
            if (arr[pos] == len) {
                arr[pos] = -1;
                pos--;
            } else if (pos == len - 1) {
                for (int c : arr) {
                    System.out.print((char) (c + 65) + "        ");
                }
                System.out.println();
            } else {
                pos++;
            }
        }
    }

    public static boolean check(int[] args, int c, int pos) {
        for (int i = 0; i < pos; i++) {
            if (c == args[i]) {
                return false;
            }
        }
        return true;
    }

    public static boolean check(char[] args, char c, int pos) {
        for (int i = 0; i < pos; i++) {
            if (c == args[i]) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        char[] arr = {'A', 'B', 'C', 'D'};
        dfs(arr, 0);

        backtracking(5);
    }

    public static void print(char[] args) {
        for (char c : args) {
            System.out.print(c);
        }
        System.out.println();
    }
}
