import pytest


class Test:
    @pytest.fixture(scope="method")
    # @pytest.fixture(scope="function")
    # @pytest.fixture(scope=class)
    # @pytest.fixture(scope= class )

    def setUp(self):
        print("setup related things")
        yield "-this is resource -"
        print("teardown ")

    def test_sample_0(self, setUp):
        print("test sample 0:  {}".format(setUp))

    def test_sample_1(self, setUp):
        print("test sample 1 {}".format(setUp))

    @pytest.mark.run(order=1)
    def test_sample_2(self, setUp):
        print("test sample 2 {}".format(setUp))

    @pytest.mark.depends(on=['test_sample_1'])
    def test_sample_3(self, setUp):
        print("test sample 3 {}".format(setUp))

    @pytest.skip
    def test_sample_4(self, setUp):
        print("test sample 4 {}".format(setUp))
