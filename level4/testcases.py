import pytest
from level.SystyemDriveFinder  import SystemDriveFinder
from level.searchfile import FileFinder
class Test_Drive:
    def test_Drivecase(self):
        obj=SystemDriveFinder()
        self.expected=obj.find_drives()
        self.actual=['C']
        assert self.expected==self.actual
    def test_searchfile(self):
        obj=FileFinder()
        d=obj.find_file('demo.txt','C:\hcl')
        self.expected_filename=d[0]
        self.actual_res='C:\hcl\demo.txt'
        assert self.expected_filename==self.actual_res

