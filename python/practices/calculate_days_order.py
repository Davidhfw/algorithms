def calculate_days_order(year, month, day):
  """
  根据输入的年月日， 推断出该日期属于一年中的第几天，注意，二月的天数在闰年时是29天，其他时间是28天
  """
  sums = 0
  days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    days_per_month[1] = 29
  for i in range(0, month - 1):
    sums += days_per_month[i]
  sums += day
  return sums


if __name__=='__main__':
  year = int(input())   # python2使用raw_input代替input()
  month = int(input())
  day = int(input())
  sums = calculate_days_order(year, month, day)
  print(sums)
 
