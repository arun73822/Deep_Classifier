import pytest
from deep_classifier.utility.common import read_yaml_file
from pathlib import Path
from box import ConfigBox
from ensure.main import EnsureError

class Test_read_yaml_file:

    yaml_files=[
        "tests\data\empty.yaml",
        "tests\data\demo.yaml"
    ]

    def test_read_yaml_file_empty(self):
        with pytest.raises(ValueError):
            read_yaml_file(Path(self.yaml_files[0]))

    def test_read_yaml_return(self):
        response=read_yaml_file(Path(self.yaml_files[-1]))
        assert isinstance(response,ConfigBox)

    @pytest.mark.parametrize("path_to_yaml",yaml_files)
    def test_read_yaml_bad_type(self,path_to_yaml):
        with pytest.raises(EnsureError):
            read_yaml_file(path_to_yaml)