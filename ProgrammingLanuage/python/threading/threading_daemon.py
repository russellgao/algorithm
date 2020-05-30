import threading
import time


# 守护线程用法
def runner(p1, p2, p3="benzi", p4="BMW", **kwargs):
    """

    :return:
    """
    count = 0
    print("param1:====", p1)
    print("param2:====", p2)
    print("param3:====", p3)
    print("param3:====", p4)
    while True:
        count += 1
        print("第 {} 秒 后: ......".format(count))
        time.sleep(1)


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
    thread = threading.Thread(target=runner, args=("abc", "dce"), kwargs={"p4": "路虎", "p5": "audi"})
    # 子线程设置位守护线程，当主线程结束后子线程也结束
    # 默认不是守护线程，会阻塞主线
    thread.setDaemon(True)
    thread.start()
    main_thread()


if __name__ == "__main__":
    main()
