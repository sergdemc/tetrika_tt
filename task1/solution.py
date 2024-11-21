from functools import wraps


# def strict(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         annotations = func.__annotations__
#         param_names = list(annotations.keys())[:-1]
#
#         for arg_name, arg_value in zip(param_names, args):
#             expected_type = annotations[arg_name]
#             if not isinstance(arg_value, expected_type):
#                 raise TypeError(
#                     f"Argument '{arg_name}' must be of type {expected_type.__name__}, "
#                     f"but got {type(arg_value).__name__}."
#                 )
#
#         return func(*args, **kwargs)
#
#     return wrapper


from functools import wraps


def strict(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__
        param_names = list(annotations.keys())[:-1]  # Исключаем возвращаемый тип (последний аннотационный параметр)

        # Проверяем позиционные аргументы
        for arg_name, arg_value in zip(param_names, args):
            if arg_name not in annotations:
                continue
            expected_type = annotations[arg_name]
            if not isinstance(arg_value, expected_type):
                raise TypeError(
                    f"Argument '{arg_name}' must be of type {expected_type.__name__}, "
                    f"but got {type(arg_value).__name__}."
                )

        # Проверяем именованные аргументы
        for kwarg_name, kwarg_value in kwargs.items():
            if kwarg_name not in annotations:
                continue
            expected_type = annotations[kwarg_name]
            if not isinstance(kwarg_value, expected_type):
                raise TypeError(
                    f"Argument '{kwarg_name}' must be of type {expected_type.__name__}, "
                    f"but got {type(kwarg_value).__name__}."
                )

        return func(*args, **kwargs)

    return wrapper

# def strict2(func):
#     annotations = func.__annotations__
#     param_names = list(annotations.keys())[:-1]
#
#     def wrapper(*args, **kw):
#
#
#         return func(*args, **kw)
#
#     return wrapper
#
# @strict2
# def foo(a: int, b: int) -> int:
#     return a + b
#
#
# a = foo(2, 12)
