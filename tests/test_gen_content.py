import unittest
from src.gen_content import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_valid_title(self):
        self.assertEqual(extract_title("# Hello"), "Hello")

    def test_title_with_whitespace(self):
        self.assertEqual(extract_title("   # Hello World   "), "Hello World")

    def test_no_title(self):
        with self.assertRaises(ValueError):
            extract_title("This is a markdown file without an H1 header.")

    def test_multiple_lines(self):
        markdown = """
        Some content
        # Welcome to the site
        More content
        """
        self.assertEqual(extract_title(markdown), "Welcome to the site")

    def test_no_h1_but_other_headers(self):
        markdown = """
        ## Subheader
        ### Another subheader
        """
        with self.assertRaises(ValueError):
            extract_title(markdown)
            
    def test_none(self):
        try:
            extract_title(
                """
no title
"""
            )
            self.fail("Should have raised an exception")
        except Exception as e:
            pass

if __name__ == "__main__":
    unittest.main()
