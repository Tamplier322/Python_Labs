import unittest
import first_task


class TestCountSentences(unittest.TestCase):
    def test1_for_sentences(self):
        expected = 0
        actual = statistic_util.amount_of_sentences('')
        self.assertEqual(actual, expected,
            'Error in test1_for_sentences, sentences must be ' + str(expected))

    def test2_for_sentences(self):
        text = 'Sdfgdsfg, mr. sdfaassd. ashdfjh etc. ajsdfja PH.D. - asdfasdf?'
        expected = 2
        actual = statistic_util.amount_of_sentences(text)
        self.assertEqual(actual, expected,
            'Error in test2_for_sentences, sentences must be ' + str(expected))

    def test3_for_sentences(self):
        text = 'Hahsdgfhasgdf!!! asdfasdasdf; dsf... jhgfd... gasdf etc. aadsfaasd?'
        expected = 4
        actual = statistic_util.amount_of_sentences(text)
        self.assertEqual(actual, expected,
            'Error in test3_for_sentences, sentences must be ' + str(expected))