import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_metrics():
    return json.loads((ROOT / "evidence" / "public_metrics.json").read_text(encoding="utf-8"))


def test_green_checkpoint_is_276():
    data = load_metrics()
    assert data["current_locked_green_in_supplied_lineage_evidence"] == 276


def test_302_inventory_is_not_a_pass_claim():
    data = load_metrics()
    inv = data["later_repository_inventory"]
    assert inv["python_test_modules"] == 47
    assert inv["statically_identified_test_functions"] == 302
    assert inv["executed_during_reconciliation"] is False
    assert inv["passing_claim_allowed_from_this_reconciliation"] is False


def test_readme_does_not_invent_276_over_302_pass_rate():
    readme = (ROOT / "README.md").read_text(encoding="utf-8").lower()
    assert "276 of 302 tests passing" not in readme
    assert "91% pass rate" not in readme
    assert "not executed during that reconciliation" in readme


def test_public_repo_history_is_disclosed_as_later_publication():
    readme = (ROOT / "README.md").read_text(encoding="utf-8").lower()
    publication = (ROOT / "docs" / "PUBLICATION_NOTE.md").read_text(encoding="utf-8").lower()
    assert "git history begins when the case study is published" in readme
    assert "no attempt should be made to backdate" in publication


def test_prototype_metrics_remain_available_in_evidence():
    data = load_metrics()
    proto = data["browser_prototype_validation"]
    assert proto["routes"] == 13
    assert proto["interactive_controls"] == 280
    assert proto["modeled_domains"] == 96
    assert proto["subsystem_records"] == 38
    assert proto["all_recorded_checks_passed"] is True
    assert proto["inert_buttons_detected"] == 0
