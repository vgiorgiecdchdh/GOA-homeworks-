pin = ""
attempts = 0
while pin != "9877":
    pin = input("შეიყვანეთ პინკოდი: ")
    attempts += 1
print("სცდების რაოდენობა * 2 =", attempts * 2)
