from lib.solutions.CHK.checkout_solution import checkout_r4


class TestCheckoutR4NewSolution():
    def test_discount_offers(self):
        assert checkout_r4("AAA") == 130
        assert checkout_r4("AAAAAA") == 250

    def test_free_item(self):
        assert checkout_r4("EEB") == 80
        assert checkout_r4("EEEEBBB") == 190
    
    def test_illegal_input(self):
        assert checkout_r4("--") == -1
    
    def test_mixed_free_discount(self):
        # 8A -> 2 offers 130 + 200
        # EEB -> get B free 80
        # BB -> offer 45 
        # Total = 470
        assert checkout_r4("AAAAAEEBAAABB") == 455
        assert checkout_r4("AAAAAEEBAAAB") == 440
    
    def test_extra_letters(self):
        assert checkout_r4("XYZ") == 150
        assert checkout_r4("RRRQ") == 150
        assert checkout_r4("VVVV") == 180
        assert checkout_r4("HHHHHHHHH") == 85
        assert checkout_r4 ("UUU") == 120
        assert checkout_r4("FFF") == 20
        assert checkout_r4("FFFF") == 30
