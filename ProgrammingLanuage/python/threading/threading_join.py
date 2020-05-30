import threading
import time

lock = threading.Lock()

# join 用法
def runner(i, p1, p2, p3="benzi", p4="BMW", **kwargs):
    """

    :return:
    """
    count = 0
    print("线程{} param1:====".format(i), p1)
    print("线程{} param2:====".format(i), p2)
    print("线程{} param3:====".format(i), p3)
    print("线程{} param3:====".format(i), p4)
    while True:
        with lock:
            count += 1
            print("线程{} 第 {} 秒 后: ......".format(i, count))
            time.sleep(1)
            if count == 5:
                break


def main_thread():
    """
    主线程的运行代码
    :return:
    """
    # 假设主线程中处理需要10s
    print("主线程开始执行")
    time.sleep(10)
    print("主线程执行结束")


def main():
    """
    :return:
    """
    for i in range(5):
        thread = threading.Thread(target=runner, args=(i, "abc", "dce"), kwargs={"p4": "路虎", "p5": "audi"})
        thread.setName("线程{}".format(i))
        thread.start()

        # 使用join 之后所有函数等待前面的线程执行结束后在开始执行下一个线程，不使用 join 则所有的线程一起执行
        thread.join()

    main_thread()


if __name__ == "__main__":
    main()
