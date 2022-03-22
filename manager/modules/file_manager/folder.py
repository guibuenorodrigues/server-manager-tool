"""Manage folder"""
import logging
import shutil

from . import util


class Folder:
    """Class to manage folder"""

    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)

    def copy(self, source_path: str, dest_path: str, ignore_pattern: list = None) -> str:
        """Copy a entire folder from a path to other - list of *.xml"""

        if not util.is_folder(source_path):
            raise Exception(f"{source_path} is not a folder/dir")

        self.logger.debug(f"ignoring by pattern: {ignore_pattern}")

        if ignore_pattern is None or len(ignore_pattern) <= 0:
            _ignore_pattern = None
        else:
            _ignore_pattern = shutil.ignore_patterns(*ignore_pattern)

        try:
            dest = shutil.copytree(src=source_path, dst=dest_path, dirs_exist_ok=True, ignore=_ignore_pattern)
            self.logger.debug("folder copied successfuly")

            return dest
        except Exception as err:
            self.logger.exception(f"unable to copy folder from {source_path} to {dest_path}")
            raise err
