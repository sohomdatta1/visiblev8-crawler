import unittest
import os.path
import filecmp

from task_queue.vv8web_task_queue.util.log_parser_v2 import parse_log

dirname = os.path.dirname(__file__)
log_dir = os.path.join(dirname, 'logs')
parsed_log_dir = os.path.join(dirname, 'parsed_logs')


# Testing api_v1 and a little bit of webpage, sending a valid webpage and two invalid ones to ensure
# our backend url validation works correctly.
class BackendApiTests(unittest.TestCase):
    def test_parser_accuracy(self):
        log_files = [
            'akamai.net.txt',
            'https-__appleinsider.com.txt',
            'https-__coinsbit.io.txt',
            'https-__iqoption.txt'
        ]
        parsed_files = [
            'akamai.net_parsed.json',
            'https-__appleinsider.com_parsed.json',
            'https-__coinsbit.io_parsed.json',
            'https-__iqoption_parsed.json'
        ]
        for in_file, out_file in zip(log_files, parsed_files):
            with open(os.path.join(log_dir, in_file), 'rt') as fp:
                log_str = fp.read()
            log_json = parse_log(log_str)
            with open(os.path.join(parsed_log_dir, out_file), 'rt') as fp:
                act_log_json = fp.read()
            self.assertEqual(log_json, act_log_json)


if __name__ == '__main__':
    unittest.main()
