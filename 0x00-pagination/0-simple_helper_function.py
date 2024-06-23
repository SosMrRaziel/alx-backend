#!/usr/bin/env python3
from typing import Tuple


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
        raise ValueError("Page and page_size must be positive integers.")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
