package main.java.nums;

import java.util.HashMap;
import java.util.Map;

public class TwoSum1 {

    public static int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>(16);
        for(int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if(map.containsKey(complement)) {
                return new int[] {map.get(complement), i};
            }
            map.put(nums[i], i);
        }
        return new int[] {-1, -1};
    }

    public static void main(String[] args) {
        int[] arr = new int[4];
        arr[0] = 2;
        arr[1] = 7;
        arr[2] = 11;
        arr[3] = 15;
        int target = 9;
        int[] afterArr = TwoSum1.twoSum(arr, target);
//        for(int i = 0; i < afterArr.length; i ++) {
//            System.out.println(afterArr[i]);
//        }
        System.out.println(afterArr);
    }

}
