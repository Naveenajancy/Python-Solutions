import threading


def testThread(num):
    print(f"Thread number {num}")
    


if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=testThread, args=(i,))
        t.start()
