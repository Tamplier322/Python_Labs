WORDS = r'\b[a-zA-Z\d]+\b'
NUMBERS = r'\b\d+\b'
SENTENCES = r'[.!\?]+'
NON_DECL_SENTENCES = r'[!\?]+'

ABBREVIATIONS1 = [
'jan.', 'feb.', 'mar.', 'apr.', 'jun.', 'jul.', 'aug.', 'sep.', 'oct.', 'nov.', 'dec.',
'mon.', 'tue.', 'wed.', 'thu', 'fri.', 'sat.', 'sun.',
'etc.', 'vs.', 'jr.', 'sr.', 'mr.', 'ms.', 'mrs.', 'smb.', 'smth.', 'adj.', 'prep.', 'pp.', 'par.', 'ex.',
'pl.', 'edu.', 'appx.', 'sec.', 'gm.', 'cm.', 'yr.', ]

ABBREVIATIONS2 = ['e.g.', 'i.e.', 'p.s.', 'ph.d.']