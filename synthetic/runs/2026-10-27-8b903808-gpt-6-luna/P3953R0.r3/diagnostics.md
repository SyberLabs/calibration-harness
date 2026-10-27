SYNTHETIC: a real paperweight run, scored against synthetic reviewer grades; its agreement numbers are no finding about paperweight.
# Diagnostics

Provisional: Medium (5.00/14)

Provisionally addressed: 3 of 7. Provisional points: 5.00 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.00   corroborated 5.00   accumulate 5.00   max 5.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 1.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 40 of 42 section-criterion pairs unanimous (95%)
single-sample totals would have been: 5.00 / 5.00 / 5.00   (all 3 samples: 5.00)
headings: h2 5
on threshold: none
splits: motivation[4] 0/0/1  prior_art[3] 1/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 6 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Motivation                                   2/2/2  -> 2.00
  [4] Proposed Naming: std::dynamicformat          0/0/1  -> 0.33
  [5] Impact on existing code                      0/0/0  -> 0.00
  [6] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): As a result, `std::runtime_format` can now be evaluated at compile time, making its name misleading.
candidate 2 (found by 3 of 18 passes): Despite its name, `std::runtime_format` can be evaluated at compile time.
candidate 3 (found by 1 of 18 passes): The format string is dynamically provided

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

## prior_art - grade 2.00 (fired in 3 of 6 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Motivation                                   1/1/0  -> 0.67
  [4] Proposed Naming: std::dynamicformat          2/2/2  -> 2.00
  [5] Impact on existing code                      0/0/0  -> 0.00
  [6] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): Subsequently, [P3391] made `std::format` usable in constant evaluation. As a result, `std::runtime_format` can now be evaluated at compile time, making its name misleading.
candidate 2 (found by 3 of 18 passes): This aligns with existing terminology `std::format` such as dynamic format specifiers (`check_dynamic_spec`).
candidate 3 (found by 2 of 18 passes): The real distinction is not when formatting occurs, but how the format string is provided and validated.

## vehicle - grade 1.00 (fired in 2 of 6 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Proposed Naming: std::dynamicformat          0/0/0  -> 0.00
  [5] Impact on existing code                      1/1/1  -> 1.00
  [6] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): This paper proposes renaming `std::runtime_format` to `std::dynamic_format` to better reflect its semantics and avoid confusion in `constexpr` contexts.
candidate 2 (found by 3 of 18 passes): If this is adopted for C++26 there will be no impact on existing code since `std::runtime_format` is a C++26 feature.

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
