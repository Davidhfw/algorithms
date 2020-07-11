package main.java.nums;



import java.util.*;

/**
 * 解题思路：使用摩尔投票法的升级版来解决这个问题，先来简单看看摩尔投票法的基本原理
 * 摩尔投票法：首先我们得明确，n/k的众数最多只有k-1个，为什么呢？假设有k个众数，n/k * k=n,这k个元素都是众数，还要不同，怎么可能啊。那么对于这个题，超过n/3的数最多只能有3-1 = 2 个，我们可以先选出两个候选人A,B。 遍历数组，分三种情况：
 *
 * 候选1：> n/3
 * 候选2：> n/3
 * 其他：< n/3
 * 写代码三步走
 * 1、如果投A（当前元素等于A），则A的票数++;
 * 2、如果投B（当前元素等于B），B的票数++；
 * 3、如果A,B都不投（即当前与A，B都不相等）,那么检查此时A或B的票数是否减为0，如果为0,则当前元素成为新的候选人；如果A,B两个人的票数都不为0，那么A,B两个候选人的票数均减一。
 *
 * 最后会有这么几种可能：有2个大于n/3，有1个大于n/3，有0个大于n/3
 * 遍历结束后选出了两个候选人，但是这两个候选人是否满足>n/3，还需要再遍历一遍数组，找出两个候选人的具体票数，因为题目没有像169题保证一定有。
 */
public class MajorityElementII229 {
    private static List<Integer> MajorityElementII(int[] nums) {
        //返回值
        List<Integer> res = new ArrayList<>(4);
        if(nums == null || nums.length == 0) return res;
        //初始化两个候选人和得票数
        int candidate1 = nums[0];
        int count1 = 0;
        int candidate2 = nums[0];
        int count2 = 0;
        //摩尔投票法，分为配对和计数阶段，配对阶段主要是挑选出比较有潜力的票数超过莫个数，技术阶段就是对这几个候选人分别计数，
        // 挑选出其中得票数超过题目规定的个数
        // 配对阶段
        for(int num: nums) {
            if (candidate1 == num) {
                count1 += 1;
            }
            if(candidate2 == num) {
                count2 += 1;
            }
            //第一个候选人配对
            if(count1 == 0) {
                candidate1 = num;
                count1 += 1;
            }
            //第二个候选人配对
            if(count2 == 0) {
                candidate2 = num;
                count2 += 1;
            }
            count1 --;
            count2 --;
        }
        count1 = 0;
        count2 = 0;
        for(int num: nums) {
            if(candidate1 == num) {
                count1 ++;
            } else if(candidate2 == num) {
                count2 ++;
            }
        }
        if(count1 > nums.length / 3) res.add(candidate1);
        if(count2 > nums.length / 3) res.add(candidate2);
        return res;
    }

    /**
     * 求众数，使用hashmap
     * @param nums 输入数字
     * @return
     */
    private static List<Integer> MajorityElementIIUsedMap(int[] nums) {
        //返回值
        List<Integer> res = new ArrayList<>(4);
        if(nums == null || nums.length == 0) return res;
        Map<Integer, Integer> map = new HashMap<>(8);
        for(int num : nums) {
            map.merge(num, 1, (a, b) -> a + b);
        }
        Set<Integer> keySet = map.keySet();
        //创建set集合的迭代器
        for (Integer key : keySet) {
            Integer value = map.get(key);
            if (value > nums.length / 3) res.add(key);
        }
        return res;
    }
    public static void main(String[] args) {

        int[] arr = new int[3];
        arr[0] = 3;
        arr[1] = 2;
        arr[2] = 3;
        List<Integer> ret = MajorityElementII229.MajorityElementII(arr);
        for(Integer integer : ret) {
            System.out.println(integer);
        }
        List<Integer> ret1 = MajorityElementII229.MajorityElementIIUsedMap(arr);
        for(Integer integer : ret1) {
            System.out.println(integer);
        }

    }
}
