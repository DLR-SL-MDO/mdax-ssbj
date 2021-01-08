from ssbjkadmos.tools.structures.Structures import Structures
import os
import sys
import logging

logger = logging.getLogger(__file__)

CWD = os.getcwd()
LOCAL_INPUT_PATH = os.path.join(CWD, "ToolInput", "toolInput.xml")
LOCAL_OUTPUT_PATH = os.path.join(CWD, "ToolOutput", "toolOutput.xml")


def run():
    logger.info("--- starting --- SSBJ Structures")
    Structures().execute(LOCAL_INPUT_PATH, LOCAL_OUTPUT_PATH)
    logger.info("--- finished --- SSBJ Structures")


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    run()
