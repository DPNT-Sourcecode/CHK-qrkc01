from lib.solutions.CHK.checkout_solution import checkout


class TestCheckoutR4NewSolution():
    def test_discount_offers(self):
        assert checkout("AAA") == 130
        assert checkout("AAAAAA") == 250

    def test_free_item(self):
        assert checkout("EEB") == 80
        assert checkout("EEEEBBB") == 190
    
    def test_illegal_input(self):
        assert checkout("--") == -1
    
    def test_mixed_free_discount(self):
        # 8A -> 2 offers 130 + 200
        # EEB -> get B free 80
        # BB -> offer 45 
        # Total = 470
        assert checkout("AAAAAEEBAAABB") == 455
        assert checkout("AAAAAEEBAAAB") == 440