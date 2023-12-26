#!/usr/bin/env python3
"""get the starting index and ending index of the page"""

import csv
import math
from typing import Tuple, List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return the starting index and ending index"""
    if page and page_size != 0:
        start_index = (page - 1) * page_size
        end_index = page * page_size

    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        return the information form dataset according to pages
        passed in method
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start_end = index_range(page, page_size)
        if page * page_size > len(self.dataset()):
            return []
        return self.dataset()[start_end[0]: start_end[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        create HATEAOS.
        returns dictionary containing page_size, page, data, next_page,
        prev_page, and total_page
        """
        my_page = self.get_page(page, page_size)
        hateaos = {
                'page_size': page_size if len(my_page) > 0 else 0,
                'page': page,
                'data': my_page if len(my_page) > 0 else [],
                'next_page': page + 1 if len(my_page) > 0 else None,
                'prev_page': page - 1 if page > 1 else None,
                'total_pages': math.ceil(len(self.dataset()) / page_size)
                }
        return hateaos
