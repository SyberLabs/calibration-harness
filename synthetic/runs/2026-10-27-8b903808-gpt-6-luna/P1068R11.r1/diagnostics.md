SYNTHETIC: a real paperweight run, scored against synthetic reviewer grades; its agreement numbers are no finding about paperweight.
# Diagnostics

Provisional: Heavy (10.33/14, close to Supermassive)

Provisionally addressed: 7 of 7. Provisional points: 10.33 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 10.33   corroborated 10.67   accumulate 10.83   max 11.33

## SUMMARY
grades: motivation 2.00  audience 2.00  prior_art 2.00  vehicle 1.17  coordination 0.33  insufficiency 0.83  implementation 2.00
sample agreement: 87 of 98 section-criterion pairs unanimous (89%)
single-sample totals would have been: 11.50 / 10.50 / 10.00   (all 3 samples: 10.33)
headings: h2 13
on threshold: none
splits: motivation[2] 1/1/0  audience[6] 2/0/0  prior_art[6] 2/0/0  prior_art[8] 0/0/1
        vehicle[4] 0/1/1  vehicle[5] 2/2/0  coordination[5] 2/0/0  insufficiency[4] 0/1/0
        insufficiency[7] 0/1/0  insufficiency[10] 2/0/2  implementation[4] 0/1/1
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 14 sections, strong in 5)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 1/1/0  -> 0.67
  [3] Revision history                             0/0/0  -> 0.00
  [4] Motivation and Scope                         2/2/2  -> 2.00
  [5] Libraries and other languages                2/2/2  -> 2.00
  [6] Problem description                          2/2/2  -> 2.00
  [7] New API                                      2/2/2  -> 2.00
  [8] Wording proposal                             0/0/0  -> 0.00
  [9] Past poll results                            0/0/0  -> 0.00
  [10] Design considerations                        2/2/2  -> 2.00
  [11] Implementation experience                    0/0/0  -> 0.00
  [12] Impact on the standard                       0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
  [14] Notices & Disclaimers                        0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): The C++11 random-number API is essentially a scalar one. Stateful nature and the scalar definition of underlying algorithms prevent auto-vectorization by the compiler.
candidate 2 (found by 3 of 42 passes): GNU* libstc++ library implementation has an extension, which introduces __generate() member function to all distributions (but not engines). It was added back in 2012 jointly with simd_fast_mersenne_twister_engine implementation in order to be able to benefit from simd instructions.
candidate 3 (found by 3 of 42 passes): operator() on the engine level is the key showstopper for the auto-vectorization.
candidate 4 (found by 3 of 42 passes): The following API extension is targeting to cover generation of bigger chunks of random numbers, which allows internal optimizations hidden inside implementation.

## audience - grade 2.00 (fired in 4 of 14 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] Motivation and Scope                         1/1/1  -> 1.00
  [5] Libraries and other languages                2/2/2  -> 2.00
  [6] Problem description                          2/0/0  -> 0.67
  [7] New API                                      0/0/0  -> 0.00
  [8] Wording proposal                             0/0/0  -> 0.00
  [9] Past poll results                            0/0/0  -> 0.00
  [10] Design considerations                        2/2/2  -> 2.00
  [11] Implementation experience                    0/0/0  -> 0.00
  [12] Impact on the standard                       0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
  [14] Notices & Disclaimers                        0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): Internal measurements show significant scaling over simd-size for key baseline Engines yielding a substantial performance difference on the table on modern HW architectures.
candidate 2 (found by 3 of 42 passes): GNU* libstc++ library implementation has an extension, which introduces __generate() member function to all distributions (but not engines). It was added back in 2012 jointly with simd_fast_mersenne_twister_engine implementation in order to be able to benefit from simd instructions.
candidate 3 (found by 3 of 42 passes): Our experience shows that a contiguous memory use case is the most important for this API.
candidate 4 (found by 1 of 42 passes): operator() of an Engine is (almost) always stateful with non-trivial dependencies between iterations, which prevents any auto-vectorization:

## prior_art - grade 2.00 (fired in 5 of 14 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] Motivation and Scope                         0/0/0  -> 0.00
  [5] Libraries and other languages                2/2/2  -> 2.00
  [6] Problem description                          2/0/0  -> 0.67
  [7] New API                                      0/0/0  -> 0.00
  [8] Wording proposal                             0/0/1  -> 0.33
  [9] Past poll results                            0/0/0  -> 0.00
  [10] Design considerations                        2/2/2  -> 2.00
  [11] Implementation experience                    1/1/1  -> 1.00
  [12] Impact on the standard                       0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
  [14] Notices & Disclaimers                        0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): Similar approach is implemented in Intel® C++ Compiler in the Short Vector Random Number Generator Library (see section Usage Model [2]).
