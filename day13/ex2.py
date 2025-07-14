try:
    from datetime import datetime

    t1 = datetime.now()
    num = list(map(int, input('Enter numbers: ').split()))
    if len(num) < 3:
        print('At least 3 numbers are required.')
    else:
        
        a, b, c = num[0], num[1], num[2]

        if a > b: a, b = b, a
        if b > c: b, c = c, b
        if a > b: a, b = b, a
        minimum = [a, b, c]

        a, b, c = num[0], num[1], num[2]
        if a < b: a, b = b, a
        if b < c: b, c = c, b
        if a < b: a, b = b, a
        maximum = [a, b, c]

        for i in num[3:]:

            if i < minimum[2]:
                if i < minimum[0]:
                    minimum = [i, minimum[0], minimum[1]]
                elif i < minimum[1]:
                    minimum = [minimum[0], i, minimum[1]]
                else:
                    minimum[2] = i

            if i > maximum[2]:
                if i > maximum[0]:
                    maximum = [i, maximum[0], maximum[1]]
                elif i > maximum[1]:
                    maximum = [maximum[0], i, maximum[1]]
                else:
                    maximum[2] = i

        print(f"Minimum 3 values: {minimum}")
        print(f"Maximum 3 values: {maximum}")
        t2 = datetime.now()

        print(f"time: {t2-t1}")

except Exception as e:
    print(f"Error occurred: {e}")
