# -*-coding:utf-8 -*-
"""
FileName: 468_verify_ip_address.py
Author: raphealwu
Date: 2021/2/24 8:55 下午
"""
"""
题目描述：编写一个函数来验证输入的字符串是否是有效的 IPv4 或 IPv6 地址。

如果是有效的 IPv4 地址，返回 "IPv4" ；
如果是有效的 IPv6 地址，返回 "IPv6" ；
如果不是上述类型的 IP 地址，返回 "Neither" 。
IPv4 地址由十进制数和点来表示，每个地址包含 4 个十进制数，其范围为 0 - 255， 用(".")分割。比如，172.16.254.1；

同时，IPv4 地址内的数不会以 0 开头。比如，地址 172.16.254.01 是不合法的。

IPv6 地址由 8 组 16 进制的数字来表示，每组表示 16 比特。这些组数字通过 (":")分割。比如,  2001:0db8:85a3:0000:0000:8a2e:0370:7334 是一个有效的地址。而且，我们可以加入一些以 0 开头的数字，字母可以使用大写，也可以是小写。所以， 2001:db8:85a3:0:0:8A2E:0370:7334 也是一个有效的 IPv6 address地址 (即，忽略 0 开头，忽略大小写)。

然而，我们不能因为某个组的值为 0，而使用一个空的组，以至于出现 (::) 的情况。 比如， 2001:0db8:85a3::8A2E:0370:7334 是无效的 IPv6 地址。

同时，在 IPv6 地址中，多余的 0 也是不被允许的。比如， 02001:0db8:85a3:0000:0000:8a2e:0370:7334 是无效的。

解题思路：
对于ipv4验证，首先先使用.将字符串转换为列表，然后依次遍历数组，只需要找出异常情况，因为正常情况的判断方法太多
1 每段字符串为空或者长度超过3
2 每段字符中有0而且0的个数超过1
3 每段字符中包含非数字字符
4 每段字符转为整数后超过255
对于ipv6验证，首先先使用:将字符串转换为列表，然后依次遍历数组，只需要找出异常情况，因为正常情况的判断方法太多
1 每段字符串为空或者长度超过4
2 每段字符串中所有字符都不在0123456789abcdefABCDEF中
"""
def validate_ipv4(ip):
    nums = ip.split(".")
    for x in nums:
        if len(x) == 0 or len(x) > 3:
            return 'Neither'
        if x[0] == '0' and len(x) != 1 or not x.isdigit() or int(x) > 255:
            return 'Neither'
    return "IPv4"

def validate_ipv6(ip):
    nums = ip.split(":")
    hexdigits = "0123456789abcdefABCDEF"
    for x in nums:
        if len(x) == 0 or len(x) > 4:
            return "Neither"
        if not all(c in hexdigits for c in x):
            return "Neither"
        return "IPv6"
    
def validate_ip_address(ip):
    if ip.count('.') == 3:
        return validate_ipv4(ip)
    elif ip.count(':') == 7:
        return validate_ipv6(ip)
    else:
        return "Neither"
