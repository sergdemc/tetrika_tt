from functools import wraps


def strict(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__
        param_names = list(annotations.keys())[:-1]

        for arg_name, arg_value in zip(param_names, args):
            expected_type = annotations[arg_name]
            if not isinstance(arg_value, expected_type):
                raise TypeError(
                    f"Argument '{arg_name}' must be of type {expected_type.__name__}, "
                    f"but got {type(arg_value).__name__}."
                )

        return func(*args, **kwargs)

    return wrapper
