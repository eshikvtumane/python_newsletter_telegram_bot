import sys

import pytest

from bot.data_sources.external_news_sources.driver import DataSourcesDriver


class TestExternalNewsSourceDriver:
    @pytest.mark.skipif(sys.platform == 'win32',
                        reason="does not run on windows")
    def test_network_not_available(self, socket_disabled):
        news = list(DataSourcesDriver().get_all_news())

        assert len(news) == 0, "Wrong news quantity."