candidate 2 (found by 3 of 42 passes): Proposed extensions were prototyped on godbolt: [https://godbolt.org/z/4Kzh45cE7](https://godbolt.org/z/4Kzh45cE7)
candidate 3 (found by 2 of 42 passes): Another example of implementation can be intrinsics for the Short Vector Random Number Generator Library [2], which provides an API on simd level and can be considered an example of internal implementation for proposed modifications.
candidate 4 (found by 1 of 42 passes): Intel oneMKL can be an example of the existing vectorized implementation for a variety of engines and distributions. Existing API is C [1] (and FORTRAN), but the key property which allows enabling vectorization is a vector-based interface.

## vehicle - grade 1.17 (fired in 3 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.50   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] Motivation and Scope                         0/1/1  -> 0.67
  [5] Libraries and other languages                2/2/0  -> 1.33
  [6] Problem description                          0/0/0  -> 0.00
  [7] New API                                      1/1/1  -> 1.00
  [8] Wording proposal                             0/0/0  -> 0.00
  [9] Past poll results                            0/0/0  -> 0.00
  [10] Design considerations                        0/0/0  -> 0.00
  [11] Implementation experience                    0/0/0  -> 0.00
  [12] Impact on the standard                       0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
  [14] Notices & Disclaimers                        0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): New CPO allows writing customizations primarily for generation of random numbers in chunks, which can rely on vectorization internally in implementation details.
candidate 2 (found by 2 of 42 passes): Stateful nature and the scalar definition of underlying algorithms prevent auto-vectorization by the compiler.
candidate 3 (found by 2 of 42 passes): GNU* libstc++ library implementation has an extension, which introduces __generate() member function to all distributions (but not engines). It was added back in 2012 jointly with simd_fast_mersenne_twister_engine implementation in order to be able to benefit from simd instructions.

## coordination - grade 0.33 (fired in 1 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] Motivation and Scope                         0/0/0  -> 0.00
  [5] Libraries and other languages                2/0/0  -> 0.67
  [6] Problem description                          0/0/0  -> 0.00
  [7] New API                                      0/0/0  -> 0.00
  [8] Wording proposal                             0/0/0  -> 0.00
  [9] Past poll results                            0/0/0  -> 0.00
  [10] Design considerations                        0/0/0  -> 0.00
  [11] Implementation experience                    0/0/0  -> 0.00
  [12] Impact on the standard                       0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
  [14] Notices & Disclaimers                        0/0/0  -> 0.00
candidate 1 (found by 1 of 42 passes): GNU* libstc++ library implementation has an extension, which introduces __generate() member function to all distributions (but not engines). It was added back in 2012 jointly with simd_fast_mersenne_twister_engine implementation in order to be able to benefit from simd instructions.

## insufficiency - grade 0.83 (fired in 3 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 1.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] Motivation and Scope                         0/1/0  -> 0.33
  [5] Libraries and other languages                0/0/0  -> 0.00
  [6] Problem description                          0/0/0  -> 0.00
  [7] New API                                      0/1/0  -> 0.33
  [8] Wording proposal                             0/0/0  -> 0.00
  [9] Past poll results                            0/0/0  -> 0.00
  [10] Design considerations                        2/0/2  -> 1.33
  [11] Implementation experience                    0/0/0  -> 0.00
  [12] Impact on the standard                       0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
  [14] Notices & Disclaimers                        0/0/0  -> 0.00
candidate 1 (found by 2 of 42 passes): API allows using different engines for each scalar call and thus implementation can not speculatively assume that the same engine is used further on
candidate 2 (found by 1 of 42 passes): Stateful nature and the scalar definition of underlying algorithms prevent auto-vectorization by the compiler.
candidate 3 (found by 1 of 42 passes): New CPO allows writing customizations primarily for generation of random numbers in chunks, which can rely on vectorization internally in implementation details.

## implementation - grade 2.00  [binary: max] (fired in 4 of 14 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] Motivation and Scope                         0/1/1  -> 0.67
  [5] Libraries and other languages                2/2/2  -> 2.00
  [6] Problem description                          0/0/0  -> 0.00
  [7] New API                                      0/0/0  -> 0.00
  [8] Wording proposal                             0/0/0  -> 0.00
  [9] Past poll results                            0/0/0  -> 0.00
  [10] Design considerations                        2/2/2  -> 2.00
  [11] Implementation experience                    2/2/2  -> 2.00
  [12] Impact on the standard                       0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
  [14] Notices & Disclaimers                        0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): GNU* libstc++ library implementation has an extension, which introduces __generate() member function to all distributions (but not engines). It was added back in 2012 jointly with simd_fast_mersenne_twister_engine implementation in order to be able to benefit from simd instructions.
candidate 2 (found by 3 of 42 passes): Similar approach is implemented in Intel® C++ Compiler in the Short Vector Random Number Generator Library (see section Usage Model [2).
candidate 3 (found by 3 of 42 passes): Proposed extensions were prototyped on godbolt: [https://godbolt.org/z/4Kzh45cE7](https://godbolt.org/z/4Kzh45cE7)
candidate 4 (found by 2 of 42 passes): Internal measurements show significant scaling over simd-size for key baseline Engines yielding a substantial performance difference on the table on modern HW architectures.
