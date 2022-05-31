from threading import Thread


class MyThread(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self) -> None:
        for i in range(100000):
            msg = f'{self.name} is running'
            print(msg)


def create_threads():
    for i in range(10000):
        name = f'Thread {i + 1}'
        my_thread = MyThread(name)
        my_thread.start()


if __name__ == '__main__':
    create_threads()
