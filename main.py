import cmath
from typing import Tuple, Union

from tango import Step

@Step.register("main")
class Main(Step):
    def run(self) -> int:
        print("Hello!")
        return 5
