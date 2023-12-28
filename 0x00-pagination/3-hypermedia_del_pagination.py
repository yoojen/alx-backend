#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
                self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                    i: dataset[i] for i in range(len(dataset))
                    }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """get the indexed element from the dataset"""
        old_dataset = self.indexed_dataset()
        new_dataset = {}
        hyper_indexed = {
                    'index': index,
                    'next_index': index + page_size,
                    'page_size': page_size,
                    'data': [old_dataset.get(item) for item in range(
                        index, index + page_size)]
                    }
        if old_dataset.get(index) is None:
            after_any_deletion = [val for val in old_dataset.values()]
            new_dataset = {
                    i: after_any_deletion[i] for i in range(
                        len(after_any_deletion))
                    }
            old_dataset = new_dataset
            hyper_indexed['data'] = [new_dataset.get(item) for item in range(
                index, index + page_size)]
            return hyper_indexed
        return hyper_indexed
