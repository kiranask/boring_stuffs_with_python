import pytest
class Test:
    @pytest.fixture()
    def setUp(self):
        print("setup")
        yield "resource"
        print("teardown")

    def test_that_depends_on_resource(self, setUp):
        print("testing {}".
              format(setUp))