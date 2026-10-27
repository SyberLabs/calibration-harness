SYNTHETIC: a real paperweight run, scored against synthetic reviewer grades; its agreement numbers are no finding about paperweight.
Weight: Heavy (8/14)

The paper gives meaningful support for the need it identifies, its comparison with alternatives, and the existence of a working implementation. Its case is thinner on who would benefit and why the facility belongs in the standard rather than a library, and it does not establish a need for coordination or interoperability.

- The paper identifies limitations in existing polymorphism mechanisms, including allocator customization and lifetime management, and explains how its approach is intended to address them.
- It compares the proposal with traditional object-oriented polymorphism and value-semantics alternatives, and reports a C++20 implementation with tests and code-generation comparisons.
- The paper asserts broad applicability and improved usability, but does not establish which users or projects are affected or why standardization is preferable to library distribution.
- It does not establish coordination or interoperability needs.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Heavy (8.33/14)

Provisionally addressed: 6 of 7. Provisional points: 8.33 of 14. Unsupported quotes rejected: 12. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.33   corroborated 9.00   accumulate 9.33   max 9.00

## SUMMARY
grades: motivation 2.00  audience 0.67  prior_art 2.00  vehicle 1.00  coordination 0.00  insufficiency 0.67  implementation 2.00
sample agreement: 50 of 56 section-criterion pairs unanimous (89%)
single-sample totals would have been: 9.00 / 8.00 / 8.50   (all 3 samples: 8.33)
headings: h2 7
on threshold: implementation
splits: motivation[8] 1/1/0  audience[3] 1/0/0  audience[4] 0/0/1  vehicle[3] 1/0/1
        insufficiency[4] 1/0/0  implementation[5] 2/2/0
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 8 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 History                                    0/0/0  -> 0.00
  [3] 2 Introduction                               2/2/2  -> 2.00
  [4] 3 Motivation and scope                       2/2/2  -> 2.00
  [5] 4 Considerations and design decisions        2/2/2  -> 2.00
  [6] 5 Technical specifications                   0/0/0  -> 0.00
  [7] 6 Acknowledgements                           0/0/0  -> 0.00
  [8] 7 Summary                                    1/1/0  -> 0.67
candidate 1 (found by 3 of 24 passes): For example, in cases where allocator customization is required for performance considerations, `std::function` and `std::any` are not supported.
candidate 2 (found by 2 of 24 passes): Since there are architecting and performance limitations in existing mechanisms of polymorphism, the "proxy" is proposed as a generic, extendable, and efficient template library solution of polymorphic programming.
candidate 3 (found by 2 of 24 passes): Lifetime management with inheritance-based polymorphism is error-prone and inflexible, while the "proxy" allows easy customization of any lifetime management strategy, including but not limited to raw pointers and various smart pointers with potentially pooled memory management.
candidate 4 (found by 2 of 24 passes): The "proxy" library is an extendable and efficient solution for polymorphism. We believe this feature will largely improve the usability of the C++ programming language, especially in large-scale programming.

## audience - grade 0.67 (fired in 3 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 History                                    0/0/0  -> 0.00
  [3] 2 Introduction                               1/0/0  -> 0.33
  [4] 3 Motivation and scope                       0/0/1  -> 0.33
  [5] 4 Considerations and design decisions        0/0/0  -> 0.00
  [6] 5 Technical specifications                   0/0/0  -> 0.00
  [7] 6 Acknowledgements                           0/0/0  -> 0.00
  [8] 7 Summary                                    1/1/1  -> 1.00
candidate 1 (found by 3 of 24 passes): We believe this feature will largely improve the usability of the C++ programming language, especially in large-scale programming.
candidate 2 (found by 1 of 24 passes): The "proxy" can be applied in almost every case that relates to virtual functions more elegantly.
candidate 3 (found by 1 of 24 passes): Polymorphism is widely required in large-scale programming to decouple components and increase extendibility at a cost of reducing runtime performance.

