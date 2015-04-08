import unittest
from ts_parser import TsParser

TS_FILE_NAME = '2_HDForum_H264.ts'

class TestTsParser(unittest.TestCase):
	def setUp(self):
		self.parser = TsParser(TS_FILE_NAME)

	def test_init(self):
		self.assertIsInstance(self.parser, TsParser)
		self.assertEqual(self.parser.ts_filename, TS_FILE_NAME)
		self.assertIsNotNone(self.parser.handle)

	def test_init_wrong_filename(self):
		self.assertRaises(IOError, self.helper_wrong_filename)

	@unittest.skip("I don't know how to check number of parameters")
	def test_init_without_filename(self):
		parser = TsParser()
		self.assertIsInstance(parser, TsParser)

	def test_read_one_packet(self):
		packet = self.parser.read_one_packet()
		self.assertEqual(0x47, packet[0])

	def test_raise_exception_if_packet_is_less_size(self):
		self.assertRaises(EOFError, self.helper_loop_read )

	def helper_loop_read(self):
		parser = TsParser(TS_FILE_NAME)

		while True:
			packet = parser.read_one_packet()

	def helper_wrong_filename(self):
		parser = TsParser('wrong_file.ts')

if __name__ == '__main__':
	unittest.main(warnings='ignore')