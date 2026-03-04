part_name = "Gear_A"
part_weight = 45.8
is_qualified = True

if part_weight > 50:
    is_qualified = False 
    status = "太重了，剔除!"
elif part_weight < 40:
    is_qualified = False
    status = "太轻了，剔除！"
else:
    statue = "重量达标，通过"

print(f"---智能检测报告---")
print(f"零件名称：{part_name}")
print(f"检测结果：{status}")
