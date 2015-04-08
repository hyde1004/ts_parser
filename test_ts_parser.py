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

	def help_loop_read(self):
		TS_FILE_NAME = '2_HDForum_H264.ts'
		parser = TsParser(TS_FILE_NAME)

		while True:
			parser.read_one_packet()
			if len(parser.packet) != 188:
				raise ZeroDivisionError

	def test_read_one_packet(self):
		TS_FILE_NAME = '2_HDForum_H264.ts'
		parser = TsParser(TS_FILE_NAME)
		packet = parser.read_one_packet()
		self.assertEqual(0x47, packet[0])

		# self.assertRaises(ZeroDivisionError, self.help_loop_read )

if __name__ == '__main__':
	unittest.main(warnings='ignore')