from lib.solutions.CHK.checkout_solution import checkout


class TestCheckoutR3NewSolution():
    def test_new_F_offer(self):
        assert checkout("FFF") == 20
        assert checkout("FFFFF") == 40

    def test_mixed_F_offer(self):
        assert checkout("FAFAAAAF") == 220
        assert checkout("FBBFFFC") == 95