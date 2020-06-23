# def func(**kwargs):
#     print(kwargs)
#     print(type(kwargs))  # <class 'dict'>
#
#
# func(name='asep', last='sayyad')  # {'name': 'asep', 'last': 'sayyad'}
#
#
# def func_loop(**kwargs):
#     for k, v in kwargs.items():
#         print(f"{k}:{v}")


# func_loop(name='asep', last='sayyad')


# def func_loop(name, **kwargs):
#     for k, v in kwargs.items():
#         print(f"{k}:{v}:", name)


# func_loop('mohit', first_name='asep', last='sayyad')

# ============dict unpacking========
def func_loop(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}:{v}")


d = {'name': 'asep', 'age': 24}
func_loop(**d)
