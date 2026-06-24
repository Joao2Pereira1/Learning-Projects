import os

import pytest  # installed in python 3.12

import utils.utilities as util
from scratch import commands, main
from utils.file_methods import file
from utils.folder_methods import folder


@pytest.fixture(scope="function")
def test_directory():
    # Create a test directory
    dir_name = "test_directory"
    folder.create(dir_name)
    yield dir_name
    folder.delete(dir_name)


@pytest.fixture(scope="function")
def test_file():
    # Create a test file
    file_name = "test_file.txt"
    file.create(file_name)
    yield file_name
    file.delete(file_name)


class TestFileCommands:
    def test_create_file(self, test_file):
        # Test creating a new file
        file_name = test_file
        commands["mk"](file_name)
        assert os.path.exists(file_name)

    def test_delete_file(self):
        # Test deleting a file
        file_name = "delete_test_file.txt"
        file.create(file_name)
        commands["delete"](file_name)
        assert not os.path.exists(file_name)


class TestDirectoryCommands:
    def test_create_directory(self, test_directory):
        # Test creating a new directory
        dir_name = test_directory
        commands["mkdir"](dir_name)
        assert os.path.exists(dir_name)

    def test_change_directory(self, test_directory):
        # Test changing the current directory
        dir_name = test_directory
        original_dir = os.getcwd()
        try:
            folder.change(dir_name)
            assert os.path.basename(os.getcwd()) == dir_name
        finally:
            os.chdir(original_dir)  # Change back to the original directory


class TestUtilityFunctions:
    def test_list_files(self, test_file):
        # Test listing files in the current directory
        files = util.list_files()
        assert test_file in files

    def test_help(self):
        # Test displaying help information
        util.helper()

    def test_about(self):
        # Test displaying about information
        util.about()
