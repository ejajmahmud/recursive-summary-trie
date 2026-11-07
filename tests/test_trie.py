"""Tests for recursive-summary-trie."""
import unittest
from recursive_summary_trie.trie import RecursiveSummaryTrie


class TestSummaryTrie(unittest.TestCase):
    def test_trie_assembly(self):
        t = RecursiveSummaryTrie("Project Root")
        t.start_chapter("c1", "Chap 1 summary")
        t.add_turn("t1", "T1 sum", "verbatim text 1")
        t.add_turn("t2", "T2 sum", "verbatim text 2")

        prompt = t.assemble_prompt(max_verbatim_turns=1)
        self.assertIn("[System Global Goal]: Project Root", prompt)
        self.assertIn("Chap 1 summary", prompt)
        self.assertIn("[Turn t1 (Summary)]: T1 sum", prompt)
        self.assertIn("[Turn t2 (Verbatim)]: verbatim text 2", prompt)
