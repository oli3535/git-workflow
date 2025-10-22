
import sys
sys.path.append("C:\\Users\\mozou\\Desktop\\githubworkflow\\app")
from app import dedupe_header
def test_unique_columns():
    assert dedupe_header(["id", "name", "age"]) == ["id", "name", "age"]

def test_duplicate_columns():
    assert dedupe_header(["id", "id", "id"]) == ["id", "id.1", "id.2"]

def test_mixed_columns():
    cols = ["id", "name", "id", "name", "name"]
    expected = ["id", "name", "id.1", "name.1", "name.2"]
    assert dedupe_header(cols) == expected

def test_empty_list():
    assert dedupe_header([]) == []

def test_single_column():
    assert dedupe_header(["column"]) == ["column"]

def test_complex_duplicates():
    cols = ["a", "b", "a", "c", "b", "a", "d"]
    expected = ["a", "b", "a.1", "c", "b.1", "a.2", "d"]
    assert dedupe_header(cols) == expected