def generate_four_diff_num():
  """
  使用1,2,3,4生成所有不重复的四位数并且返回数据集
  """
  # 记录生成的结果，避免重复
  visited = set()
  for i in range(1, 5):
    for j in range(1, 5):
      for x in range(1, 5):
        for y in range(1, 5):
          num = i * 1000 + j * 100 + x * 10 + y
          if num not in visited:
            visited.add(num)
   return num


print(generate_four_diff_num)
