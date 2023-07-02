import threading
import time


def print_fib(number: int) -> None:
    def fib(n: int) -> int:
        if n ==1:
            return 0
        elif n == 2:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)

    print(f'fib({number})равно {fib(number)}')


def fib_with_threads():
    forty_thread = threading.Thread(target=print_fib, args=(40,))
    forty1_thread = threading.Thread(target=print_fib, args=(41,))

    forty_thread.start()
    forty1_thread.start()

    forty_thread.join()
    forty1_thread.join()


start = time.time()

fib_with_threads()

end = time.time()

print(f'Время многопоточной работы {end - start: .4f} с.')