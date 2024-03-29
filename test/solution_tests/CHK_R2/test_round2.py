from lib.solutions.CHK.checkout_solution import checkout


class TestCheckoutNewSolution():
    def test_discount_offers(self):
        assert checkout("AAA") == 130
        assert checkout("AAAAAA") == 250

    def test_free_item(self):
        assert checkout("EEB") == 80
        assert checkout("EEEEBBB") == 190