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


class TestCountNonDeclarativeSentences(unittest.TestCase):
    def test1_for_ND_sentences(self):
        expected = 0
        actual = statistic_util.amount_of_non_declarative_sentences('')
        self.assertEqual(actual, expected,
            'Error in test1_for_ND_sentences, sentences must be ' + str(expected))

    def test2_for_ND_sentences(self):
        text = 'Sdfgdsfg, mr. sdfaassd. ashdfjh etc. ajsdfja PH.D. - asdfasdf?'
        expected = 1
        actual = statistic_util.amount_of_non_declarative_sentences(text)
        self.assertEqual(actual, expected,
            'Error in test2_for_ND_sentences, sentences must be ' + str(expected))

    def test3_for_ND_sentences(self):
        text = 'Hahsdgfhasgdf!!! asdfasdasdf; dsf... jhgfd... gasdf etc. aadsfaasd?'
        expected = 2
        actual = statistic_util.amount_of_non_declarative_sentences(text)
        self.assertEqual(actual, expected,
            'Error in test3_for_ND_sentences, sentences must be ' + str(expected))


class TestGetAverageSentenceLength(unittest.TestCase):
    def test1_for_average_sentence_length(self):
        expected = 0
        actual = statistic_util.average_sentence_lenght('')
        self.assertEqual(actual, expected,
            'Error in test1_for_average_sentence_length, length must be ' + str(expected))

    def test2_for_average_sentence_length(self):
        text = 'Sdfgdsfg, mr. sdfaassd. ashdfjh etc. ajsdfja PH.D. - asdfasdf?'
        expected = round(46 / 2, 2)
        actual = statistic_util.average_sentence_lenght(text)
        self.assertEqual(actual, expected,
            'Error in test2_for_average_sentence_length, length must be ' + str(expected))

    def test3_for_average_sentence_length(self):
        text = 'Hahsdgfhasgdf!!! asdfasdasdf; dsf... jhgfd... gasdf etc. aadsfaasd?'
        expected = round(49 / 4, 2)
        actual = statistic_util.average_sentence_lenght(text)
        self.assertEqual(actual, expected,
            'Error in test3_for_average_sentence_length, length must be ' + str(expected))


class TestAvgWordLength(unittest.TestCase):
    def test1_for_average_word_length(self):
        expected = 0
        actual = statistic_util.average_word_lenght('')
        self.assertEqual(actual, expected,
            'Error in test1_for_average_word_length, length must be ' + str(expected))

    def test2_for_average_word_length(self):
        text = 'Sdfgdsfg, mr. sdfaassd. ashdfjh etc. ajsdfja PH.D. - asdfasdf?'
        expected = round(46 / 9, 2)
        actual = statistic_util.average_word_lenght(text)
        self.assertEqual(actual, expected,
            'Error in test2_for_average_word_length, length must be ' + str(expected))

    def test3_for_average_word_length(self):
        text = 'Hahsdgfhasgdf!!! asdfasdasdf; dsf... jhgfd... gasdf etc. aadsfaasd?'
        expected = round(49 / 7, 2)
        actual = statistic_util.average_word_lenght(text)
        self.assertEqual(actual, expected,
            'Error in test3_for_average_word_length, length must be ' + str(expected))