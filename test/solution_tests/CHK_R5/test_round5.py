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

    
    def test_group_discount_offers(self):
        # 45 Offer + Min(S,T,X,Y) = X = 17
        assert checkout("STXY") == 62
        # multiple of group discount offer should still give 45
        assert checkout("SSS") == 45
        # 65 + (3U + U free offer) 120 = 185
        assert checkout("USTZUUUY") == 185
        assert checkout("K") == 70
        assert checkout("ABCDEFGHIJKLMNOPQRSTUVW") == 795



