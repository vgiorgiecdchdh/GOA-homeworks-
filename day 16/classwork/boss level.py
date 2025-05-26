attempts = 0  # მცდელობების რაოდენობა

while True:
    pin = int(input("შეიყვანე PIN კოდი: "))
    attempts += 1
    if pin == 9877:
        print("სწორია!")
        print("შენი მცდელობების რაოდენობა გამრავლებული 2-ზეა:", attempts * 2)
        break
    else:
        print("არასწორი PIN, სცადე თავიდან.")
