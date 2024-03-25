import logging
import os
import pytest
from py_selenium_auto.browsers.browser_services import BrowserServices
from py_selenium_auto_core.utilities.root_path_helper import RootPathHelper

from utilities.configManager import ConfigManager


@pytest.fixture(scope="session", autouse=True)
def setup_session(request):
    work_dir = RootPathHelper.current_root_path(__file__)
    os.chdir(work_dir)
    for log_name in [
        "selenium.webdriver.remote.remote_connection",
        "selenium.webdriver.common.selenium_manager",
        "urllib3.connectionpool",
    ]:
        logger = logging.getLogger(log_name)
        logger.disabled = True


@pytest.fixture(autouse=True)
def set_up(request):
    base_url = ConfigManager.get_config_value("url")
    BrowserServices.Instance.browser.go_to(base_url)
    BrowserServices.Instance.browser.wait_for_page_to_load()
    BrowserServices.Instance.browser.maximize()

    yield

    if BrowserServices.Instance.is_browser_started:
        BrowserServices.Instance.browser.quit()
