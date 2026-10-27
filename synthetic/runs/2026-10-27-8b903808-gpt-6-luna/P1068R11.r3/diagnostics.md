SYNTHETIC: a real paperweight run, scored against synthetic reviewer grades; its agreement numbers are no finding about paperweight.
# Diagnostics

Provisional: Heavy (9.50/14)

Provisionally addressed: 6 of 7. Provisional points: 9.50 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.50   corroborated 9.00   accumulate 10.50   max 11.00

## SUMMARY
grades: motivation 2.00  audience 2.00  prior_art 1.67  vehicle 0.83  coordination 0.00  insufficiency 1.00  implementation 2.00
sample agreement: 90 of 98 section-criterion pairs unanimous (92%)
single-sample totals would have been: 10.50 / 9.00 / 10.50   (all 3 samples: 9.50)
headings: h2 13
on threshold: prior_art, insufficiency
splits: motivation[10] 2/0/2  prior_art[2] 0/0/2  prior_art[10] 2/0/2  vehicle[4] 1/0/0
        vehicle[5] 2/0/0  vehicle[10] 0/0/2  vehicle[12] 1/0/0  implementation[4] 1/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 14 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 1/1/1  -> 1.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] Motivation and Scope                         2/2/2  -> 2.00
  [5] Libraries and other languages                2/2/2  -> 2.00
  [6] Problem description                          2/2/2  -> 2.00
  [7] New API                                      2/2/2  -> 2.00
  [8] Wording proposal                             0/0/0  -> 0.00
  [9] Past poll results                            0/0/0  -> 0.00
  [10] Design considerations                        2/0/2  -> 1.33
  [11] Implementation experience                    0/0/0  -> 0.00
  [12] Impact on the standard                       0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
  [14] Notices & Disclaimers                        0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): We propose to introduce an additional API based on iterators in alignment with algorithms definition.
candidate 2 (found by 3 of 42 passes): Stateful nature and the scalar definition of underlying algorithms prevent auto-vectorization by the compiler.
candidate 3 (found by 3 of 42 passes): GNU* libstc++ library implementation has an extension, which introduces __generate() member function to all distributions (but not engines). It was added back in 2012 jointly with simd_fast_mersenne_twister_engine implementation in order to be able to benefit from simd instructions.
candidate 4 (found by 3 of 42 passes): operator() on the engine level is the key showstopper for the auto-vectorization.

## audience - grade 2.00 (fired in 3 of 14 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] Motivation and Scope                         2/2/2  -> 2.00
  [5] Libraries and other languages                2/2/2  -> 2.00
  [6] Problem description                          0/0/0  -> 0.00
  [7] New API                                      0/0/0  -> 0.00
  [8] Wording proposal                             0/0/0  -> 0.00
  [9] Past poll results                            0/0/0  -> 0.00
  [10] Design considerations                        2/2/2  -> 2.00
  [11] Implementation experience                    0/0/0  -> 0.00
  [12] Impact on the standard                       0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
  [14] Notices & Disclaimers                        0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): Internal measurements show significant scaling over simd-size for key baseline Engines yielding a substantial performance difference on the table on modern HW architectures.
candidate 2 (found by 3 of 42 passes): Our experience shows that a contiguous memory use case is the most important for this API.
candidate 3 (found by 2 of 42 passes): GNU* libstc++ library implementation has an extension, which introduces __generate() member function to all distributions (but not engines). It was added back in 2012 jointly with simd_fast_mersenne_twister_engine implementation in order to be able to benefit from simd instructions.
candidate 4 (found by 1 of 42 passes): Intel oneMKL can be an example of the existing vectorized implementation for a variety of engines and distributions.

## prior_art - grade 1.67 (fired in 4 of 14 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/2  -> 0.67
  [3] Revision history                             0/0/0  -> 0.00
  [4] Motivation and Scope                         0/0/0  -> 0.00
  [5] Libraries and other languages                2/2/2  -> 2.00
  [6] Problem description                          1/1/1  -> 1.00
  [7] New API                                      0/0/0  -> 0.00
  [8] Wording proposal                             0/0/0  -> 0.00
  [9] Past poll results                            0/0/0  -> 0.00
  [10] Design considerations                        2/0/2  -> 1.33
  [11] Implementation experience                    0/0/0  -> 0.00
  [12] Impact on the standard                       0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
  [14] Notices & Disclaimers                        0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): Having said that, 3 main standard library implementations share the same schema, described here.
