SYNTHETIC: a real paperweight run, scored against synthetic reviewer grades; its agreement numbers are no finding about paperweight.
# Diagnostics

Provisional: Heavy (8.00/14)

Provisionally addressed: 6 of 7. Provisional points: 8.00 of 14. Unsupported quotes rejected: 21. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.00   corroborated 7.33   accumulate 9.33   max 9.00

## SUMMARY
grades: motivation 2.00  audience 1.17  prior_art 1.00  vehicle 1.67  coordination 0.00  insufficiency 0.17  implementation 2.00
sample agreement: 73 of 84 section-criterion pairs unanimous (87%)
single-sample totals would have been: 10.00 / 7.50 / 9.50   (all 3 samples: 8.00)
headings: h2 11
on threshold: vehicle, implementation
splits: motivation[4] 1/1/2  motivation[8] 2/0/0  audience[4] 1/1/0  audience[6] 2/0/2
        prior_art[5] 0/2/0  prior_art[6] 2/0/2  prior_art[8] 2/0/0  prior_art[9] 0/0/2
        vehicle[2] 0/1/1  vehicle[7] 2/0/2  insufficiency[7] 1/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 12 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] REVISION HISTORY                             0/0/0  -> 0.00
  [4] INTRODUCTION                                 1/1/2  -> 1.33
  [5] MOTIVATION & SCOPE                           2/2/2  -> 2.00
  [6] STATE OF THE ART                             2/2/2  -> 2.00
  [7] IMPACT ON THE STANDARD                       0/0/0  -> 0.00
  [8] DESIGN DECISIONS                             2/0/0  -> 0.67
  [9] FUTURE DIRECTIONS                            0/0/0  -> 0.00
  [10] ACKNOWLEDGMENTS                              0/0/0  -> 0.00
  [11] REFERENCES                                   0/0/0  -> 0.00
  [12] PROPOSED WORDING                             0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The aim is to transparently select a sufficiently large portion of `<cmath>` in order to be useful but without placing too much burden on compiler vendors.
candidate 2 (found by 3 of 36 passes): This paper seeks to rectify the almost complete absence of `constexpr` in `<cmath>` (and also in `<cstdlib>`), so as to broaden the range of numeric computations that can be performed using standard library facilities.
candidate 3 (found by 3 of 36 passes): However, in `<cmath>`, only the recently added `lerp` is currently declared `constexpr`, thereby artificially restricting what can be done at compile-time within the standard library.
candidate 4 (found by 2 of 36 passes): Despite the fact that GCC neither sets errno nor raises any floating-point exception flags, it prohibits the use of this expression in a `constexpr` context.

## audience - grade 1.17 (fired in 3 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.50   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] REVISION HISTORY                             0/0/0  -> 0.00
  [4] INTRODUCTION                                 1/1/0  -> 0.67
  [5] MOTIVATION & SCOPE                           0/0/0  -> 0.00
  [6] STATE OF THE ART                             2/0/2  -> 1.33
  [7] IMPACT ON THE STANDARD                       0/0/0  -> 0.00
  [8] DESIGN DECISIONS                             0/0/0  -> 0.00
  [9] FUTURE DIRECTIONS                            0/0/0  -> 0.00
  [10] ACKNOWLEDGMENTS                              0/0/0  -> 0.00
  [11] REFERENCES                                   0/0/0  -> 0.00
  [12] PROPOSED WORDING                             0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The aim is to transparently select a sufficiently large portion of `<cmath>` in order to be useful but without placing too much burden on compiler vendors.
candidate 2 (found by 2 of 36 passes): This paper seeks to rectify the almost complete absence of `constexpr` in `<cmath>` (and also in `<cstdlib>`), so as to broaden the range of numeric computations that can be performed using standard library facilities.
candidate 3 (found by 2 of 36 passes): Indeed, at least as early as GCC 5.3.0 almost all functions, besides the special functions, those taking a pointer argument (cf. III C) and those with an explicit dependence on the runtime rounding mode (III B) are declared `constexpr`.

## prior_art - grade 1.00 (fired in 4 of 12 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] REVISION HISTORY                             0/0/0  -> 0.00
  [4] INTRODUCTION                                 0/0/0  -> 0.00
  [5] MOTIVATION & SCOPE                           0/2/0  -> 0.67
  [6] STATE OF THE ART                             2/0/2  -> 1.33
  [7] IMPACT ON THE STANDARD                       0/0/0  -> 0.00
  [8] DESIGN DECISIONS                             2/0/0  -> 0.67
  [9] FUTURE DIRECTIONS                            0/0/2  -> 0.67
  [10] ACKNOWLEDGMENTS                              0/0/0  -> 0.00
  [11] REFERENCES                                   0/0/0  -> 0.00
  [12] PROPOSED WORDING                             0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): The latter applies, in its entirety, to floating-point models with signed zeros, extended with NaNs and signed infinities.
