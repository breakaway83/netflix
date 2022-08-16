import unittest
from typing import List

import requests_mock

from config import Config
from exploit_automation import ExploitAutomation


class TestExploitEndpoints(unittest.TestCase):

    @classmethod
    def setUp(cls) -> None:
        cls.log_url: str = Config.LOG_URL
        cls.affected_url: str = Config.AFFECTED_URL
        cls.open_connections: int = Config.OPEN_CONNECTIONS
        cls.batch_file: str = Config.BATCH_FILE
        cls.size: int = 0
        cls.exploit: ExploitAutomation = ExploitAutomation()

    def test_log_download(self):
        with requests_mock.Mocker() as rm:
            rm.get(
                self.log_url,
                content="33334444".encode("utf-8"),
                status_code=200
            )
            filename: str = self.exploit.create_batch_files(self.batch_file)[0]
            client_id: str = ""
            with open(filename, "r") as fd:
                client_id = fd.readline().strip()
            self.assertEqual(client_id, "33334444")

    def test_benign_url(self):
        with requests_mock.Mocker() as rm:
            client_url: str = "".join(
                [self.affected_url, "/clients/", "33334444"]
                )
            rm.post(
                client_url,
                content="processing batch file 1-11-2015.txt; cat /etc/secret".encode(
                    "utf-8"
                ), status_code=200
            )
            result: List[str] = self.exploit.run_exploit(
                "files/1-11-2015-0.txt"
            )
            self.assertTrue(len(result) == 0)

    def test_vulnerable_url(self):
        with requests_mock.Mocker() as rm:
            client_url: str = "".join(
                [self.affected_url, "/clients/", "33334444"]
            )

            rm.post(
                client_url,
                content="processing batch file 1-11-2015.txt; fahfalhjh4314bvcwoo232bn34r43290".encode(
                    "utf-8"
                ), status_code=200
            )
            result: List[str] = self.exploit.run_exploit(
                "files/1-11-2015-0.txt"
            )
            self.assertFalse(len(result) == 0)
            self.assertEqual(
                result[0], "33334444: fahfalhjh4314bvcwoo232bn34r43290"
            )
