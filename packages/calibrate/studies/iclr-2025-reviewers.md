PROXY: real human reviews of ICLR 2025 (Paper Copilot's public list), not paperweight's rubric; nothing here is a finding about paperweight.

# How much reviewers agree, and how many papers a reading needs

The harness's own statistics, run on real human disagreement instead of
simulated reviewers. ICLR 2025 reviewers grade soundness, presentation and
contribution from 1 to 4. A paper's "total" here is their sum, 3 to 12,
standing in for paperweight's sum of seven criteria graded 0 to 2. The
scales differ, so the useful numbers are relative: how well reviewers
agree, and how often a real improvement is detected.

Data: 11,677 papers listed, 11,521 with all three scores.
The source is pinned by sha256 `d288d0348d121671...` and is not
committed, because its repository declares no license. The list orders
each paper's reviews by overall rating (100% of papers with four
or more reviews arrive sorted), so each paper's reviewers were shuffled with
a fixed seed first, keeping every reviewer's grades together. Unshuffled,
"reviewer 1" is the harshest reviewer, and every comparison is skewed.

## How many papers a reading needs

Each row compares a candidate with a single reviewer, both scored against
the mean of the other reviewers on the same paper. The cells show how often
the harness's MAE reading (paired bootstrap, 95%) came out "better" over
200 random draws of that many papers. The first row is no real change:
one reviewer swapped for another, so any reading other than "within noise"
is a false alarm, and its cells count those. The improvements are real
ones, not planted: the average of two or three actual reviewers, which cuts
the error unevenly, paper by paper.

| Candidate against one reviewer | Error change, all papers | 10 papers | 20 papers | 40 papers | 80 papers |
| --- | --- | --- | --- | --- | --- |
| One reviewer swapped for another (9,784 papers) | +1% | 12% false alarms | 6% false alarms | 5% false alarms | 5% false alarms |
| Mean of 2 reviewers instead of one (9,784 papers) | -19% | 18% better | 28% better | 44% better | 72% better |
| Mean of 3 reviewers instead of one (2,051 papers) | -25% | 27% better | 40% better | 66% better | 90% better |

How to read it: a real improvement that cuts the error by about
19% (two reviewers averaged instead of one) reads "better"
18% of the time on ten papers, 28% on twenty and
44% on forty. One that cuts it by about 25% reads
"better" 27% of the time on ten papers.

The false-alarm rate is what a 95% interval should hold to about 5%. On ten
papers it is 12%, and it settles near 5% only from
about forty: the percentile bootstrap draws its interval too narrow when
there are so few papers to resample. A "better" or "worse" on ten papers is
therefore weaker evidence than its 95% suggests. Each reading here uses
1,000 resamples, not the harness's 2,000, to keep the study to
minutes.

## How much reviewers agree

| Measure | Value (95% interval) |
| --- | --- |
| Reviewer ceiling, 3 reviewers (mean pairwise r of totals) | 0.24 |
| Reviewer ceiling, 4 reviewers | 0.24 |
| One reviewer against the mean of the others: bias (a check, should be near 0) | +0.00 (-0.03 to +0.04) |
| One reviewer against the mean of the others: MAE | 1.41 (1.39 to 1.43) |
| One reviewer against the mean of the others: r | 0.32 (0.30 to 0.34) |

A single human reviewer, scored the way the harness scores paperweight,
reaches r = 0.32 against the other reviewers' mean. An
automated grader at that level agrees with the panel about as well as one
of its own members does.

| Criterion | Pairs giving the same grade | r, two reviewers |
| --- | --- | --- |
| soundness | 45% | 0.17 |
| presentation | 43% | 0.17 |
| contribution | 45% | 0.19 |
