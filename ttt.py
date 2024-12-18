import unittest
import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO, format='%(message)s')

# 테스트 대상 함수
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

class TestMathOperations(unittest.TestCase):

    def setUp(self):
        logging.info("\n=== START TEST: %s ===", self._testMethodName)

    def tearDown(self):
        logging.info("=== END TEST: %s ===\n\n", self._testMethodName)

    def test_add(self):
        result = add(2, 3)
        logging.info(f"Result of add(2, 3): {result}")
        self.assertEqual(result, 5)

    def test_subtract_failure(self):
        result = subtract(5, 3)
        logging.info(f"Result of subtract(5, 3): {result}")
        self.assertEqual(result, 1)  # 실패 의도


    def test_subtract_success(self):
        result = subtract(5, 3)
        logging.info(f"Result of subtract(5, 3): {result}")
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
