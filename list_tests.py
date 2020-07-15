import sys
import pytest

class PytestCollectPlugin():

    def __init__(self):
        self.collected = []

    def pytest_collection_modifyitems(self, items):
        for item in items:
            self.collected.append(item)



def main(directory):
    my_plugin = PytestCollectPlugin()
    pytest.main(['--collect-only', directory], plugins=[my_plugin])

    tests_to_run = []
    for item in my_plugin.collected:
        is_skipped_flag = False
        for marker in item.own_markers:
            if marker.name == "skip":
                is_skipped_flag = True

        if not is_skipped_flag:
            tests_to_run.append(item.nodeid)

    print("\n".join(tests_to_run))

# at deep-learning-containers/test/dlc_tests level, run:
# python3 /Users/huahq/myworkspace/pytest-playground/list_tests.py ec2/
if __name__ == "__main__":
    directory = sys.argv[1]
    main(directory)

