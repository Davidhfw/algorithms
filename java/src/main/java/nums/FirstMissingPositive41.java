package main.java.nums;

import java.util.HashSet;
import java.util.Set;

public class FirstMissingPositive41 {

    public static int firstMissingPositive(int[] nums) {
        int len = nums.length;
        Set<Integer> hashSet = new HashSet<>(10);
        for(int num: nums) {
            hashSet.add(num);
        }
        for(int i = 1; i <= len; i++) {
            if(!hashSet.contains(i)) {
                return i;
            }
        }
        return len + 1;
    }

    public static int firstMissingPositive1(int[] nums) {
        int len = nums.length;
        for(int i = 0; i < len; ++i) {
            if (nums[i] <= 0) {
                nums[i] = len + 1;
            }
        }

        for(int i = 0; i < len; ++i) {
            int num = Math.abs(nums[i]);
            if(num < len+1) {
                nums[num - 1] = -Math.abs(nums[num - 1]);
            }
        }
        for(int i = 0; i < len; i ++) {
            if(nums[i] > 0) {
                return i + 1;
            }
        }
        return len + 1;
    }

    public static void main(String[] args) {
        int[] nums = new int[] {1, 2, 0};
        int n = FirstMissingPositive41.firstMissingPositive(nums);
        System.out.println(n);
        int n1 = FirstMissingPositive41.firstMissingPositive1(nums);
        System.out.println(n1);
    }
}
