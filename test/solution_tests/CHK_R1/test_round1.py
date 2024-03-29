from lib.solutions.CHK.checkout_solution import checkout_r1


class TestCheckoutR1Solution():
    def test_single_item(self):
        assert checkout_r1("C") == 20
        assert checkout_r1("D") == 15
    
    def test_mixed_no_offers(self):
        assert checkout_r1("ABC") == 100
        assert checkout_r1("DDDDCCC") == 120
    
    def test_empty_basket(self):
        assert checkout_r1("") == 0
    
    def test_special_offers(self):
        assert checkout_r1("AAAA") == 180
        assert checkout_r1("BB") == 45
    
    def test_mixed_specials(self):
        assert checkout_r1("AAABBCD") == 210
    
    def test_illegal_input(self):
        assert checkout_r1("E") == -1