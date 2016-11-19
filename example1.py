class Logging:

    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        result = self.f(*args, **kwargs)
        print("%s(%s, %s)" % (
            self.f.__name__, ", ".join(map(str, *args)), kwargs))
        return result


class Counter:

    def __init__(self, f):
        self.counter = 0
        self.f = f

    def __call__(self, *args, **kwargs):
        self.counter += 1
        print("ran %d times" % self.counter)
        return self.f(*args, **kwargs)


class Benchmark:

    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        import time
        t = time.clock()
        result = self.f(*args, **kwargs)
        print("ran for %f s" % (time.clock() - t))
        return result


@Counter
@Benchmark
@Logging
class Reverse_list:

    def __init__(self, x):
        self.x = list(reversed(x))

    def __str__(self):
        return str(self.x)


print(Reverse_list([1, 2, 3]))
