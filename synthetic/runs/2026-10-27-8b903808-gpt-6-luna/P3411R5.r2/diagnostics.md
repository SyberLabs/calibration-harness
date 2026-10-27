SYNTHETIC: a real paperweight run, scored against synthetic reviewer grades; its agreement numbers are no finding about paperweight.
# Diagnostics

Provisional: Heavy (9.83/14)

Provisionally addressed: 7 of 7. Provisional points: 9.83 of 14. Unsupported quotes rejected: 12. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.83   corroborated 10.00   accumulate 10.33   max 12.33

## SUMMARY
grades: motivation 2.00  audience 1.33  prior_art 2.00  vehicle 1.00  coordination 1.00  insufficiency 0.50  implementation 2.00
sample agreement: 73 of 77 section-criterion pairs unanimous (95%)
single-sample totals would have been: 10.50 / 10.00 / 10.00   (all 3 samples: 9.83)
headings: h2 10
on threshold: vehicle, coordination
splits: motivation[3] 1/2/1  audience[7] 2/2/0  audience[8] 2/0/2  prior_art[5] 2/0/2
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 11 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   1/2/1  -> 1.33
  [4] 3 Motivation                                 2/2/2  -> 2.00
  [5] 4 Design Space and Prior Art                 2/2/2  -> 2.00
  [6] 5 Proposed Design                            0/0/0  -> 0.00
  [7] 6 Alternative Design for Template Parameters 2/2/2  -> 2.00
  [8] 7 Other Design Considerations                2/2/2  -> 2.00
  [9] 8 Implementation Experience                  0/0/0  -> 0.00
  [10] 9 Wording                                    0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): In large applications, such liberal use of `std::ranges` can lead to increased header dependencies and often a significant compilation time penalty.
candidate 2 (found by 3 of 33 passes): We can easily get a combinatorial explosion of types if we follow the same approach we did for `std::function`.
candidate 3 (found by 3 of 33 passes): And in most of cases, the implementation of `algo` only iterate over the range once. The design should make it easy to specify an “`input_range` only” `view`, and sometimes “read-only” access to the elements (a `const` reference element type).
candidate 4 (found by 3 of 33 passes): Due to the lack of type erasure utilities, typically the API takes a `vector`, even though the implementation only needs to iterate once over the elements.

## audience - grade 1.33 (fired in 3 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.83   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 1/1/1  -> 1.00
  [5] 4 Design Space and Prior Art                 0/0/0  -> 0.00
  [6] 5 Proposed Design                            0/0/0  -> 0.00
  [7] 6 Alternative Design for Template Parameters 2/2/0  -> 1.33
  [8] 7 Other Design Considerations                2/0/2  -> 1.33
  [9] 8 Implementation Experience                  0/0/0  -> 0.00
  [10] 9 Wording                                    0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): In large applications, such liberal use of `std::ranges` can lead to increased header dependencies and often a significant compilation time penalty.
candidate 2 (found by 2 of 33 passes): | Option | Approval votes |
candidate 3 (found by 1 of 33 passes): In our benchmark, 10% of the `Widget`s were filtered out by the filter pipeline and the `name` string’s length is randomly 0-30.
candidate 4 (found by 1 of 33 passes): We maintain that this code pattern is very common in the wild: making the code simple and clean at the cost of copying data, even though most of the callers don’t actually need a copy of the data at all.

## prior_art - grade 2.00 (fired in 4 of 11 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 2/2/2  -> 2.00
  [5] 4 Design Space and Prior Art                 2/0/2  -> 1.33
  [6] 5 Proposed Design                            0/0/0  -> 0.00
  [7] 6 Alternative Design for Template Parameters 2/2/2  -> 2.00
  [8] 7 Other Design Considerations                0/0/0  -> 0.00
  [9] 8 Implementation Experience                  2/2/2  -> 2.00
  [10] 9 Wording                                    0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): `std::span<T>` is another type-erasure utility recently added to the standard; and is closely related to ranges in fact, by allowing type-erased *reference* of any underlying *contiguous* range of objects.
