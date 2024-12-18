import unittest

# 테스트할 함수 (예시)
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)  # 성공해야 함

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)  # 성공해야 함
        self.assertEqual(subtract(5, 3), 1)  # 실패해야 함 (오류를 유도)

if __name__ == '__main__':
    unittest.main()
