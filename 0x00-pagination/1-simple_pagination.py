#!/usr/bin/env python3
""" Module for task 1 """

import csv
import math
from typing import List, Tuple
# index_range = __import__('0-simple_helper_function').index_range


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
        Returns the appropriate page of the dataset
        based on the given page and page size.

        Args:
            page (int): The 1-indexed page number.
            page_size (int): The number of items per page.

        Returns:
            List[List]: A list of rows corresponding to the requested page.
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        start, end = index_range(page, page_size)
        return self.dataset()[start:end]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple containing the start
    and end indices for a given page and page size.

    Args:
        page (int): The 1-indexed page number.
        page_size (int): The number of items per page.

    Returns:
        tuple[int, int]: A tuple with the start and end indices.
    """

    if page <= 0 or page_size <= 0:
        return (0, 0)
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
