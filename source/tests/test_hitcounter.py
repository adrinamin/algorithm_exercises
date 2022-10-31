import unittest
from datetime import datetime
from hit_counter import hitcounter


class HitCounterTest(unittest.TestCase):

    def test_total_hits(self):
        hc = hitcounter.HitCounter()

        for i in range(10):
            dt = datetime.now()
            timestamp = datetime.timestamp(dt)
            hc.record(timestamp)
        
        self.assertEqual(10, hc.total())

    def test_record_hit(self):
        hc = hitcounter.HitCounter()

        for i in range(1):
            dt = datetime.now()
            timestamp = datetime.timestamp(dt)
            hc.record(timestamp)

        self.assertEqual(1, hc.total())


    def test_range(self):
        hc = hitcounter.HitCounter()

        ts_lower = datetime.timestamp(datetime.now())

        for i in range(10):
            dt = datetime.now()
            timestamp = datetime.timestamp(dt)
            hc.record(timestamp)

        ts_upper = datetime.timestamp(datetime.now())
        
        result = hc.range(ts_lower, ts_upper)

        self.assertEqual(10, result)


if __name__ == '__main__':
    unittest.main()