int_list = []
for i in range(10):
    num = int(input(f"{i+1}) 49 (int): "))
    int_list.append(num)
str_list = []
for i in range(10):
    text = input(f"{i+1})i like goa (str): ")
    str_list.append(text)

# Float მონაცემების მიღება
float_list = []
for i in range(10):
    fnum = float(input(f"{i+1}) 5.4(float): "))
    float_list.append(fnum)
print("20(int):", int_list)
print("ი ლიკე გოა(str):", str_list)
print("10.9 (float):", float_list)
