#!/usr/bin/env python3

# 存放最终结果
total = 0

# 设每次至少有20人继续将消息转发下去
message = 20

# 2.5英寸硬盘的体积=长 × 宽 × 厚，立方厘米 => 立方米
volume = 10 * 7 * 0.7 * 1e-6

# 设一共转发了100层
for i in range(0, 100):
        temp = message ** i
        total = total + temp

# 设消息内容约1000个字，大小约为2K，转成T表示
total = total * 2048 / 1024 / 1024 / 1024 / 1024

# 用4T的硬盘来存储，需要的硬盘数
total = total / 4

# 硬盘总体积
total = total * volume

# 地球的体积约1.08 × 10^21 立方米，看看这么多硬盘有多少个地球大？
total = total / 1e21

print(total)



