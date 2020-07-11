package main.java.nums;

/**
 * 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
 *
 * 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
 *
 *  
 *
 * 示例 1:
 *
 * 输入: [3,2,3]
 * 输出: 3
 * 示例 2:
 *
 * 输入: [2,2,1,1,1,2,2]
 * 输出: 2
 *
 * 来源：力扣（LeetCode）
 * 链接：https://leetcode-cn.com/problems/majority-element
 * 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
 */

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

/**
 * 解题思路，对数组进行排序，返回中间位置的元素
 */
public class MajorityElement169 {

    private static Integer majorityElement(int[] nums) {
        if (nums == null || nums.length == 0) return -1;
        Map<Integer, Integer> map = new HashMap<>(8);
        for(int num : nums) {
            map.merge(num, 1, (a, b) -> a + b);
        }
        Set<Integer> keySet = map.keySet();
        //创建set集合的迭代器
        for (Integer key : keySet) {
            Integer value = map.get(key);
            if (value > nums.length / 2) return key;
        }
        return -1;
    }

    private static Integer majorityElementSort(int[] nums) {
        if (nums == null || nums.length == 0) return -1;
        Arrays.sort(nums);
        return nums[nums.length / 2];
    }

    private static int majorityElementMore(int[] nums) {
        if (nums == null || nums.length == 0) return -1;
        int candidate = nums[0];
        int count = 0;
        for(int i=1; i < nums.length; i ++) {
            if(candidate == nums[i]) {
                count += 1;
            }
            else if (count == 0) {
                candidate = nums[i];
                count = 0;
            }
            count -= 1;
        }
        return candidate;
    }

    public static void main(String[] args) {
        int[] nums = new int[]{2, 2, 1, 1, 1, 1, 1};
        int res = MajorityElement169.majorityElement(nums);
        System.out.println(res);
        int res1 = MajorityElement169.majorityElementMore(nums);
        System.out.println(res1);


    }
}
