# -*- coding: utf-8 -*-
"""
Interact with the Metropolitan Police Service API to
retrieve stop and search data
"""
import datetime

import requests

from .exceptions import MetropolitanPoliceServiceError

BASE_API_URL = "https://data.police.uk/api/stops-force?force={force_id}&date={month}"


class MetropolitanPoliceService:
    def __init__(self, force_id: int, search_date: datetime):
        self.force_id = force_id

        month = search_date.month
        if search_date.month < 10:
            month = f"0{search_date.month}"

        self.search_month = f"{search_date.year}-{month}"

    def stop_and_search_data(self):
        """Retrieve stop and search from the API"""
        url = BASE_API_URL.format(
            force_id=self.force_id,
            month=self.search_month,
        )
        response = requests.get(url)

        if response.status_code != 200:
            raise MetropolitanPoliceServiceError("No stop and search data found!")

        return response.json()
