import multiprocessing
from dal.collector import Collector
from dal.registrar import Registrar


class GuiOperationQueue:

    def __init__(self):
        # The main_queue is for operations that occur only in the gui thread.
        # The multi_queue is for operations that travel across threads,
        # !Objects in the multi_queue are pickled and lose their references.

        self.multi_queue = multiprocessing.Queue()
        self.main_queue = []

    def __bool__(self):
        if not self.multi_queue.empty():
            self.__unload_multi()
        return bool(self.main_queue)

    def push(self, operation):
        self.main_queue.append(operation)

    def shift(self):
        if self:
            return self.main_queue.pop()
        return None

    def multi_push(self, operation):
        self.multi_queue.put(operation)

    def multi_shift(self):
        return self.multi_queue.get()

    def __unload_multi(self):
        while not self.multi_queue.empty():
            self.push(self.multi_shift())

def collect_worker(multi_queue, paths, exts):
    collect = Collector()
    collect.search_dir(multi_queue, paths, exts)

def cleaning_worker(multi_queue, library):
    registrar = Registrar(library)
    registrar.clean_library(multi_queue)
