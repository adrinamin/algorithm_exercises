import unittest
from minion_id.minion_id_creator import get_minion_id


class MinionIdTest(unittest.TestCase):
    
    def test_get_minion_id_with_chosen_index_3(self):
        chosen_number = 3
        result = get_minion_id(chosen_number)
        self.assertEqual(result, "71113")
        
        
    def test_get_minion_id_with_chosen_index_0(self):
        chosen_number = 0
        result = get_minion_id(chosen_number)
        self.assertEqual(result, "23571")
        
    
    def test_get_minion_id_with_chosen_index_10000(self):
        chosen_number = 10000
        result = get_minion_id(chosen_number)
        self.assertEqual(result, "02192")