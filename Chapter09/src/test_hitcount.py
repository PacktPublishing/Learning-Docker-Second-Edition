#########################################
#
#########################################
import unittest
from unittest.mock import patch

import mockredis
import hitcount

class HitCountTest(unittest.TestCase):

    @patch('hitcount.r',
           mockredis.mock_strict_redis_client(host='0.0.0.0', port=6379, db=0))
    def testOneHit(self):
        # increase the hit count for user1
        hitcount.hit("user1")
        # ensure that the hit count for user1 is just 1
        self.assertEqual(b'1', hitcount.getHit("user1"))


if __name__ == '__main__':
    unittest.main()
