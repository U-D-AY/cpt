try:
    lis:list[int] = list(map(int,input("Enter list of nums with space: ").strip().split()))
    print(sum(lis))
except Exception as e:
    print(f"{e} not int.")
