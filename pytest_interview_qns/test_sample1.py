import pytest


class Test:
    @pytest.fixture()
    def setUp(self):
        print("setup related things")
        yield "this is resource passed from setup--"
        print("teardown")

    def test_that_depends_on_resource(self, setUp):
        print(" {}".format(setUp))

    def test_sample_1(self, setUp):
        print("name of : {}".format(setUp))
