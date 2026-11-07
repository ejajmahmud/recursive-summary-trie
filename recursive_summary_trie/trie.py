"""Core Recursive Summary Trie implementation."""
from typing import Dict, List, Any, Optional


class TrieNode:
    def __init__(self, node_id: str, summary: str, level: int):
        self.node_id = node_id
        self.summary = summary
        self.level = level  # 0: root, 1: chapter, 2: turn
        self.children: List["TrieNode"] = []
        self.verbatim_text: Optional[str] = None

    def add_child(self, child: "TrieNode"):
        self.children.append(child)


class RecursiveSummaryTrie:
    def __init__(self, root_goal: str):
        self.root = TrieNode("root", root_goal, level=0)
        self._current_chapter: Optional[TrieNode] = None

    def start_chapter(self, chapter_id: str, chapter_summary: str) -> TrieNode:
        chapter = TrieNode(chapter_id, chapter_summary, level=1)
        self.root.add_child(chapter)
        self._current_chapter = chapter
        return chapter

    def add_turn(self, turn_id: str, turn_summary: str, verbatim_text: str) -> TrieNode:
        if not self._current_chapter:
            self.start_chapter("default_chapter", "General discussion")
        turn = TrieNode(turn_id, turn_summary, level=2)
        turn.verbatim_text = verbatim_text
        self._current_chapter.add_child(turn)
        return turn

    def assemble_prompt(self, max_verbatim_turns: int = 2) -> str:
        lines = [f"[System Global Goal]: {self.root.summary}"]
        for ch in self.root.children:
            lines.append(f"[Chapter: {ch.node_id}]: {ch.summary}")
            turns = ch.children
            # Show summary for older turns, verbatim for recent turns
            for i, t in enumerate(turns):
                if i >= len(turns) - max_verbatim_turns:
                    lines.append(f"  [Turn {t.node_id} (Verbatim)]: {t.verbatim_text}")
                else:
                    lines.append(f"  [Turn {t.node_id} (Summary)]: {t.summary}")
        return "\n".join(lines)
