from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")

name = "calculator_Elie_Medawar"
version = "0.1"
default_task = "publish"


@init
def initialize(project):
    project.set_property("name", "calculator_Elie_Medawar")
    project.set_property("version", "0.1")
    project.set_property("default_task", "publish")
    project.set_property("unittest_module", "tests.unittest")
    # Point PyBuilder at our tests folder so `pyb run_unit_tests` actually runs them
    project.set_property("dir_source_unittest_python", "tests/unittest/calculator_Elie_Medawar")
    project.set_property("unittest_module_glob", "test_*")
