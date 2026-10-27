SYNTHETIC: a real paperweight run, scored against synthetic reviewer grades; its agreement numbers are no finding about paperweight.
Weight: Light to Medium (3/14)

The paper offers some support for standardization by pointing to an existing precedent and proposing the same semantics for `vector` and `vector<bool>`. Its case is thinnest on why the change matters, who needs it, and why it belongs in the standard; it also leaves several practical and coordination questions unaddressed.

- The paper identifies `inplace_vector` as prior art and proposes carrying over its semantics and specification.
- It says the operations are just as useful in `vector`, but does not substantiate the need or identify who would benefit.
- It asserts that the operations should be added to the standard without explaining why standardization is needed.
- The paper does not address coordination, why a library could not provide the functionality, or implementation experience.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Medium (3.50/14, close to Light)

Provisionally addressed: 4 of 7. Provisional points: 3.50 of 14. Unsupported quotes rejected: 10. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.50   corroborated 3.67   accumulate 3.50   max 4.67

## SUMMARY
grades: motivation 0.83  audience 0.50  prior_art 1.50  vehicle 0.67  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 59 of 63 section-criterion pairs unanimous (94%)
single-sample totals would have been: 4.00 / 2.50 / 4.00   (all 3 samples: 3.50)
headings: h2 8
on threshold: prior_art
splits: motivation[6] 2/0/0  audience[4] 1/0/0  audience[6] 0/0/2  vehicle[4] 0/0/1
## END SUMMARY

## motivation - grade 0.83 (fired in 2 of 9 sections, strong in 0)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Introduction                                 1/1/1  -> 1.00
  [4] Motivation and Scope                         0/0/0  -> 0.00
  [5] Impact On the Standard                       0/0/0  -> 0.00
  [6] Design Decisions                             2/0/0  -> 0.67
  [7] Technical Specifications                     0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Now that we have `try_*_back` in `inplace_vector`, we should add it to `vector` and explore adding it to other sequence containers that provide `push_back` and `emplace_back`.
candidate 2 (found by 1 of 27 passes): There is currently no method to set the capacity, so it is not quite as useful here.

## audience - grade 0.50 (fired in 2 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.50   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation and Scope                         1/0/0  -> 0.33
  [5] Impact On the Standard                       0/0/0  -> 0.00
  [6] Design Decisions                             0/0/2  -> 0.67
  [7] Technical Specifications                     0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): In P0843R7, `try_push_back` and `try_emplace_back` were added to `inplace_vector`. They are just as useful in `vector`.
candidate 2 (found by 1 of 27 passes): However, there is currently no method to set the capacity, so it is not quite as useful here.

## prior_art - grade 1.50 (fired in 2 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation and Scope                         1/1/1  -> 1.00
  [5] Impact On the Standard                       0/0/0  -> 0.00
  [6] Design Decisions                             2/2/2  -> 2.00
  [7] Technical Specifications                     0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): This paper proposes adding `try_push_back` and `try_emplace_back` to `vector` and `vector<bool>`. They would have the same exact semantics as they do for `inplace_vector`, including the same specification.
candidate 2 (found by 2 of 27 passes): In P0843R7, `try_push_back` and `try_emplace_back` were added to `inplace_vector`. They are just as useful in `vector`.
candidate 3 (found by 1 of 27 passes): In P0843R7, `try_push_back` and `try_emplace_back` were added to `inplace_vector`.

## vehicle - grade 0.67 (fired in 2 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation and Scope                         0/0/1  -> 0.33
  [5] Impact On the Standard                       0/0/0  -> 0.00
  [6] Design Decisions                             1/1/1  -> 1.00
  [7] Technical Specifications                     0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): This paper proposes adding `try_push_back` and `try_emplace_back` to `vector` and `vector<bool>`. They would have the same exact semantics as they do for `inplace_vector`, including the same specification.
candidate 2 (found by 1 of 27 passes): They are just as useful in `vector`.

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

-->
