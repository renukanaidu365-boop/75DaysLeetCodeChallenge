
import collections
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = collections.Counter(tasks)
        frequencies = list(task_counts.values())
        max_freq = max(frequencies)
        max_count = frequencies.count(max_freq)
        
        part_count = max_freq - 1
        part_length = n - (max_count - 1)
        empty_slots = part_count * part_length
        available_tasks = len(tasks) - (max_freq * max_count)
        idles = max(0, empty_slots - available_tasks)
        
        return len(tasks) + idles
