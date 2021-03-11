import unittest
import sys
sys.path.append('/home/joe/mycroft-core/')
from __init__ import create_skill, ProgrammingSupport


class __init__test(unittest.TestCase):

    def init_skill(self):
        skill = create_skill()
        self.assertTrue(isinstance(skill, ProgrammingSupport))
        return skill

    def utt_not_applicable(self):
        skill = self.init_skill()
        self.assertEqual(skill.CQS_match_query_phrase("bananas"), None)


if __name__ == '__main__':
    unittest.main()
