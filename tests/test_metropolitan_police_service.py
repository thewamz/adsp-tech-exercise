from datetime import datetime
from unittest.mock import patch

from adsp.exceptions import MetropolitanPoliceServiceError
from adsp.metropolitan_police_service import MetropolitanPoliceService

from .basetestcase import BaseTestCase

MODULE = "adsp.metropolitan_police_service"


class TestMetropolitanPoliceService(BaseTestCase):
    def setUp(self):
        super().setUp()

        requests_patcher = patch(f"{MODULE}.requests")
        self.mock_requests = requests_patcher.start()
        self.addCleanup(requests_patcher.stop)

    def test_instantiation(self):
        force_id = "Avengers"
        search_date = datetime.now()

        month = search_date.month
        if search_date.month < 10:
            month = f"0{search_date.month}"

        search_month = f"{search_date.year}-{month}"

        msp = MetropolitanPoliceService(force_id, search_date)

        self.assertEqual(force_id, msp.force_id)
        self.assertEqual(search_month, msp.search_month)

    def test_stop_and_search_data(self):
        self.mock_requests.get.return_value.status_code = 200
        self.mock_requests.get.return_value.json.return_value = [{"hello": "world"}]

        force_id = "Avengers"
        search_date = datetime.now()

        month = search_date.month
        if search_date.month < 10:
            month = f"0{search_date.month}"

        search_month = f"{search_date.year}-{month}"

        msp = MetropolitanPoliceService(force_id, search_date)

        self.assertEqual([{"hello": "world"}], msp.stop_and_search_data())

        self.mock_requests.get.assert_called_once_with(
            "https://data.police.uk/api/stops-force?"
            f"force={force_id}&date={search_month}"
        )

    def test_stop_and_search_data_error(self):
        self.mock_requests.get.return_value.status_code = 400

        force_id = "Avengers"
        search_date = datetime.now()

        month = search_date.month
        if search_date.month < 10:
            month = f"0{search_date.month}"

        search_month = f"{search_date.year}-{month}"

        msp = MetropolitanPoliceService(force_id, search_date)

        with self.assertRaises(MetropolitanPoliceServiceError):
            msp.stop_and_search_data()

        self.mock_requests.get.assert_called_once_with(
            "https://data.police.uk/api/stops-force?"
            f"force={force_id}&date={search_month}"
        )
