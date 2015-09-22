import unittest
import PatternMatch
import FolderManager

delimiters=['-', ',',' ','']

class KnownValues(unittest.TestCase):
    '''Test patterns to ensure things are working consistently.'''
    threshold2_match = (
    ('Smith,John-12345','12345-Smith,John'),
    ('Jane-0000','DoeJane-0000'),
    ('mike james 3321','3321-James,Mike'),
    ('Doe,John-12345','12345 Doe John'),
    ('green mike','12345-Green,Mike'),
    ('45552 Hakim Amar','Amar Hakim'),
    ('00000 nobody else','00000-Nobody,Else')
    )

    threshold1_match = (
    ('Smith,John-12345','12345,BlahbetiBlahBlah'),
    ('78901 Mike Belanger','Mike Green')
    )

    no_match = (
    ('Smith,John-12345',''),
    ('0000000','11111')
    )

    def test_match_min2(self):
        '''Determines if patternmatch returns matching pairs
        as expected at a threshold of 2'''
        for pattern, pattern_query in self.threshold2_match:
            p = PatternMatch.Pattern(pattern)
            q = PatternMatch.Pattern(pattern_query)
            p.chunkify(delimiters)
            q.chunkify(delimiters)

            result = p.match(q)
            self.assertGreaterEqual(len(result), 2)

    def test_no_match(self):
        '''Test to see if patterns get rejected as they are
        not sufficiently similar.'''
        for pattern, pattern_query in self.no_match:
            p = PatternMatch.Pattern(pattern)
            q = PatternMatch.Pattern(pattern_query)
            p.chunkify(delimiters)
            q.chunkify(delimiters)

            result = p.match(q)
            self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