candidate 2 (found by 1 of 36 passes): Both GCC and clang already support `constexpr` within `<cmath>` to varying extents.
candidate 3 (found by 1 of 36 passes): While clang does not go nearly as far as GCC, it does offer some functions as builtins and is able to use them to perform compile time computations, constant propagation and so on.
candidate 4 (found by 1 of 36 passes): since it has already been proposed that, in addition to the arithmetic operations, `complex::norm` and a few other functions be declared `constexpr` [P0415R0].

## vehicle - grade 1.67 (fired in 4 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/1  -> 0.67
  [3] REVISION HISTORY                             0/0/0  -> 0.00
  [4] INTRODUCTION                                 1/1/1  -> 1.00
  [5] MOTIVATION & SCOPE                           2/2/2  -> 2.00
  [6] STATE OF THE ART                             0/0/0  -> 0.00
  [7] IMPACT ON THE STANDARD                       2/0/2  -> 1.33
  [8] DESIGN DECISIONS                             0/0/0  -> 0.00
  [9] FUTURE DIRECTIONS                            0/0/0  -> 0.00
  [10] ACKNOWLEDGMENTS                              0/0/0  -> 0.00
  [11] REFERENCES                                   0/0/0  -> 0.00
  [12] PROPOSED WORDING                             0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): so as to broaden the range of numeric computations that can be performed using standard library facilities.
candidate 2 (found by 3 of 36 passes): This distinction between these two contexts previously implied that any implementation cannot be done as a pure library extension. However, the emergence of `std::is_constant_evaluated()` [P0595] may allow for this be circumvented.
candidate 3 (found by 2 of 36 passes): The aim is to transparently select a sufficiently large portion of `<cmath>` in order to be useful but without placing too much burden on compiler vendors.
candidate 4 (found by 2 of 36 passes): With `std::is_constant_evaluated()` it may be possible to implement the desired behaviour as a pure library extension; previously, this was not the case.

## coordination - grade 0.00 (fired in 0 of 12 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] REVISION HISTORY                             0/0/0  -> 0.00
  [4] INTRODUCTION                                 0/0/0  -> 0.00
  [5] MOTIVATION & SCOPE                           0/0/0  -> 0.00
  [6] STATE OF THE ART                             0/0/0  -> 0.00
  [7] IMPACT ON THE STANDARD                       0/0/0  -> 0.00
  [8] DESIGN DECISIONS                             0/0/0  -> 0.00
  [9] FUTURE DIRECTIONS                            0/0/0  -> 0.00
  [10] ACKNOWLEDGMENTS                              0/0/0  -> 0.00
  [11] REFERENCES                                   0/0/0  -> 0.00
  [12] PROPOSED WORDING                             0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.17 (fired in 1 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] REVISION HISTORY                             0/0/0  -> 0.00
  [4] INTRODUCTION                                 0/0/0  -> 0.00
  [5] MOTIVATION & SCOPE                           0/0/0  -> 0.00
  [6] STATE OF THE ART                             0/0/0  -> 0.00
  [7] IMPACT ON THE STANDARD                       1/0/0  -> 0.33
  [8] DESIGN DECISIONS                             0/0/0  -> 0.00
  [9] FUTURE DIRECTIONS                            0/0/0  -> 0.00
  [10] ACKNOWLEDGMENTS                              0/0/0  -> 0.00
  [11] REFERENCES                                   0/0/0  -> 0.00
  [12] PROPOSED WORDING                             0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): With `std::is_constant_evaluated()` it may be possible to implement the desired behaviour as a pure library extension; previously, this was not the case.

## implementation - grade 2.00  [binary: max] (fired in 1 of 12 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] REVISION HISTORY                             0/0/0  -> 0.00
  [4] INTRODUCTION                                 0/0/0  -> 0.00
  [5] MOTIVATION & SCOPE                           0/0/0  -> 0.00
  [6] STATE OF THE ART                             2/2/2  -> 2.00
  [7] IMPACT ON THE STANDARD                       0/0/0  -> 0.00
  [8] DESIGN DECISIONS                             0/0/0  -> 0.00
  [9] FUTURE DIRECTIONS                            0/0/0  -> 0.00
  [10] ACKNOWLEDGMENTS                              0/0/0  -> 0.00
  [11] REFERENCES                                   0/0/0  -> 0.00
  [12] PROPOSED WORDING                             0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): A breakdown of GCC’s current behaviour can be found here [GCC Behaviour].
