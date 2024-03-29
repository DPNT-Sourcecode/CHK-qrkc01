from lib.solutions.CHK.checkout_solution import checkout_r2


class TestCheckoutR2Solution():
    def test_discount_offers(self):
        assert checkout_r2("AAA") == 130
        assert checkout_r2("AAAAAA") == 250

    def test_free_item(self):
        assert checkout_r2("EEB") == 80
        assert checkout_r2("EEEEBBB") == 190
    
    def test_illegal_input(self):
        assert checkout_r2("F") == -1
    
    def test_mixed_free_discount(self):
        # 8A -> 2 offers 130 + 200
        # EEB -> get B free 80
        # BB -> offer 45 
        # Total = 470
        assert checkout_r2("AAAAAEEBAAABB") == 455
        assert checkout_r2("AAAAAEEBAAAB") == 440