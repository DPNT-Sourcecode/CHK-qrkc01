from lib.solutions.CHK.checkout_solution import checkout_old


class TestCheckoutSolution():
    def test_single_item(self):
        assert checkout_old("C") == 20
        assert checkout_old("D") == 15
    
    def test_mixed_no_offers(self):
        assert checkout_old("ABC") == 100
        assert checkout_old("DDDDCCC") == 120
    
    def test_empty_basket(self):
        assert checkout_old("") == 0
    
    def test_special_offers(self):
        assert checkout_old("AAAA") == 180
        assert checkout_old("BB") == 45
    
    def test_mixed_specials(self):
        assert checkout_old("AAABBCD") == 210
    
    def test_illegal_input(self):
        assert checkout_old("E") == -1