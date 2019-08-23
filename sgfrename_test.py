import unittest
import sgfrename

class TestSgfrename(unittest.TestCase):

    def test_parse_date_date_empty(self):
        self.assertEqual(sgfrename.parse_date(''), '')

    def test_parse_date_date_no_separation(self):
        self.assertEqual(sgfrename.parse_date('20190101'), '2019-01-01')
    
    def test_parse_date_hyphens(self):
        self.assertEqual(sgfrename.parse_date('2019- 01- 01'), '2019-01-01')
    
    def test_parse_date_hyphens_not_padded(self):
        self.assertEqual(sgfrename.parse_date('2019 -   1   -1 '), '2019-01-01')
    
    def test_parse_date_hyphens_not_escaped(self):
        self.assertEqual(sgfrename.parse_date('20190101 [12\:07\]'), '2019-01-01 12-07')

    def test_find_prop_empty(self):
        self.assertEqual(sgfrename.find_prop('', ''), [])

    def test_find_prop_ap(self):
        self.assertEqual(sgfrename.find_prop('CA[Windows-1252]SZ[19]AP[sgfrename]GN[Rank]', 'AP'), ['sgfrename'])
    
    def test_find_prop_multi(self):
        self.assertEqual(sgfrename.find_prop('CA[Windows-1252]SZ[19]AP[sgfrename]AP[cgoban]GN[Rank]', 'AP'), ['sgfrename', 'cgoban'])
    
    def test_find_prop_escaped(self):
        self.assertEqual(sgfrename.find_prop('CA[Windows-1252]SZ[19]AP[[sgf\]rename]GN[Rank]', 'AP'), ['[sgf\]rename'])
    
    def test_translate(self):
        dictionary = {'a': 'b'}
        self.assertEqual(sgfrename.translate('a', dictionary), 'b')
    
    def test_translate_negex(self):
        dictionary = {r'^a$': 'b'}
        self.assertNotEqual(sgfrename.translate('aa', dictionary), 'b')
    
    def test_find_location(self):
        self.assertEqual(sgfrename.find_location('CA[Windows-1252]SZ[19]AP[sgfrename]GN[Rank]PC[The KGS Go Server]'), 'KGS')
    
    def test_get_game_info(self):
        data = '(;GM[1]FF[4]CA[UTF-8]AP[CGoban:3]ST[2]RU[Chinese]SZ[19]KM[0.50]TM[300]OT[5x30 byo-yomi]PW[abc]PB[def]WR[4段]BR[3级]DT[2019-08-23]PC[The KGS Go Server at http://www.gokgs.com/])'
        game_info = {
            'date': '2019-08-23',
            'blackname': 'def',
            'whitename': 'abc',
            'blackrank': '3k',
            'whiterank': '4d',
            'result': 'unknown-result',
            'location': 'KGS'
        }
        self.assertEqual(sgfrename.get_game_info(data), game_info)

if __name__ == '__main__':
    unittest.main()
