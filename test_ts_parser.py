import unittest
from ts_parser import TsParser

class TestTsParser(unittest.TestCase):
	def test_init(self):
		# parser = TsParser()
		# self.assertIsInstance(parser, TsParser)

		TS_FILE_NAME = '2_HDForum_H264.ts'
		parser = TsParser(TS_FILE_NAME)
		self.assertIsInstance(parser, TsParser)
		self.assertEqual(parser.ts_filename, TS_FILE_NAME)
		self.assertIsNotNone(parser.handle)

if __name__ == '__main__':
	unittest.main(warnings='ignore')