from dataclasses import dataclass


SUPPORTED_BROWSERS = ['chrome', 'firefox', 'edge']


@dataclass(frozen=True)
class TestConfig:
    browser: str
    implicit_wait: int = 10
    headless: bool = False
    full_screen: bool = True

    def __post_init__(self):
        if self.browser not in SUPPORTED_BROWSERS:
            raise ValueError(f"Current {self.browser=} not supported.")