## prior_art - grade 2.00 (fired in 2 of 8 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 History                                    0/0/0  -> 0.00
  [3] 2 Introduction                               2/2/2  -> 2.00
  [4] 3 Motivation and scope                       0/0/0  -> 0.00
  [5] 4 Considerations and design decisions        2/2/2  -> 2.00
  [6] 5 Technical specifications                   0/0/0  -> 0.00
  [7] 6 Acknowledgements                           0/0/0  -> 0.00
  [8] 7 Summary                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): Compared with traditional OOP, the "proxy" can largely replace the existing "virtual mechanism" and have no intrusion on existing code or runtime memory layout, without reducing performance.
candidate 2 (found by 3 of 24 passes): For "100% based on value semantics", the design direction is different from the proposed "proxy" library, while the "proxy" is based on pointer semantics, as discussed in 4.1.1, value semantics has certain limitations in lifetime management.

## vehicle - grade 1.00 (fired in 4 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 History                                    0/0/0  -> 0.00
  [3] 2 Introduction                               1/0/1  -> 0.67
  [4] 3 Motivation and scope                       1/1/1  -> 1.00
  [5] 4 Considerations and design decisions        1/1/1  -> 1.00
  [6] 5 Technical specifications                   0/0/0  -> 0.00
  [7] 6 Acknowledgements                           0/0/0  -> 0.00
  [8] 7 Summary                                    1/1/1  -> 1.00
candidate 1 (found by 3 of 24 passes): Overall, inheritance-based polymorphism has limitations both in architecting and performance.
candidate 2 (found by 3 of 24 passes): Because the virtual functions can be easily implemented with the "proxy" more elegantly without performance loss, it could be largely replaced in the future.
candidate 3 (found by 3 of 24 passes): We believe this feature will largely improve the usability of the C++ programming language, especially in large-scale programming.
candidate 4 (found by 2 of 24 passes): The "proxy" is proposed as a generic, extendable, and efficient template library solution of polymorphic programming.

## coordination - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 History                                    0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Motivation and scope                       0/0/0  -> 0.00
  [5] 4 Considerations and design decisions        0/0/0  -> 0.00
  [6] 5 Technical specifications                   0/0/0  -> 0.00
  [7] 6 Acknowledgements                           0/0/0  -> 0.00
  [8] 7 Summary                                    0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.67 (fired in 2 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 History                                    0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Motivation and scope                       1/0/0  -> 0.33
  [5] 4 Considerations and design decisions        0/0/0  -> 0.00
  [6] 5 Technical specifications                   0/0/0  -> 0.00
  [7] 6 Acknowledgements                           0/0/0  -> 0.00
  [8] 7 Summary                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): Compared with traditional OOP, the "proxy" can largely replace the existing "virtual mechanism" and have no intrusion on existing code or runtime memory layout, without reducing performance.
candidate 2 (found by 1 of 24 passes): Lifetime management with inheritance-based polymorphism is error-prone and inflexible, while the "proxy" allows easy customization of any lifetime management strategy, including but not limited to raw pointers and various smart pointers with potentially pooled memory management.

## implementation - grade 2.00  [binary: max] (fired in 2 of 8 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 History                                    0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Motivation and scope                       2/2/2  -> 2.00
  [5] 4 Considerations and design decisions        2/2/0  -> 1.33
  [6] 5 Technical specifications                   0/0/0  -> 0.00
  [7] 6 Acknowledgements                           0/0/0  -> 0.00
  [8] 7 Summary                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): As proof of concept, we have implemented the technical specifications as a single-header template library, meeting the C++20 standard. The implementation, including unit tests, could be found [here](https://github.com/microsoft/proxy/tree/1.0.0).
candidate 2 (found by 1 of 24 passes): e.g., in [tests/proxy_invocation_tests.cpp](https://github.com/microsoft/proxy/blob/1.0.0/tests/proxy_invocation_tests.cpp#L25-L33):
candidate 3 (found by 1 of 24 passes): To evaluate the quality of code generation, we tried to compile the "Drawable" example from section 3 with various compilers and compare the generated assembly between the sample implementation of the "proxy" and traditional inheritance-based polymorphism.

-->
