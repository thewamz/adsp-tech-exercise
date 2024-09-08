from unittest.mock import patch

from adsp.entry import main

from .basetestcase import BaseTestCase

MODULE = "adsp.entry"


class TestEntry(BaseTestCase):
    def setUp(self):
        super().setUp()

        parser_patcher = patch(f"{MODULE}.ArgumentParser")
        self.mock_parser = parser_patcher.start()
        self.addCleanup(parser_patcher.stop)

        # self.mock_parser.return_value.parser_args.return_value = Mock(
        #     force_id='Batman',
        #     month='2023-04',
        #     csv_file='output.csv'
        # )

        msp_patcher = patch(f"{MODULE}.MetropolitanPoliceService")
        self.mock_msp = msp_patcher.start()
        self.addCleanup(msp_patcher.stop)

        to_pandas_patcher = patch(f"{MODULE}.to_pandas")
        self.mock_to_pandas = to_pandas_patcher.start()
        self.addCleanup(to_pandas_patcher.stop)

        to_csv_patcher = patch(f"{MODULE}.to_csv")
        self.mock_to_csv = to_csv_patcher.start()
        self.addCleanup(to_csv_patcher.stop)

        sys_exit_patcher = patch(f"{MODULE}.sys_exit")
        self.mock_sys_exit = sys_exit_patcher.start()
        self.addCleanup(sys_exit_patcher.stop)

    def test_main(self):
        main()

        self.mock_msp.assert_called_once()
        self.mock_msp.return_value.stop_and_search_data.assert_called_once()
        self.mock_to_pandas.assert_called_once_with(
            self.mock_msp.return_value.stop_and_search_data.return_value
        )
        self.mock_to_csv.assert_called_once()
        self.mock_sys_exit.assert_called_once_with(0)
