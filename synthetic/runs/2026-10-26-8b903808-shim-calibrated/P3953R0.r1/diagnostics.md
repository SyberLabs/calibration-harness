SYNTHETIC: produced by the calibration shim from simulated votes; not a paperweight run, and no finding about paperweight.
# Diagnostics

Provisional: Heavy (7.17/14, close to Medium)

Provisionally addressed: 5 of 7. Provisional points: 7.17 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.17   corroborated 7.00   accumulate 7.17   max 8.33

## SUMMARY
grades: motivation 1.17  audience 0.00  prior_art 2.00  vehicle 1.00  coordination 0.00  insufficiency 1.00  implementation 2.00
sample agreement: 41 of 42 section-criterion pairs unanimous (98%)
single-sample totals would have been: 7.00 / 7.00 / 7.50   (all 3 samples: 7.17)
headings: h2 5
on threshold: insufficiency, implementation
splits: motivation[5] 1/1/2
## END SUMMARY

## motivation - grade 1.17 (fired in 2 of 6 sections, strong in 0)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Motivation                                   1/1/1  -> 1.00
  [4] Proposed Naming: std::dynamicformat          0/0/0  -> 0.00
  [5] Impact on existing code                      1/1/2  -> 1.33
  [6] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 18 passes): - "runtime" suggests evaluation timing
candidate 2 (found by 1 of 18 passes): `std::runtime_format` was accurate when introduced
candidate 3 (found by 1 of 18 passes): with the adoption of `constexpr`
candidate 4 (found by 1 of 18 passes): there will be no impact on existing code

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

## prior_art - grade 2.00 (fired in 2 of 6 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Proposed Naming: std::dynamicformat          0/0/0  -> 0.00
  [5] Impact on existing code                      2/2/2  -> 2.00
  [6] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 18 passes): compile time, making its name misleading. This paper proposes renaming `std::runtime_format`
candidate 2 (found by 1 of 18 passes): can now be evaluated at compile time,
candidate 3 (found by 1 of 18 passes): `std::dynamic_format` to better reflect its semantics and avoid confusion in `constexpr` contexts.
candidate 4 (found by 1 of 18 passes): for C++26 there will be no

## vehicle - grade 1.00 (fired in 2 of 6 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Motivation                                   1/1/1  -> 1.00
  [4] Proposed Naming: std::dynamicformat          0/0/0  -> 0.00
  [5] Impact on existing code                      0/0/0  -> 0.00
  [6] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 18 passes): compile-time format string checks in `std::format`. Subsequently, [P3391] made `std::format`
candidate 2 (found by 1 of 18 passes): misleading. This paper proposes renaming `std::runtime_format` to `std::dynamic_format` to better reflect its
candidate 3 (found by 1 of 18 passes): `std::format`. Subsequently, [P3391] made `std::format` usable in constant evaluation. As a
candidate 4 (found by 1 of 18 passes): - The facility actually describes

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

## insufficiency - grade 1.00 (fired in 1 of 6 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 2/2/2  -> 2.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Proposed Naming: std::dynamicformat          0/0/0  -> 0.00
  [5] Impact on existing code                      0/0/0  -> 0.00
  [6] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 18 passes): title: "Rename std::runtime_format"
candidate 2 (found by 1 of 18 passes): - "Victor Zverovich <victor.zverovich@gmail.com>"

## implementation - grade 2.00  [binary: max] (fired in 1 of 6 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 2/2/2  -> 2.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Proposed Naming: std::dynamicformat          0/0/0  -> 0.00
  [5] Impact on existing code                      0/0/0  -> 0.00
  [6] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 18 passes): — Phil Karlton
candidate 2 (found by 1 of 18 passes): title: "Rename std::runtime_format"
