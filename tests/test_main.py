import pytest


@pytest.mark.xfail
def test_main(config):
    data = config["wrong key value"]


def test_run_browser(init_driver):
    expected_url = "https://duckduckgo.com/"
    init_driver.get(expected_url)
    assert init_driver.current_url == expected_url
