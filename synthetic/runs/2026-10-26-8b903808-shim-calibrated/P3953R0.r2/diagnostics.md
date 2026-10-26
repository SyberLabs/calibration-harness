SYNTHETIC: produced by the calibration shim from simulated votes; not a paperweight run, and no finding about paperweight.
# Diagnostics

Provisional: Medium (6.83/14, close to Heavy)

Provisionally addressed: 5 of 7. Provisional points: 6.83 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.83   corroborated 7.00   accumulate 6.83   max 8.00

## SUMMARY
grades: motivation 1.00  audience 0.00  prior_art 2.00  vehicle 0.83  coordination 0.00  insufficiency 1.00  implementation 2.00
sample agreement: 41 of 42 section-criterion pairs unanimous (98%)
single-sample totals would have been: 7.00 / 7.00 / 6.50   (all 3 samples: 6.83)
headings: h2 5
on threshold: insufficiency, implementation
splits: vehicle[2] 1/1/0
## END SUMMARY

## motivation - grade 1.00 (fired in 2 of 6 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Motivation                                   1/1/1  -> 1.00
  [4] Proposed Naming: std::dynamicformat          0/0/0  -> 0.00
  [5] Impact on existing code                      1/1/1  -> 1.00
  [6] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 18 passes): return std::format(std::runtime_format(fmt), value);
candidate 2 (found by 1 of 18 passes): is not when formatting occurs, but how the format
candidate 3 (found by 1 of 18 passes): adoption of `constexpr` `std::format`, the term
candidate 4 (found by 1 of 18 passes): no impact on existing code since

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
candidate 1 (found by 2 of 18 passes): As a result, `std::runtime_format` can now be evaluated at compile time, making
candidate 2 (found by 1 of 18 passes): proposes renaming `std::runtime_format` to `std::dynamic_format` to better reflect its semantics and
candidate 3 (found by 1 of 18 passes): on existing code since `std::runtime_format` is
candidate 4 (found by 1 of 18 passes): C++26 there will be no impact on existing code since `std::runtime_format`

## vehicle - grade 0.83 (fired in 2 of 6 sections, strong in 0)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/0  -> 0.67
  [3] Motivation                                   1/1/1  -> 1.00
  [4] Proposed Naming: std::dynamicformat          0/0/0  -> 0.00
  [5] Impact on existing code                      0/0/0  -> 0.00
  [6] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 18 passes): Subsequently, [P3391] made `std::format` usable in constant evaluation. As a result,
candidate 2 (found by 1 of 18 passes): proposes renaming `std::runtime_format` to `std::dynamic_format` to better reflect its semantics
candidate 3 (found by 1 of 18 passes): Consider the following code:
candidate 4 (found by 1 of 18 passes): constexpr auto f(std::string_view fmt, int value) {

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
candidate 1 (found by 3 of 18 passes): - "Victor Zverovich <victor.zverovich@gmail.com>"

## implementation - grade 2.00  [binary: max] (fired in 1 of 6 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 2/2/2  -> 2.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Proposed Naming: std::dynamicformat          0/0/0  -> 0.00
  [5] Impact on existing code                      0/0/0  -> 0.00
  [6] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 18 passes): title: "Rename std::runtime_format"
candidate 2 (found by 1 of 18 passes): - "Victor Zverovich <victor.zverovich@gmail.com>"
