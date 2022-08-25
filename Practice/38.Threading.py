"""

stu_data=[]
for y in range(int(input())):
    name = input()
    score = float(input())
    stu_data.append([name,score])
print(stu_data)

stu_data = [['abc', 12.3], ['def', 45.6], ['adc', 12.3], ['dedf', 2.6]]
scr = sorted(list(set([x[1] for x in stu_data])))


nd_low = scr[1]
#
stu_names = []
for i in stu_data:
     if i[1]==nd_low:
         stu_names.append(i[0])
stu_names = sorted(stu_names)
for k in stu_names:
     print(k)


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        print(name)
        print(*line)
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    print(student_marks)
"""

import threading
import sys
import time

def time_it(func):
    print(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        #print(start)
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + " took " + str((end-start)) + "sec" )
        return result
    return wrapper

@time_it
def print_sleep(n, k):
    print("Thread %s: Starting", n)
    for i in range(0, n):
        sys.stdout.write(str(k))
        sys.stdout.flush()
        time.sleep(1)

    print("Thread %s: Finishing", n)


if __name__ == "__main__":
    # print_sleep(5)
    # print_sleep(15)

    # creating thread
    t1 = threading.Thread(target=print_sleep, args=(10, "#"))
    t2 = threading.Thread(target=print_sleep, args=(20, "*"))

    # starting thread 1print_sleep
    t1.start()
    # starting thread 2
    t2.start()

    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()

    # both threads completely executed
    print("Done!")