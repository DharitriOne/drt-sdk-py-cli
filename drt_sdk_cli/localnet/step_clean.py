import logging
from pathlib import Path

from drt_sdk_cli import utils
from drt_sdk_cli.localnet.config_root import ConfigRoot

logger = logging.getLogger("localnet")


def clean(configfile: Path):
    logger.info("clean()")

    config = ConfigRoot.from_file(configfile)
    utils.remove_folder(config.root())
