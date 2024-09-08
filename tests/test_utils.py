from unittest.mock import patch

from adsp.utils import to_csv, to_pandas

from .basetestcase import BaseTestCase

MODULE = "adsp.utils"


class TestUtils(BaseTestCase):
    def setUp(self):
        super().setUp()

        pandas_patcher = patch(f"{MODULE}.pd")
        self.mock_pandas = pandas_patcher.start()
        self.addCleanup(pandas_patcher.stop)

        path_patcher = patch(f"{MODULE}.Path")
        self.mock_path = path_patcher.start()
        self.addCleanup(path_patcher.stop)

    def test_to_pandas(self):
        data = [{"hello": "world", "bad": "boys"}]

        to_pandas(data)

        self.mock_pandas.json_normalize.assert_called_once_with(data)

    def test_to_csv_new_file(self):
        self.mock_path.return_value.exists.return_value = False

        mock_df = self.mock_pandas.json_normalize.return_value
        filename = "output.csv"

        to_csv(mock_df, filename)

        mock_df.to_csv.assert_called_once_with(filename, mode="w", header=True)

    def test_to_csv_existing_file(self):
        self.mock_path.return_value.exists.return_value = True

        mock_df = self.mock_pandas.json_normalize.return_value
        filename = "output.csv"

        to_csv(mock_df, filename)

        mock_df.to_csv.assert_called_once_with(filename, mode="a", header=False)
