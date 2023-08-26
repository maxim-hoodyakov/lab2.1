import math

h = int(input("Введите сколько часов(0-23): "))
m = int(input("Введите сколько минут(0-59): "))
s = int(input("Введите сколько секунд(0-59): "))

angle_h = (h % 12 + m / 60 + s / 3600) * 30
angle_m = (m + s / 60) * 6
angle_diff = abs(angle_h - angle_m)
if angle_diff > 180:
    angle_diff = 360 - angle_diff

print("Угол:", angle_diff, "градусов")