candidate 2 (found by 3 of 33 passes): However, we believe that this overcomplicates the design.
candidate 3 (found by 2 of 33 passes): Users will need to provide `range_reference_t`, `range_value_t` and `range_difference_t`. `Traversal` is equivalent to `iterator_concept`, which decides the traversal category of the range.
candidate 4 (found by 2 of 33 passes): `any_view` has been implemented in [[range-v3]](https://github.com/ericniebler/range-v3), with equivalent semantics as proposed here. The authors also implemented a version that directly follows the proposed wording below without any issue [[ours]](https://github.com/huixie90/cpp_papers/tree/main/impl/any_view) and [[beman-project]](https://github.com/bemanproject/any_view).

## vehicle - grade 1.00 (fired in 1 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 2/2/2  -> 2.00
  [5] 4 Design Space and Prior Art                 0/0/0  -> 0.00
  [6] 5 Proposed Design                            0/0/0  -> 0.00
  [7] 6 Alternative Design for Template Parameters 0/0/0  -> 0.00
  [8] 7 Other Design Considerations                0/0/0  -> 0.00
  [9] 8 Implementation Experience                  0/0/0  -> 0.00
  [10] 9 Wording                                    0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): In large applications, such liberal use of `std::ranges` can lead to increased header dependencies and often a significant compilation time penalty.

## coordination - grade 1.00 (fired in 1 of 11 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 Design Space and Prior Art                 0/0/0  -> 0.00
  [6] 5 Proposed Design                            0/0/0  -> 0.00
  [7] 6 Alternative Design for Template Parameters 0/0/0  -> 0.00
  [8] 7 Other Design Considerations                2/2/2  -> 2.00
  [9] 8 Implementation Experience                  0/0/0  -> 0.00
  [10] 9 Wording                                    0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): As a type intended to exist at ABI boundaries, ensuring the ABI stability of `any_view` is extremely important.
candidate 2 (found by 1 of 33 passes): As a result, most people would instead copy the results of the pipeline into a container and return that from `getWidgetNames()`, for example as a `std::vector<std::string>`.

## insufficiency - grade 0.50 (fired in 1 of 11 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 1/1/1  -> 1.00
  [5] 4 Design Space and Prior Art                 0/0/0  -> 0.00
  [6] 5 Proposed Design                            0/0/0  -> 0.00
  [7] 6 Alternative Design for Template Parameters 0/0/0  -> 0.00
  [8] 7 Other Design Considerations                0/0/0  -> 0.00
  [9] 8 Implementation Experience                  0/0/0  -> 0.00
  [10] 9 Wording                                    0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Attempts to separate the implementation into its own translation unit, as is a common practice for non-templated code, are futile in this situation.

## implementation - grade 2.00  [binary: max] (fired in 3 of 11 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 Design Space and Prior Art                 0/0/0  -> 0.00
  [6] 5 Proposed Design                            0/0/0  -> 0.00
  [7] 6 Alternative Design for Template Parameters 2/2/2  -> 2.00
  [8] 7 Other Design Considerations                2/2/2  -> 2.00
  [9] 8 Implementation Experience                  2/2/2  -> 2.00
  [10] 9 Wording                                    0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): An implementation of this approach would look like this: [link](https://godbolt.org/z/qdnoE7Mb9)
candidate 2 (found by 3 of 33 passes): The following benchmarks were compiled with clang 20 with libc++, with -O3, run on APPLE M4 MAX CPU with 16 cores. We have done the same benchmarks on a 8 core Intel CPU and they have very similar results.
candidate 3 (found by 3 of 33 passes): `any_view` has been implemented in [[range-v3]](https://github.com/ericniebler/range-v3), with equivalent semantics as proposed here. The authors also implemented a version that directly follows the proposed wording below without any issue [[ours]](https://github.com/huixie90/cpp_papers/tree/main/impl/any_view) and [[beman-project]](https://github.com/bemanproject/any_view).