candidate 2 (found by 2 of 42 passes): Intel oneMKL can be an example of the existing vectorized implementation for a variety of engines and distributions. Existing API is C [1] (and FORTRAN), but the key property which allows enabling vectorization is a vector-based interface.
candidate 3 (found by 1 of 42 passes): We propose to introduce an additional API based on iterators in alignment with algorithms definition. simd-type based interface presented in previous paper revisions will be submitted as a separate paper.
candidate 4 (found by 1 of 42 passes): Another example of implementation can be intrinsics for the Short Vector Random Number Generator Library [2], which provides an API on simd level and can be considered an example of internal implementation for proposed modifications.

## vehicle - grade 0.83 (fired in 5 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 1.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] Motivation and Scope                         1/0/0  -> 0.33
  [5] Libraries and other languages                2/0/0  -> 0.67
  [6] Problem description                          0/0/0  -> 0.00
  [7] New API                                      1/1/1  -> 1.00
  [8] Wording proposal                             0/0/0  -> 0.00
  [9] Past poll results                            0/0/0  -> 0.00
  [10] Design considerations                        0/0/2  -> 0.67
  [11] Implementation experience                    0/0/0  -> 0.00
  [12] Impact on the standard                       1/0/0  -> 0.33
  [13] References                                   0/0/0  -> 0.00
  [14] Notices & Disclaimers                        0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): New CPO allows writing customizations primarily for generation of random numbers in chunks, which can rely on vectorization internally in implementation details.
candidate 2 (found by 1 of 42 passes): Stateful nature and the scalar definition of underlying algorithms prevent auto-vectorization by the compiler.
candidate 3 (found by 1 of 42 passes): GNU* libstc++ library implementation has an extension, which introduces __generate() member function to all distributions (but not engines). It was added back in 2012 jointly with simd_fast_mersenne_twister_engine implementation in order to be able to benefit from simd instructions.
candidate 4 (found by 1 of 42 passes): This is why the state of engines is predefined in the standard. E.g. see [rand.eng.lcong]: “The state xi of a linear_congruential_engine object x is of size 1 and consists of a single integer.”

## coordination - grade 0.00 (fired in 0 of 14 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] Motivation and Scope                         0/0/0  -> 0.00
  [5] Libraries and other languages                0/0/0  -> 0.00
  [6] Problem description                          0/0/0  -> 0.00
  [7] New API                                      0/0/0  -> 0.00
  [8] Wording proposal                             0/0/0  -> 0.00
  [9] Past poll results                            0/0/0  -> 0.00
  [10] Design considerations                        0/0/0  -> 0.00
  [11] Implementation experience                    0/0/0  -> 0.00
  [12] Impact on the standard                       0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
  [14] Notices & Disclaimers                        0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 1.00 (fired in 1 of 14 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] Motivation and Scope                         0/0/0  -> 0.00
  [5] Libraries and other languages                0/0/0  -> 0.00
  [6] Problem description                          0/0/0  -> 0.00
  [7] New API                                      0/0/0  -> 0.00
  [8] Wording proposal                             0/0/0  -> 0.00
  [9] Past poll results                            0/0/0  -> 0.00
  [10] Design considerations                        2/2/2  -> 2.00
  [11] Implementation experience                    0/0/0  -> 0.00
  [12] Impact on the standard                       0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
  [14] Notices & Disclaimers                        0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): API allows using different engines for each scalar call and thus implementation can not speculatively assume that the same engine is used further on

## implementation - grade 2.00  [binary: max] (fired in 4 of 14 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] Motivation and Scope                         1/0/1  -> 0.67
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
candidate 2 (found by 3 of 42 passes): Proposed extensions were prototyped on godbolt: [https://godbolt.org/z/4Kzh45cE7](https://godbolt.org/z/4Kzh45cE7)
candidate 3 (found by 2 of 42 passes): Internal measurements show significant scaling over simd-size for key baseline Engines yielding a substantial performance difference on the table on modern HW architectures.
candidate 4 (found by 2 of 42 passes): Our experience shows that a contiguous memory use case is the most important for this API.
