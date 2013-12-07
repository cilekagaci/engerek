# coding=utf-8
import unittest
from engerek import BalkansDeasciifier


class TestBalkansDeasciifier(unittest.TestCase):

    def test_default(self):
        deasciifier = BalkansDeasciifier()

        self.assertEqual(
            deasciifier.deasciify(
                u'Hadi bir masal uyduralim, icinde mutlu, doygun, telassiz'
                u' durdugumuz.'
            ),
            u'Hadi bir masal uyduralım, içinde mutlu, doygun, telaşsız'
            u' durduğumuz.',
        )


if __name__ == '__main__':
    unittest.main()
