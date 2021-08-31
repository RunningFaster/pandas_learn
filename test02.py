class Test:
    def __call__(self, *args, **kwargs):
        return "this is call function"


print(Test()())
