# test_blockforce.py
"""
Tests for BlockForce module.
"""

import unittest
from blockforce import BlockForce

class TestBlockForce(unittest.TestCase):
    """Test cases for BlockForce class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockForce()
        self.assertIsInstance(instance, BlockForce)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockForce()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
