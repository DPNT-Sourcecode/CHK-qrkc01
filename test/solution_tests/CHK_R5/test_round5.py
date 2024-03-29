from lib.solutions.CHK.checkout_solution import checkout


class TestCheckoutR5NewSolution():
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
    
    def test_extra_letters(self):
        assert checkout("XYZ") == 150
        assert checkout("RRRQ") == 150
        assert checkout("VVVV") == 180
        assert checkout("HHHHHHHHH") == 85
        assert checkout ("UUU") == 120
        assert checkout("FFF") == 20
        assert checkout("FFFF") == 30
    
    def test_group_discount_offers(self):
        # 45 Offer + Min(S,T,X,Y) = X = 17
        assert checkout("STXY") == 62

