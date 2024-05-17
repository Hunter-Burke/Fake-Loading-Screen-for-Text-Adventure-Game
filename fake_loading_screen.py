def loading_text():
  sleep(1.5)
  print("\nLoading", end = "")
  for i in range(4):
    sleep(1)
    if i < 3:
      print(".", end = "")
    else:
      print("")
  sleep(2)
