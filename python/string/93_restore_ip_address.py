# -*-coding:utf-8 -*-
"""
FileName: restore_ipv4.py
Author: raphealwu
Date: 2021/2/23 11:22 下午
"""
"""
题目描述：给定一个只包含数字的字符串，用以表示一个 IP 地址，返回所有可能从 s 获得的 有效 IP 地址 。你可以按任何顺序返回答案
解题思路：
以"25525511135"为例，做第一步时我们有如下选择
1 选2作为第一个字段
2 选25作为第一个字段
3 选255作为第一个字段
这样就能切分三种不同长度，切第二个片段时，有面临三种选择
这会向下分支成一棵树，我们用dfs去遍历所有选择，必要时提前结束回溯
回溯的约束条件
1 一个片段的长度是1～3
2 片段的范围是0-255
3 不能是0x，0xx，也就是说0只能单独作为一个字段
目标
1 决定什么时候砍掉分支
2 生成4个有效片段，而且要将字符串使用完
3 满足2中条件时，将结果加入结果集中
4 如果满足4个片段，但是字符串还没有被用光，则直接返回，表明不是合理的解

"""

def restoreIpAddresses(s):
    res = []
    def dfs(sub_res, start, s):
        # 回溯从start开始的子串
        if len(sub_res) == 4:
            if start == len(s):
                # 条件1: 满四段且用光所有字符
                ans = '.'.join(sub_res)
            # 四段拼一起，返回列表中
                res.append(ans)
            elif start < len(s):
            # 条件2:满四段，但没用光所有字符
                return
        # 三种长度选择
        for i in range(3):
            # 字符不存在，超出边界了
            if start >= len(s):
                return
            if len(s[start:start + i + 1]) > 1 and s[start] == '0':
                # 长度超过2的子串不能是‘0’开头
                return
            # 当前切出来字符
            path = s[start:start + 1 + i]
            # 字符串长度为3时，大小不能超过255
            if i == 2 and int(path) > 255:
                return
            sub_res.append(path)
            # 基于上一次选择，向下选择
            dfs(sub_res, start + i + 1, s)
            sub_res.pop()
    dfs([], 0, s)  # 复原从0开始的子串
    return res

if __name__ == '__main__':
    s = '25525511135'
    print(restoreIpAddresses(s))
