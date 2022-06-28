import importlib

def call_install(name: str, **kwargs) -> int:
    """call_install() is a function which imports :param:`name`
    and calls a function called `install()` inside the module.

    Parameters
    ----------
    name : str
        The name of the module to be imported.

    Returns
    -------
    int
        The return value of the function called `install()`.
    """
    module = importlib.import_module(name)
    return module.install(**kwargs)
