'''
Created on Oct 18, 2014
testing class IPythonTOC
@author: bren
'''
import unittest
from IPythonTOC import IPythonTOC

toc = IPythonTOC()

class TestTOC(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testSetTitle(self):
        tm = 'test title'
        toc.title = tm
        self.assertEqual(toc.title, tm, 'setting class title property')
        
    def testFormatTitle(self):
        tm = 'test title'
        self.assertEqual('test_title', toc.formatTitle(tm), 'formatting title string')
        tm = 'test + title'
        tsttm = toc.formatTitle(tm)
        self.assertEqual('test_title', tsttm, 'formatting title string- {} : {}'.format(tm, tsttm))

    def testGenMarkdownCell(self):
        tm = 'test title'
        toc.title = tm
        tmd = toc.genTOCMarkdownCell()
        tmdTst = tmd.split('\n')
        self.assertEqual("<a id='test_title'></a>", tmdTst[0], 'formatting markdown - {} : {}'.format(tm, tmdTst[0]))
        self.assertEqual("###test title", tmdTst[1], 'formatting markdown - {} : {}'.format(tm, tmdTst[1]))

    def testGenEntry(self):
        tm = 'test title'
        toc.title = tm
        tmd = toc.genTOCEntry()
        self.assertEqual("[test title](#test_title)", tmd, 'formatting markdown - {} : {}'.format(tm, tmd))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()