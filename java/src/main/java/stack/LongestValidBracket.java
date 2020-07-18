package main.java.stack;

import java.util.Stack;

/**
 * 题目描述：　给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
 */
public class LongestValidBracket {
    /*
     * 解题思路１：　使用两个计数器left和right，首先，从左到右遍历字符串，对遇到的每个'('，增加left计数，　对于遇到的每个')'，增加right计数，
            * 每当当前left和right计数相等时，计算当前有效字符串的长度，并且记录当前最长的字符串长度，当right大于left时，将left和right计数同时置为０．
            * 上述情况有一个弊端就是，只能针对右括号多于左括号的情况使用，我们还需要考虑左括号多余右括号的情况。
            * 就是从右往左遍历，每当当前left和right计数相等时，计算当前有效字符串的长度，并且记录当前最长的字符串长度，当left大于right时，将left和right计数同时置为０
    */
    private static int longestValidParentheses(String s) {
        int left = 0, right =0 , maxLength = 0;
        for(int i = 0; i < s.length(); i ++) {
            if (s.charAt(i) == '('){
                left++;
            } else {
                right ++;
            }
            if (left == right) {
                maxLength = Math.max(maxLength, 2 * right);
            } else if (right > left) {
                left = right = 0;
            }
        }
        left = right = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            if (s.charAt(i) == '(') {
                left++;
            } else {
                right++;
            }
            if (left == right) {
                maxLength = Math.max(maxLength, 2 * left);
            } else if (left > right) {
                left = right = 0;
            }
        }
        return maxLength;
    }

    /**
     * 解题思路：　具体做法是我们始终保持栈底元素为当前已经遍历过的元素中「最后一个没有被匹配的右括号的下标」，这样的做法主要是考虑了边界条件的处理，栈里其他元素维护左括号的下标：
     *
     * 对于遇到的每个'('，我们将它的下标放入栈中
     * 对于遇到的每个')' ，我们先弹出栈顶元素表示匹配了当前右括号：
     *  -  如果栈为空，说明当前的右括号为没有被匹配的右括号，我们将其下标放入栈中来更新我们之前提到的「最后一个没有被匹配的右括号的下标」
     *  -  如果栈不为空，当前右括号的下标减去栈顶元素即为「以该右括号为结尾的最长有效括号的长度」
     * 我们从前往后遍历字符串并更新答案即可。
     *
     * 需要注意的是，如果一开始栈为空，第一个字符为左括号的时候我们会将其放入栈中，这样就不满足提及的「最后一个没有被匹配的右括号的下标」，为了保持统一，我们在一开始的时候往栈中放入一个值为 -1−1 的元素。
     * @param s　输入字符串
     * @return
     */
    private static int longestValidParentheses1(String s) {
        int ans = 0;
        Stack<Integer> stack = new Stack<>();
        stack.push(-1);
        for(int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                stack.push(i);
            } else {
                stack.pop();
                if (stack.isEmpty()) {
                    stack.push(i);
                } else {
                    ans = Math.max(ans, i - stack.peek());
                }

            }
        }
        return ans;
    }

    /**
     * 我们从前往后遍历字符串求解 \textit{dp}dp 值，我们每两个字符检查一次：
     *
     * s[i] = \text{‘)’}s[i]=‘)’ 且 s[i - 1] = \text{‘(’}s[i−1]=‘(’，也就是字符串形如 “……()”“……()”，我们可以推出：
     *
     * \textit{dp}[i]=\textit{dp}[i-2]+2
     * dp[i]=dp[i−2]+2
     *
     * 我们可以进行这样的转移，是因为结束部分的 "()" 是一个有效子字符串，并且将之前有效子字符串的长度增加了 22 。
     *
     * s[i] = \text{‘)’}s[i]=‘)’ 且 s[i - 1] = \text{‘)’}s[i−1]=‘)’，也就是字符串形如 “……))”“……))”，我们可以推出：
     * 如果 s[i - \textit{dp}[i - 1] - 1] = \text{‘(’}s[i−dp[i−1]−1]=‘(’，那么
     *
     * \textit{dp}[i]=\textit{dp}[i-1]+\textit{dp}[i-\textit{dp}[i-1]-2]+2
     * dp[i]=dp[i−1]+dp[i−dp[i−1]−2]+2
     *
     * 我们考虑如果倒数第二个 \text{‘)’}‘)’ 是一个有效子字符串的一部分（记作 sub_ssub
     * s
     * ​
     *  ），对于最后一个 \text{‘)’}‘)’ ，如果它是一个更长子字符串的一部分，那么它一定有一个对应的 \text{‘(’}‘(’ ，且它的位置在倒数第二个 \text{‘)’}‘)’ 所在的有效子字符串的前面（也就是 sub_ssub
     * s
     * ​
     *   的前面）。因此，如果子字符串 sub_ssub
     * s
     * ​
     *   的前面恰好是 \text{‘(’}‘(’ ，那么我们就用 22 加上 sub_ssub
     * s
     * ​
     *   的长度（\textit{dp}[i-1]dp[i−1]）去更新 \textit{dp}[i]dp[i]。同时，我们也会把有效子串 “(sub_s)”“(sub
     * s
     * ​
     *  )” 之前的有效子串的长度也加上，也就是再加上 \textit{dp}[i-\textit{dp}[i-1]-2]dp[i−dp[i−1]−2]。
     */
    public static int longestValidParenthesesByDp(String s) {
        int maxLength = 0;
        int[] dp = new int[s.length()];
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) == ')') {
                if (s.charAt(i-1) == '(') {
                    dp[i] = (i >= 2? dp[i-2]: 0) + 2;
                }else if((i - dp[i-1] -1) >= 0 && s.charAt(i - dp[i-1] -1) == '(') {
                    dp[i] = dp[i - 1] + ((i - dp[i - 1]) >= 2 ? dp[i - dp[i - 1] - 2] : 0) + 2;
                }
            }
            maxLength = Math.max(dp[i], maxLength);
        }
        return maxLength;
    }

    public static void main(String[] args) {
        String s = "()()))";
        int n = LongestValidBracket.longestValidParentheses(s);
        System.out.println(n);
        int n1 = LongestValidBracket.longestValidParentheses1(s);
        System.out.println(n1);
        int n2 = LongestValidBracket.longestValidParenthesesByDp(s);
        System.out.println(n2);
    }
}
