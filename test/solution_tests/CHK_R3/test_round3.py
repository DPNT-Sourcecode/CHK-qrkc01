from lib.solutions.CHK.checkout_solution import checkout_r3


class TestCheckoutR3NewSolution():
    def test_new_F_offer(self):
        assert checkout_r3("FFF") == 20
        assert checkout_r3("FFFFF") == 40

    def test_mixed_F_offer(self):
        assert checkout_r3("FAFAAAAF") == 220
        assert checkout_r3("FBBFFFC") == 95