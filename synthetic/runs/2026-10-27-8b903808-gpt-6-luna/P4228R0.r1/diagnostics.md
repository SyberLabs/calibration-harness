SYNTHETIC: a real paperweight run, scored against synthetic reviewer grades; its agreement numbers are no finding about paperweight.
# Diagnostics

Provisional: Medium (4.67/14)

Provisionally addressed: 5 of 7. Provisional points: 4.67 of 14. Unsupported quotes rejected: 10. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.67   corroborated 4.33   accumulate 4.83   max 5.33

## SUMMARY
grades: motivation 1.50  audience 0.17  prior_art 2.00  vehicle 0.67  coordination 0.00  insufficiency 0.00  implementation 0.33
sample agreement: 57 of 63 section-criterion pairs unanimous (90%)
single-sample totals would have been: 5.00 / 3.50 / 6.00   (all 3 samples: 4.67)
headings: h2 8
on threshold: motivation
splits: audience[4] 0/0/1  prior_art[3] 1/1/0  vehicle[3] 1/0/1  vehicle[4] 0/0/1
        vehicle[6] 2/0/0  implementation[3] 0/0/1
## END SUMMARY

## motivation - grade 1.50 (fired in 2 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Introduction                                 1/1/1  -> 1.00
  [4] Motivation and Scope                         0/0/0  -> 0.00
  [5] Impact On the Standard                       0/0/0  -> 0.00
  [6] Design Decisions                             2/2/2  -> 2.00
  [7] Technical Specifications                     0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Now that we have `try_*_back` in `inplace_vector`, we should add it to `vector` and explore adding it to other sequence containers that provide `push_back` and `emplace_back`.
candidate 2 (found by 2 of 27 passes): The salient difference between `inplace_vector` and `vector` in this case is whether or not the capacity is known at compile time or only at run time.
candidate 3 (found by 1 of 27 passes): There is currently no method to set the capacity, so it is not quite as useful here.

## audience - grade 0.17 (fired in 1 of 9 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation and Scope                         0/0/1  -> 0.33
  [5] Impact On the Standard                       0/0/0  -> 0.00
  [6] Design Decisions                             0/0/0  -> 0.00
  [7] Technical Specifications                     0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): it is common to pre-allocate the maximum capacity needed in a vector

## prior_art - grade 2.00 (fired in 3 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Introduction                                 1/1/0  -> 0.67
  [4] Motivation and Scope                         2/2/2  -> 2.00
  [5] Impact On the Standard                       0/0/0  -> 0.00
  [6] Design Decisions                             2/2/2  -> 2.00
  [7] Technical Specifications                     0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): In P0843R7, `try_push_back` and `try_emplace_back` were added to `inplace_vector`. They are just as useful in `vector`.
candidate 2 (found by 2 of 27 passes): Now that we have `try_*_back` in `inplace_vector`, we should add it to `vector` and explore adding it to other sequence containers that provide `push_back` and `emplace_back`.
candidate 3 (found by 1 of 27 passes): This paper proposes adding `try_push_back` and `try_emplace_back` to `vector` and `vector<bool>`. They would have the same exact semantics as they do for `inplace_vector`, including the same specification.
candidate 4 (found by 1 of 27 passes): The salient difference between `inplace_vector` and `vector` in this case is whether or not the capacity is known at compile time or only at run time.

## vehicle - grade 0.67 (fired in 3 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.83   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Introduction                                 1/0/1  -> 0.67
  [4] Motivation and Scope                         0/0/1  -> 0.33
  [5] Impact On the Standard                       0/0/0  -> 0.00
  [6] Design Decisions                             2/0/0  -> 0.67
  [7] Technical Specifications                     0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): Now that we have `try_*_back` in `inplace_vector`, we should add it to `vector` and explore adding it to other sequence containers that provide `push_back` and `emplace_back`.
candidate 2 (found by 1 of 27 passes): They are just as useful in `vector`.
candidate 3 (found by 1 of 27 passes): The tradeoff of adding an API with an obvious memory safety issue for a questionable micro-optimization (avoiding the internal `if` check against the capacity) isn’t worth doing.

## coordination - grade 0.00 (fired in 0 of 9 sections, strong in 0)
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

## implementation - grade 0.33  [binary: max] (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.33   accumulate 0.33   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Introduction                                 0/0/1  -> 0.33
  [4] Motivation and Scope                         0/0/0  -> 0.00
  [5] Impact On the Standard                       0/0/0  -> 0.00
  [6] Design Decisions                             0/0/0  -> 0.00
  [7] Technical Specifications                     0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): Now that we have `try_*_back` in `inplace_vector`, we should add it to `vector` and explore adding it to other sequence containers that provide `push_back` and `emplace_back`.
