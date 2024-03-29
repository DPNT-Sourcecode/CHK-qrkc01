from lib.solutions.CHK.checkout_solution import checkout


class TestCheckoutSolution():
    def test_single_item(self):
        assert checkout("C") == 20
        assert checkout("D") == 15
    
    def test_mixed_no_offers(self):
        assert checkout("ABC") == 100
        assert checkout("DDDDCCC") == 120
    
    def test_empty_basket(self):
        assert checkout("") == 0
    
    def test_special_offers(self):
        assert checkout("AAAA") == 180
        assert checkout("BB") == 45
    
    def test_mixed_specials(self):
        assert checkout("AAABBCD") == 210
    
    def test_illegal_input(self):
        assert checkout("E") == -1