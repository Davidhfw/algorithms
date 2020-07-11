package main.java.nums;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ThreeSum16 {

    public static List<List<Integer>> threeSum(int[] arr, int target) {
        if (arr == null) {
            return new ArrayList<>();
        } else if (arr.length < 3) {
            return new ArrayList<>();
        }
        // 数组排序
        Arrays.sort(arr);
        List<List<Integer>> res = new ArrayList<List<Integer>>(16);
        int arrLen = arr.length;
        for(int i = 0; i < arrLen - 2; i ++) {
            if (i > 0 && arr[i] == arr[i-1]) {
                continue;
            }
            int left = i + 1;
            int right = arrLen - 1;
            while(left < right) {
                int curSum = arr[i] + arr[left] + arr[right];
                if (curSum == target) {
                    List<Integer> lst = new ArrayList<>(16);
                    lst.add(arr[i]);
                    lst.add(arr[left]);
                    lst.add(arr[right]);
                    res.add(lst);
                    while(left < right && arr[left] == arr[left + 1]) {
                        left += 1;
                    }
                    while (left < right && arr[right] == arr[right - 1]) {
                        right -= 1;
                    }
                    left += 1;
                    right -= 1;
                } else if(curSum < target) {
                    left +=1;
                } else {
                    right -=1;
                }
            }
        }
    return res;
    }
    public static void main(String[] args) {
        int[] arr = new int[6];
        arr[0] = -1;
        arr[1] = 0;
        arr[2] = 1;
        arr[3] = 2;
        arr[4] = -1;
        arr[5] = -4;
        int target = -5;
        System.out.println(ThreeSum16.threeSum(arr, target));
    }
}
