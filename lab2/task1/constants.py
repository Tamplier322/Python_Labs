WORD_PATTERN = r'\b[a-zA-Z\d]+\b'
NUMBER_PATTERN = r'\b\d+\b'
SENTENCE_PATTERN = r'[.!\?]+'
NON_DECLARATIVE_SENTENCE_PATTERN = r'[!\?]+'

ONE_WORD_ABBREVIATIONS = [
'jan.', 'feb.', 'mar.', 'apr.', 'jun.', 'jul.', 'aug.', 'sep.', 'oct.', 'nov.', 'dec.',
'mon.', 'tue.', 'wed.', 'thu', 'fri.', 'sat.', 'sun.',
'etc.', 'vs.', 'jr.', 'sr.', 'mr.', 'ms.', 'mrs.', 'smb.', 'smth.', 'adj.', 'prep.', 'pp.', 'par.', 'ex.',
'pl.', 'edu.', 'appx.', 'sec.', 'gm.', 'cm.', 'yr.', ]

TWO_WORDS_ABBREVIATIONS = ['e.g.', 'i.e.', 'p.s.', 'ph.d.']