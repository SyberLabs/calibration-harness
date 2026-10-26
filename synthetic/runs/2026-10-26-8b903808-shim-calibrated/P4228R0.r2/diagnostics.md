SYNTHETIC: produced by the calibration shim from simulated votes; not a paperweight run, and no finding about paperweight.
# Diagnostics

Provisional: Medium (4.00/14)

Provisionally addressed: 4 of 7. Provisional points: 4.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.00   corroborated 4.00   accumulate 4.00   max 6.00

## SUMMARY
grades: motivation 1.00  audience 0.00  prior_art 1.00  vehicle 1.00  coordination 1.00  insufficiency 0.00  implementation 0.00
sample agreement: 63 of 63 section-criterion pairs unanimous (100%)
single-sample totals would have been: 4.00 / 4.00 / 4.00   (all 3 samples: 4.00)
headings: h2 8
on threshold: vehicle, coordination
splits: none
## END SUMMARY

## motivation - grade 1.00 (fired in 2 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation and Scope                         0/0/0  -> 0.00
  [5] Impact On the Standard                       0/0/0  -> 0.00
  [6] Design Decisions                             0/0/0  -> 0.00
  [7] Technical Specifications                     1/1/1  -> 1.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): - "Nevin “:-)” Liber <nliber@anl.gov>"
candidate 2 (found by 2 of 27 passes): constexpr optional try_emplace_back(Args&&... args);
candidate 3 (found by 1 of 27 passes): title: "try_*_back For Other Sequence Containers"
candidate 4 (found by 1 of 27 passes): constexpr void push_back(const bool& x);

## audience - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation and Scope                         0/0/0  -> 0.00
  [5] Impact On the Standard                       0/0/0  -> 0.00
  [6] Design Decisions                             0/0/0  -> 0.00
  [7] Technical Specifications                     0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.00 (fired in 2 of 9 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation and Scope                         1/1/1  -> 1.00
  [5] Impact On the Standard                       0/0/0  -> 0.00
  [6] Design Decisions                             1/1/1  -> 1.00
  [7] Technical Specifications                     0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): the “hot path” (low latency path) to just `push_back` elements, knowing that
candidate 2 (found by 1 of 27 passes): to `inplace_vector`. They are just as useful
candidate 3 (found by 1 of 27 passes): P0843R7, `try_push_back` and `try_emplace_back` were added to `inplace_vector`. They
candidate 4 (found by 1 of 27 passes): do not add these functions to `vector`, `deque` or `list`.

## vehicle - grade 1.00 (fired in 1 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation and Scope                         0/0/0  -> 0.00
  [5] Impact On the Standard                       2/2/2  -> 2.00
  [6] Design Decisions                             0/0/0  -> 0.00
  [7] Technical Specifications                     0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): This is purely additive.

## coordination - grade 1.00 (fired in 1 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 2/2/2  -> 2.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation and Scope                         0/0/0  -> 0.00
  [5] Impact On the Standard                       0/0/0  -> 0.00
  [6] Design Decisions                             0/0/0  -> 0.00
  [7] Technical Specifications                     0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): title: "try_*_back For Other Sequence Containers"
candidate 2 (found by 1 of 27 passes): - "Nevin “:-)” Liber <nliber@anl.gov>"

## insufficiency - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation and Scope                         0/0/0  -> 0.00
  [5] Impact On the Standard                       0/0/0  -> 0.00
  [6] Design Decisions                             0/0/0  -> 0.00
  [7] Technical Specifications                     0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation and Scope                         0/0/0  -> 0.00
  [5] Impact On the Standard                       0/0/0  -> 0.00
  [6] Design Decisions                             0/0/0  -> 0.00
  [7] Technical Specifications                     0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidates: (none validated)
