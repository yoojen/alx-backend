#!/usr/bin/env python3
from typing import Tuple


def index_range(page:int, page_size: int) -> Tuple[int, int]:
    """return the starting index and ending index"""
    start_index = (page - 1) * page_size
    end_index =  page * page_size

    return start_index, end_index
