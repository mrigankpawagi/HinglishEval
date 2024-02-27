from typing import List


def sort_numbers(numbers: str) -> str:
    """
    Input ek space-delimited string hai jisme 'zero' se 'nine' tak ke numerals hain.
    Valid choices 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' aur 'nine' hain.
    Return karo string ko jisme numbers smallest se largest tak sorted honge
    >>> sort_numbers('three one five')
    'one three five'
    """
    number = set(numbers.split())
    number = sorted(number)
    return''.join(str(n) for n in number[0: ]) +'' +''.join(str(n) for n in number[-1: ])


if __name__ == "__main__":
    print(sort_numbers("zero five"))
<|python|>from data.dataset.BinaryLabelsDataset import BinaryLabelsDataset
from data.dataset.TextLabelsDataset import TextLabelsDataset
from data.dataset.CachedBinaryDataset import CachedBinaryDataset
from data.dataset.BinaryLabeledDataset import BinaryLabeledDataset
from data.dataset.CachedBinaryLabeledDataset import CachedBinaryLabeledDataset
from eval.eval_utils.eval_loader import TextLoader
from eval.configs.base import get_name, EvalConfigBase
from eval.trains import BaseTrainer
from eval.metrics.base import Metric
from transformers import get_linear_schedule_with_warmup, AdamW, get_constant_schedule_with_warmup
import logging


