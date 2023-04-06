import unittest
import first_task


class TestCountSentences(unittest.TestCase):
    def test1_for_sentences(self):
        expected = 0
        actual = first_task.amount_of_sentences('')
        self.assertEqual(actual, expected,
            'Error in test1_for_sentences, sentences must be ' + str(expected))

    def test2_for_sentences(self):
        text = 'Sdfgdsfg, mr. sdfaassd. ashdfjh etc. ajsdfja PH.D. - asdfasdf?'
        expected = 2
        actual = first_task.amount_of_sentences(text)
        self.assertEqual(actual, expected,
            'Error in test2_for_sentences, sentences must be ' + str(expected))

    def test3_for_sentences(self):
        text = 'Hahsdgfhasgdf!!! asdfasdasdf; dsf... jhgfd... gasdf etc. aadsfaasd?'
        expected = 4
        actual = first_task.amount_of_sentences(text)
        self.assertEqual(actual, expected,
            'Error in test3_for_sentences, sentences must be ' + str(expected))


class TestCountNonDeclarativeSentences(unittest.TestCase):
    def test1_for_ND_sentences(self):
        expected = 0
        actual = first_task.amount_of_non_declarative_sentences('')
        self.assertEqual(actual, expected,
            'Error in test1_for_ND_sentences, sentences must be ' + str(expected))

    def test2_for_ND_sentences(self):
        text = 'Sdfgdsfg, mr. sdfaassd. ashdfjh etc. ajsdfja PH.D. - asdfasdf?'
        expected = 1
        actual = first_task.amount_of_non_declarative_sentences(text)
        self.assertEqual(actual, expected,
            'Error in test2_for_ND_sentences, sentences must be ' + str(expected))

    def test3_for_ND_sentences(self):
        text = 'Hahsdgfhasgdf!!! asdfasdasdf; dsf... jhgfd... gasdf etc. aadsfaasd?'
        expected = 2
        actual = first_task.amount_of_non_declarative_sentences(text)
        self.assertEqual(actual, expected,
            'Error in test3_for_ND_sentences, sentences must be ' + str(expected))


class TestGetAverageSentenceLength(unittest.TestCase):
    def test1_for_average_sentence_length(self):
        expected = 0
        actual = first_task.average_sentence_lenght('')
        self.assertEqual(actual, expected,
            'Error in test1_for_average_sentence_length, length must be ' + str(expected))

    def test2_for_average_sentence_length(self):
        text = 'Sdfgdsfg, mr. sdfaassd. ashdfjh etc. ajsdfja PH.D. - asdfasdf?'
        expected = round(46 / 2, 2)
        actual = first_task.average_sentence_lenght(text)
        self.assertEqual(actual, expected,
            'Error in test2_for_average_sentence_length, length must be ' + str(expected))

    def test3_for_average_sentence_length(self):
        text = 'Hahsdgfhasgdf!!! asdfasdasdf; dsf... jhgfd... gasdf etc. aadsfaasd?'
        expected = round(49 / 4, 2)
        actual = first_task.average_sentence_lenght(text)
        self.assertEqual(actual, expected,
            'Error in test3_for_average_sentence_length, length must be ' + str(expected))


class TestAvgWordLength(unittest.TestCase):
    def test1_for_average_word_length(self):
        expected = 0
        actual = first_task.average_word_lenght('')
        self.assertEqual(actual, expected,
            'Error in test1_for_average_word_length, length must be ' + str(expected))

    def test2_for_average_word_length(self):
        text = 'Sdfgdsfg, mr. sdfaassd. ashdfjh etc. ajsdfja PH.D. - asdfasdf?'
        expected = round(46 / 9, 2)
        actual = first_task.average_word_lenght(text)
        self.assertEqual(actual, expected,
            'Error in test2_for_average_word_length, length must be ' + str(expected))

    def test3_for_average_word_length(self):
        text = 'Hahsdgfhasgdf!!! asdfasdasdf; dsf... jhgfd... gasdf etc. aadsfaasd?'
        expected = round(49 / 7, 2)
        actual = first_task.average_word_lenght(text)
        self.assertEqual(actual, expected,
            'Error in test3_for_average_word_length, length must be ' + str(expected))

class TestTopKRepeatedNgram(unittest.TestCase):
    def test1_for_top_k_repeated_ngram(self):
        expected = []
        actual = first_task.top_k_repeated_n_grams('')
        self.assertEqual(actual, expected,
            'Error in test1_for_top_k_repeated_ngram, it\'s must be ' + str(expected))

    def test2_for_top_k_repeated_ngram(self):
        text = 'Hsdgfgdsf, My favorite food burger. And theres no repeated words.'
        expected = [('hsdgfgdsf my favorite', 1), ('my favorite food', 1), ('favorite food burger', 1)]
        actual = first_task.top_k_repeated_n_grams(text, 3, 3)
        self.assertListEqual(actual, expected,
            'Error in test2_for_top_k_repeated_ngram, it\'s must be ' + str(expected))

    def test3_for_top_k_repeated_ngram(self):
        text = 'hasdhf my favorite food is a burger my favorite burger is a burger'
        expected = [('is a burger', 2), ('hasdhf my favorite', 1), ('my favorite food', 1)]
        actual = first_task.top_k_repeated_n_grams(text, 3, 3)
        self.assertListEqual(actual, expected,
            'Error in test3_for_top_k_repeated_ngram, it\'s must be ' + str(expected))