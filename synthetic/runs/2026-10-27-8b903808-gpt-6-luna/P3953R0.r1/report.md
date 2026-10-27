SYNTHETIC: a real paperweight run, scored against synthetic reviewer grades; its agreement numbers are no finding about paperweight.
Weight: Medium (5/14)

The paper gives a clear rationale for why the issue matters and situates the proposed change in the history and terminology of the library. Its case is thinnest on who would be affected and why standardization is needed, and it offers no support on coordination, alternatives to standardization, or implementation experience.

- The paper explains that `std::runtime_format` can now be evaluated at compile time, despite its name, and that the format string may be provided dynamically.
- It describes the relevant prior changes and terminology, and notes that adopting the change for C++26 would not affect existing code because `std::runtime_format` is itself a C++26 feature.
- It proposes `std::dynamic_format` as a name that better reflects the semantics and avoids confusion in `constexpr` contexts, but does not establish why this needs to be addressed by the standard.
- The paper does not establish who is affected, how the proposal coordinates with other work, why a library solution would not suffice, or whether there is implementation experience.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Medium (4.50/14)

Provisionally addressed: 3 of 7. Provisional points: 4.50 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.50   corroborated 5.00   accumulate 4.50   max 5.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 0.50  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 40 of 42 section-criterion pairs unanimous (95%)
single-sample totals would have been: 4.50 / 4.50 / 4.50   (all 3 samples: 4.50)
headings: h2 5
on threshold: none
splits: prior_art[3] 1/1/0  prior_art[5] 1/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 6 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Motivation                                   2/2/2  -> 2.00
  [4] Proposed Naming: std::dynamicformat          1/1/1  -> 1.00
  [5] Impact on existing code                      0/0/0  -> 0.00
  [6] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): As a result, `std::runtime_format` can now be evaluated at compile time, making its name misleading.
candidate 2 (found by 3 of 18 passes): Despite its name, `std::runtime_format` can be evaluated at compile time.
candidate 3 (found by 3 of 18 passes): The format string is dynamically provided

## audience - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Proposed Naming: std::dynamicformat          0/0/0  -> 0.00
  [5] Impact on existing code                      0/0/0  -> 0.00
  [6] References                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 4 of 6 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Motivation                                   1/1/0  -> 0.67
  [4] Proposed Naming: std::dynamicformat          2/2/2  -> 2.00
  [5] Impact on existing code                      1/0/1  -> 0.67
  [6] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): Subsequently, [P3391] made `std::format` usable in constant evaluation. As a result, `std::runtime_format` can now be evaluated at compile time, making its name misleading.
candidate 2 (found by 3 of 18 passes): This aligns with existing terminology `std::format` such as dynamic format specifiers (`check_dynamic_spec`).
candidate 3 (found by 2 of 18 passes): The name `std::runtime_format` was accurate when introduced in [P2918], as format strings were not usable in constant evaluation.
candidate 4 (found by 2 of 18 passes): If this is adopted for C++26 there will be no impact on existing code since `std::runtime_format` is a C++26 feature.

## vehicle - grade 0.50 (fired in 1 of 6 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Proposed Naming: std::dynamicformat          0/0/0  -> 0.00
  [5] Impact on existing code                      0/0/0  -> 0.00
  [6] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): This paper proposes renaming `std::runtime_format` to `std::dynamic_format` to better reflect its semantics and avoid confusion in `constexpr` contexts.

## coordination - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Proposed Naming: std::dynamicformat          0/0/0  -> 0.00
  [5] Impact on existing code                      0/0/0  -> 0.00
  [6] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Proposed Naming: std::dynamicformat          0/0/0  -> 0.00
  [5] Impact on existing code                      0/0/0  -> 0.00
  [6] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Proposed Naming: std::dynamicformat          0/0/0  -> 0.00
  [5] Impact on existing code                      0/0/0  -> 0.00
  [6] References                                   0/0/0  -> 0.00
candidates: (none validated)

-->
