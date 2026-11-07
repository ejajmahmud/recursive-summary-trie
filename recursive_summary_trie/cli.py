"""CLI for recursive-summary-trie."""
import sys
import argparse
from .trie import RecursiveSummaryTrie


def main():
    parser = argparse.ArgumentParser(description="Recursive Summary Trie")
    parser.add_argument("--demo", action="store_true", help="Run demonstration")
    args = parser.parse_args()

    if args.demo:
        trie = RecursiveSummaryTrie("Migrate PostgreSQL cluster to Aurora")
        trie.start_chapter("ch1_schema", "Schema translation completed with 0 errors")
        trie.add_turn("t1", "Validated DDL", "CREATE TABLE users (id SERIAL PRIMARY KEY);")
        trie.start_chapter("ch2_data", "Active data pump batch migration")
        trie.add_turn("t2", "Sync batch 1", "INSERT INTO users SELECT * FROM legacy_users WHERE id < 1000;")

        print("=== Assembled Context ===")
        print(trie.assemble_prompt(max_verbatim_turns=1))
    else:
        parser.print_help()
    sys.exit(0)


if __name__ == "__main__":
    main()
