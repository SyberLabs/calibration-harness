SYNTHETIC: a real paperweight run, scored against synthetic reviewer grades; its agreement numbers are no finding about paperweight.
# Diagnostics

Provisional: Heavy (7.17/14, close to Medium)

Provisionally addressed: 5 of 7. Provisional points: 7.17 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.17   corroborated 8.00   accumulate 7.17   max 8.33

## SUMMARY
grades: motivation 2.00  audience 0.67  prior_art 2.00  vehicle 0.50  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 61 of 63 section-criterion pairs unanimous (97%)
single-sample totals would have been: 7.50 / 7.50 / 6.50   (all 3 samples: 7.17)
headings: h2 8
on threshold: implementation
splits: audience[5] 2/2/0  prior_art[2] 1/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 2 of 9 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] ABSTRACT                                     0/0/0  -> 0.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 STRAW POLLS                                0/0/0  -> 0.00
  [5] 3 MOTIVATION                                 2/2/2  -> 2.00
  [6] 4 DISCUSSION                                 2/2/2  -> 2.00
  [7] 5 WORDING                                    0/0/0  -> 0.00
  [8] A ACKNOWLEDGMENTS                            0/0/0  -> 0.00
  [9] B BIBLIOGRAPHY                               0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): The subscript in `#2` does not work because, even though `array<int, 4>` is an associated namespace and `x` is convertible to `array<int, 4>`, the `array::operator[]` member function is not found.
candidate 2 (found by 3 of 27 passes): Currently, every operator has its own set of restrictions and extras.

## audience - grade 0.67 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] ABSTRACT                                     0/0/0  -> 0.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 STRAW POLLS                                0/0/0  -> 0.00
  [5] 3 MOTIVATION                                 2/2/0  -> 1.33
  [6] 4 DISCUSSION                                 0/0/0  -> 0.00
  [7] 5 WORDING                                    0/0/0  -> 0.00
  [8] A ACKNOWLEDGMENTS                            0/0/0  -> 0.00
  [9] B BIBLIOGRAPHY                               0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): I always had these unwrapping overloads in my implementation of `constant_wrapper` shipping in the vir-simd library (`vir::constexpr_wrapper`). While replacing my implementation with `std::constant_wrapper` I noticed the mismatch.

## prior_art - grade 2.00 (fired in 3 of 9 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] ABSTRACT                                     1/0/0  -> 0.33
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 STRAW POLLS                                0/0/0  -> 0.00
  [5] 3 MOTIVATION                                 2/2/2  -> 2.00
  [6] 4 DISCUSSION                                 2/2/2  -> 2.00
  [7] 5 WORDING                                    0/0/0  -> 0.00
  [8] A ACKNOWLEDGMENTS                            0/0/0  -> 0.00
  [9] B BIBLIOGRAPHY                               0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Looking at `std::reference_wrapper` we see that this same issue has been resolved via an `operator()` overload that unwraps and applies `INVOKE`.
candidate 2 (found by 3 of 27 passes): In terms of consistency we also have `std::reference_wrapper` to consider. The similar naming is not accidental. Consequently, the unwrapping behavior should also be consistent.
candidate 3 (found by 1 of 27 passes): This paper proposes unwrapping overloads of `operator()` and `operator[]` to `constant_wrapper`.

## vehicle - grade 0.50 (fired in 1 of 9 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] ABSTRACT                                     0/0/0  -> 0.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 STRAW POLLS                                0/0/0  -> 0.00
  [5] 3 MOTIVATION                                 0/0/0  -> 0.00
  [6] 4 DISCUSSION                                 1/1/1  -> 1.00
  [7] 5 WORDING                                    0/0/0  -> 0.00
  [8] A ACKNOWLEDGMENTS                            0/0/0  -> 0.00
  [9] B BIBLIOGRAPHY                               0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): The only possibility that is not a breaking change is to add syntax that opts into new behavior, which has a high acceptance barrier.

## coordination - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] ABSTRACT                                     0/0/0  -> 0.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 STRAW POLLS                                0/0/0  -> 0.00
  [5] 3 MOTIVATION                                 0/0/0  -> 0.00
  [6] 4 DISCUSSION                                 0/0/0  -> 0.00
  [7] 5 WORDING                                    0/0/0  -> 0.00
  [8] A ACKNOWLEDGMENTS                            0/0/0  -> 0.00
  [9] B BIBLIOGRAPHY                               0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] ABSTRACT                                     0/0/0  -> 0.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 STRAW POLLS                                0/0/0  -> 0.00
  [5] 3 MOTIVATION                                 0/0/0  -> 0.00
  [6] 4 DISCUSSION                                 0/0/0  -> 0.00
  [7] 5 WORDING                                    0/0/0  -> 0.00
  [8] A ACKNOWLEDGMENTS                            0/0/0  -> 0.00
  [9] B BIBLIOGRAPHY                               0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 1 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] ABSTRACT                                     0/0/0  -> 0.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 STRAW POLLS                                0/0/0  -> 0.00
  [5] 3 MOTIVATION                                 2/2/2  -> 2.00
  [6] 4 DISCUSSION                                 0/0/0  -> 0.00
  [7] 5 WORDING                                    0/0/0  -> 0.00
  [8] A ACKNOWLEDGMENTS                            0/0/0  -> 0.00
  [9] B BIBLIOGRAPHY                               0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): I always had these unwrapping overloads in my implementation of `constant_wrapper` shipping in the vir-simd library (`vir::constexpr_wrapper`).
candidate 2 (found by 1 of 27 passes): I always had these unwrapping overloads in my implementation of `constant_wrapper` shipping in the vir-simd library (`vir::constexpr_wrapper`). While replacing my implementation with `std::constant_wrapper` I noticed the mismatch.
