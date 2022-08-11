import cmath
from typing import Tuple, Union

from tango import Step

@Step.register("main")
class Main(Step):
    def run(self):  # type: ignore
        print("Hello!")
