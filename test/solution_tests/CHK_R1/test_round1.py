from lib.solutions.CHK.checkout_solution import checkout


class TestCheckoutSolution():
    def test_single_item(self):
        assert checkout("C") == 20
        assert checkout("D") == 15