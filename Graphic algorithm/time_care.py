from time import time


def run_time(func):
    def wraper(*args):
        start = time()
        func(*args)
        end = time()
        print(f'本次执行的时间是：{end - start}秒！')

    return wraper


if __name__ == '__main__':
    from time import sleep


    @run_time
    def test_func():
        sleep(1)


    test_func()
