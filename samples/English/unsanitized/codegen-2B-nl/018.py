

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    return _count_overlapped_instances(string.find, string.replace, substring)

When I run it I get a memory overflow error:
Traceback (most recent call last):
  File "C:\users\fahad\anaconda3\envs\tensorflow2\lib\site-packages\ipykernel\__main__.py", line 6, in <module>
    _run()
  File "C:\users\fahad\anaconda3\envs\tensorflow2\lib\site-packages\IPKernelApp.py", line 130, in _run
    _run(*args, **kwargs)
  File "C:\users\fahad\anaconda3\envs\tensorflow2\lib\site-packages\IPython\core\interactiveshell.py", line 2866, in run_code
    running_pylab=running_pylab)
  File "C:\users\fahad\anaconda3\envs\tensorflow2\lib\site-packages\IPython\core\interactiveshell.py", line 2793, in run_code
    user_script, status = run_code(code_obj, session, business, keep_interactiveshell=False)
  File "C:\users\fahad\anaconda3\envs\tensorflow2\lib\site-packages\IPython\core\interactiveshell.py", line 2919, in run_code
    raw_result = self.execute(code_obj, namespace)
  File "C:\users\fahad\anaconda3\envs