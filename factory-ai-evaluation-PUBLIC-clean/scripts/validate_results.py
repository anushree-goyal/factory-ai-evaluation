#!/usr/bin/env python3
"""Check internal consistency of publicly shared aggregate results.

Not a reconstruction of raw OpenRouter events or a replay of code tests.
"""
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]

def read_csv(path):
    with (ROOT/path).open(newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

metrics=read_csv('data/factory-usage-by-issue.csv')
score=read_csv('eval/scorecard.csv')
assert len(metrics)==len(score)==6, 'Expected six benchmark cases'
assert [int(r['issue_number']) for r in metrics]==list(range(1,7))
assert [int(r['issue_number']) for r in score]==list(range(1,7))
assert [int(r['total_request_tokens_prompt_plus_completion']) for r in metrics] == [280995,284886,354196,510269,744956,842382]
for row in metrics:
    i=int(row['issue_number'])
    if i < 6:
        assert int(row['input_prompt_tokens_including_cached']) + int(row['output_completion_tokens']) == int(row['total_request_tokens_prompt_plus_completion']), f'Prompt+completion mismatch issue {i}'
        assert int(row['cached_prompt_tokens_subset_of_input']) <= int(row['input_prompt_tokens_including_cached'])
    else:
        assert not row['input_prompt_tokens_including_cached'].strip(), 'Issue #6 split is unavailable; do not fabricate it'
    assert float(row['recorded_api_cost_usd']) == 0.0
assert sum(int(r['total_request_tokens_prompt_plus_completion']) for r in metrics) == 3017684
assert sum(int(r['first_handling_rubric_aligned']=='yes') for r in score) == 4
assert sum(int(r['eventual_rubric_aligned']=='yes') for r in score) == 5
assert sum(int(r['corrective_human_feedback_rounds']) for r in score) == 1
assert all(int(r['first_handling_rubric_aligned']=='yes') for r in score[:4])
assert score[4]['first_handling_rubric_aligned']=='no' and score[4]['eventual_rubric_aligned']=='yes'
assert score[5]['first_handling_rubric_aligned']=='no' and score[5]['eventual_rubric_aligned']=='no'
for pr in [8,9,10,11,12]:
    assert (ROOT/f'evidence/patches/factory-pr-{pr}.patch').exists()
assert (ROOT/'evidence/patches/factory-pr-11-v2.patch').exists()
assert not (ROOT/'evidence/patches/factory-pr-7.patch').exists(), 'PR #7 was not provided; do not imply otherwise'
print('PASS: six issues, aggregate token totals, first/final scorecard, and available patch files are consistent.')
print('Selected Factory tokens: 3,017,684; rubric aligned initially: 4/6; eventually: 5/6.')
print('Caution: raw provider logs and full CI are deliberately outside this public repository.')
