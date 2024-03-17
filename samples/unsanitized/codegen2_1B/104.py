
def unique_digits(x):
    """
    Diye gaye positive integers ki list x me Woh saare elements ki sorted list return karo jisme koi bhi even digit nahi hai.

    Dhyan de: Return ki gayi list ko increasing order me sort kiya jana chahiye.
    
    Jaise ki:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    
    ki = []
    a = [x]
    for i in range(int(x)):
        b = i
        while b * b <= x:
            a.append(a[-1])
            b *= 10
        a.append(x)

    for i in a:
        if i not in ki: ki.append(i)

    return list(set(ki))

if __name__ == "__main__":
    print(unique_digits([15, 33, 1422, 1]))
<|python|>import os
import re
import shlex
from typing import Tuple, Dict, List
from subprocess import PIPE, Popen, CalledProcessError

import yaml
from pccf_client import exceptions

from.base import (
    BasePCCFCli,
    _run_command,
    _run_command_and_capture_output,
    _run_command_and_capture_stderr,
)
from....config.base import ConfigBase
from....config.project.base import ProjectBase
from....config.source.base import BaseSource, SourceOptionType, Source


class CLI(BasePCCFCli):
    def __init__(self, config: ConfigBase, root: str, project_root: str, use_terminal=True) -> None:
        super().__init__(config, root, use_terminal=use_terminal)
        self._config: ConfigBase = self._reload_config(config=config)
        self._root_dir: str = os.path.abspath(root