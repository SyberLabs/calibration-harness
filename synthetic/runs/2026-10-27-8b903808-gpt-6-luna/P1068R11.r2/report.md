SYNTHETIC: a real paperweight run, scored against synthetic reviewer grades; its agreement numbers are no finding about paperweight.
Weight: Heavy (11/14)

The paper makes a substantial case that the proposed API addresses a real performance need, affects existing implementations and users, and has implementation experience behind it. Its case is thinnest on why standardization is needed rather than an implementation-specific extension, and it does not establish coordination or interoperability needs.

- The paper explains how scalar, stateful random-number generation can inhibit auto-vectorization and describes the performance gains seen when generating larger chunks.
- It identifies affected implementations and use cases, discusses existing vector-based approaches and library extensions, and reports measurements, prototypes, and related implementation experience.
- The paper argues that the API’s customization mechanism can enable chunk-based generation and that scalar calls can prevent a library from assuming a consistent engine, but does not establish why this warrants standardization over an extension.
- It does not establish coordination or interoperability needs.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Heavy (10.67/14, close to Supermassive)

Provisionally addressed: 6 of 7. Provisional points: 10.67 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 10.67   corroborated 10.00   accumulate 10.83   max 11.33

## SUMMARY
grades: motivation 2.00  audience 2.00  prior_art 2.00  vehicle 1.17  coordination 0.00  insufficiency 1.50  implementation 2.00
sample agreement: 94 of 98 section-criterion pairs unanimous (96%)
single-sample totals would have been: 11.00 / 11.00 / 10.00   (all 3 samples: 10.67)
headings: h2 13
on threshold: insufficiency
splits: motivation[5] 0/2/2  prior_art[6] 0/0/2  vehicle[5] 2/2/0  insufficiency[7] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 14 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 1/1/1  -> 1.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] Motivation and Scope                         2/2/2  -> 2.00
  [5] Libraries and other languages                0/2/2  -> 1.33
  [6] Problem description                          2/2/2  -> 2.00
  [7] New API                                      2/2/2  -> 2.00
  [8] Wording proposal                             0/0/0  -> 0.00
  [9] Past poll results                            0/0/0  -> 0.00
  [10] Design considerations                        2/2/2  -> 2.00
  [11] Implementation experience                    0/0/0  -> 0.00
  [12] Impact on the standard                       0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
  [14] Notices & Disclaimers                        0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): We propose to introduce an additional API based on iterators in alignment with algorithms definition.
candidate 2 (found by 3 of 42 passes): Stateful nature and the scalar definition of underlying algorithms prevent auto-vectorization by the compiler.
candidate 3 (found by 3 of 42 passes): operator() on the engine level is the key showstopper for the auto-vectorization.
candidate 4 (found by 3 of 42 passes): The following API extension is targeting to cover generation of bigger chunks of random numbers, which allows internal optimizations hidden inside implementation.

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
candidate 2 (found by 3 of 42 passes): GNU* libstc++ library implementation has an extension, which introduces __generate() member function to all distributions (but not engines). It was added back in 2012 jointly with simd_fast_mersenne_twister_engine implementation in order to be able to benefit from simd instructions.
candidate 3 (found by 2 of 42 passes): Our experience shows that a contiguous memory use case is the most important for this API. Random access use case is possible in an unfortunate case of AOS data layout.
candidate 4 (found by 1 of 42 passes): Our experience shows that a contiguous memory use case is the most important for this API.

## prior_art - grade 2.00 (fired in 4 of 14 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 1/1/1  -> 1.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] Motivation and Scope                         0/0/0  -> 0.00
  [5] Libraries and other languages                2/2/2  -> 2.00
  [6] Problem description                          0/0/2  -> 0.67
  [7] New API                                      0/0/0  -> 0.00
  [8] Wording proposal                             0/0/0  -> 0.00
  [9] Past poll results                            0/0/0  -> 0.00
  [10] Design considerations                        2/2/2  -> 2.00
  [11] Implementation experience                    0/0/0  -> 0.00
  [12] Impact on the standard                       0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
  [14] Notices & Disclaimers                        0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): Intel oneMKL can be an example of the existing vectorized implementation for a variety of engines and distributions. Existing API is C [1] (and FORTRAN), but the key property which allows enabling vectorization is a vector-based interface.
candidate 2 (found by 3 of 42 passes): It is consistent with current approach to introduce customizable API via CPO
candidate 3 (found by 2 of 42 passes): C++11 introduced a comprehensive mechanism to manage generation of random numbers in the `&lt;random>` header file.
candidate 4 (found by 1 of 42 passes): C++11 introduced a comprehensive mechanism to manage generation of random numbers in the `<random>` header file.

## vehicle - grade 1.17 (fired in 2 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] Motivation and Scope                         0/0/0  -> 0.00
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
candidate 2 (found by 2 of 42 passes): GNU* libstc++ library implementation has an extension, which introduces __generate() member function to all distributions (but not engines). It was added back in 2012 jointly with simd_fast_mersenne_twister_engine implementation in order to be able to benefit from simd instructions.

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

## insufficiency - grade 1.50 (fired in 3 of 14 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] Motivation and Scope                         0/0/0  -> 0.00
  [5] Libraries and other languages                0/0/0  -> 0.00
  [6] Problem description                          1/1/1  -> 1.00
  [7] New API                                      0/1/0  -> 0.33
  [8] Wording proposal                             0/0/0  -> 0.00
  [9] Past poll results                            0/0/0  -> 0.00
  [10] Design considerations                        2/2/2  -> 2.00
  [11] Implementation experience                    0/0/0  -> 0.00
  [12] Impact on the standard                       0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
  [14] Notices & Disclaimers                        0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): operator() on the engine level is the key showstopper for the auto-vectorization.
candidate 2 (found by 2 of 42 passes): API allows using different engines for each scalar call and thus implementation can not speculatively assume that the same engine is used further on
candidate 3 (found by 1 of 42 passes): New CPO allows writing customizations primarily for generation of random numbers in chunks, which can rely on vectorization internally in implementation details.
candidate 4 (found by 1 of 42 passes): API allows using different engines for each scalar call and thus implementation can not speculatively assume that the same engine is used further on;

## implementation - grade 2.00  [binary: max] (fired in 4 of 14 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] Motivation and Scope                         1/1/1  -> 1.00
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
candidate 1 (found by 3 of 42 passes): Internal measurements show significant scaling over simd-size for key baseline Engines yielding a substantial performance difference on the table on modern HW architectures.
candidate 2 (found by 3 of 42 passes): GNU* libstc++ library implementation has an extension, which introduces __generate() member function to all distributions (but not engines). It was added back in 2012 jointly with simd_fast_mersenne_twister_engine implementation in order to be able to benefit from simd instructions.
candidate 3 (found by 3 of 42 passes): Similar approach is implemented in Intel® C++ Compiler in the Short Vector Random Number Generator Library (see section Usage Model [2).
candidate 4 (found by 3 of 42 passes): Proposed extensions were prototyped on godbolt: [https://godbolt.org/z/4Kzh45cE7](https://godbolt.org/z/4Kzh45cE7)

-->
