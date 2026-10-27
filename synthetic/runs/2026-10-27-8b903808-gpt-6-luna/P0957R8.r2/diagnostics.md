SYNTHETIC: a real paperweight run, scored against synthetic reviewer grades; its agreement numbers are no finding about paperweight.
# Diagnostics

Provisional: Heavy (8.50/14)

Provisionally addressed: 7 of 7. Provisional points: 8.50 of 14. Unsupported quotes rejected: 11. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.50   corroborated 9.00   accumulate 9.33   max 9.00

## SUMMARY
grades: motivation 2.00  audience 0.67  prior_art 2.00  vehicle 1.00  coordination 0.17  insufficiency 0.67  implementation 2.00
sample agreement: 47 of 56 section-criterion pairs unanimous (84%)
single-sample totals would have been: 7.50 / 9.00 / 9.50   (all 3 samples: 8.50)
headings: h2 7
on threshold: implementation
splits: motivation[3] 1/2/1  audience[4] 0/0/1  prior_art[4] 0/2/0  vehicle[3] 1/0/0
        coordination[8] 0/1/0  insufficiency[3] 0/1/1  insufficiency[4] 0/1/0
        insufficiency[5] 0/0/2  implementation[5] 0/2/0
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 8 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 History                                    0/0/0  -> 0.00
  [3] 2 Introduction                               1/2/1  -> 1.33
  [4] 3 Motivation and scope                       2/2/2  -> 2.00
  [5] 4 Considerations and design decisions        2/2/2  -> 2.00
  [6] 5 Technical specifications                   0/0/0  -> 0.00
  [7] 6 Acknowledgements                           0/0/0  -> 0.00
  [8] 7 Summary                                    1/1/1  -> 1.00
candidate 1 (found by 3 of 24 passes): Since there are architecting and performance limitations in existing mechanisms of polymorphism, the "proxy" is proposed as a generic, extendable, and efficient template library solution of polymorphic programming.
candidate 2 (found by 3 of 24 passes): Lifetime management with inheritance-based polymorphism is error-prone and inflexible, while the "proxy" allows easy customization of any lifetime management strategy, including but not limited to raw pointers and various smart pointers with potentially pooled memory management.
candidate 3 (found by 3 of 24 passes): For example, in cases where allocator customization is required for performance considerations, `std::function` and `std::any` are not supported.
candidate 4 (found by 3 of 24 passes): The "proxy" library is an extendable and efficient solution for polymorphism. We believe this feature will largely improve the usability of the C++ programming language, especially in large-scale programming.

## audience - grade 0.67 (fired in 2 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 History                                    0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Motivation and scope                       0/0/1  -> 0.33
  [5] 4 Considerations and design decisions        0/0/0  -> 0.00
  [6] 5 Technical specifications                   0/0/0  -> 0.00
  [7] 6 Acknowledgements                           0/0/0  -> 0.00
  [8] 7 Summary                                    1/1/1  -> 1.00
candidate 1 (found by 3 of 24 passes): We believe this feature will largely improve the usability of the C++ programming language, especially in large-scale programming.
candidate 2 (found by 1 of 24 passes): Polymorphism is widely required in large-scale programming to decouple components and increase extendibility at a cost of reducing runtime performance.

## prior_art - grade 2.00 (fired in 3 of 8 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 History                                    0/0/0  -> 0.00
  [3] 2 Introduction                               2/2/2  -> 2.00
  [4] 3 Motivation and scope                       0/2/0  -> 0.67
  [5] 4 Considerations and design decisions        2/2/2  -> 2.00
  [6] 5 Technical specifications                   0/0/0  -> 0.00
  [7] 6 Acknowledgements                           0/0/0  -> 0.00
  [8] 7 Summary                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): Compared with traditional OOP, the "proxy" can largely replace the existing "virtual mechanism" and have no intrusion on existing code or runtime memory layout, without reducing performance.
candidate 2 (found by 3 of 24 passes): For "100% based on value semantics", the design direction is different from the proposed "proxy" library, while the "proxy" is based on pointer semantics, as discussed in 4.1.1, value semantics has certain limitations in lifetime management.
candidate 3 (found by 1 of 24 passes): For other standard polymorphic wrappers, implementations may support SBO, but there is no standard way to configure so far.

## vehicle - grade 1.00 (fired in 4 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 History                                    0/0/0  -> 0.00
  [3] 2 Introduction                               1/0/0  -> 0.33
  [4] 3 Motivation and scope                       1/1/1  -> 1.00
  [5] 4 Considerations and design decisions        1/1/1  -> 1.00
  [6] 5 Technical specifications                   0/0/0  -> 0.00
  [7] 6 Acknowledgements                           0/0/0  -> 0.00
  [8] 7 Summary                                    1/1/1  -> 1.00
candidate 1 (found by 3 of 24 passes): Overall, inheritance-based polymorphism has limitations both in architecting and performance.
candidate 2 (found by 3 of 24 passes): Because the virtual functions can be easily implemented with the "proxy" more elegantly without performance loss, it could be largely replaced in the future.
candidate 3 (found by 3 of 24 passes): We believe this feature will largely improve the usability of the C++ programming language, especially in large-scale programming.
candidate 4 (found by 1 of 24 passes): The "proxy" can be applied in almost every case that relates to virtual functions more elegantly.

## coordination - grade 0.17 (fired in 1 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 History                                    0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Motivation and scope                       0/0/0  -> 0.00
  [5] 4 Considerations and design decisions        0/0/0  -> 0.00
  [6] 5 Technical specifications                   0/0/0  -> 0.00
  [7] 6 Acknowledgements                           0/0/0  -> 0.00
  [8] 7 Summary                                    0/1/0  -> 0.33
candidate 1 (found by 1 of 24 passes): We believe this feature will largely improve the usability of the C++ programming language, especially in large-scale programming.

## insufficiency - grade 0.67 (fired in 3 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.83   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 History                                    0/0/0  -> 0.00
  [3] 2 Introduction                               0/1/1  -> 0.67
  [4] 3 Motivation and scope                       0/1/0  -> 0.33
  [5] 4 Considerations and design decisions        0/0/2  -> 0.67
  [6] 5 Technical specifications                   0/0/0  -> 0.00
  [7] 6 Acknowledgements                           0/0/0  -> 0.00
  [8] 7 Summary                                    0/0/0  -> 0.00
candidate 1 (found by 2 of 24 passes): Compared with traditional OOP, the "proxy" can largely replace the existing "virtual mechanism" and have no intrusion on existing code or runtime memory layout, without reducing performance.
candidate 2 (found by 1 of 24 passes): Inheritance-based polymorphism has limitations both in architecting and performance.
candidate 3 (found by 1 of 24 passes): Such limitation makes it difficult to have different lifetime management strategies at runtime without additional overhead.

## implementation - grade 2.00  [binary: max] (fired in 2 of 8 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 History                                    0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Motivation and scope                       2/2/2  -> 2.00
  [5] 4 Considerations and design decisions        0/2/0  -> 0.67
  [6] 5 Technical specifications                   0/0/0  -> 0.00
  [7] 6 Acknowledgements                           0/0/0  -> 0.00
  [8] 7 Summary                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): As proof of concept, we have implemented the technical specifications as a single-header template library, meeting the C++20 standard. The implementation, including unit tests, could be found [here](https://github.com/microsoft/proxy/tree/1.0.0).
candidate 2 (found by 1 of 24 passes): To evaluate the quality of code generation, we tried to compile the "Drawable" example from section 3 with various compilers and compare the generated assembly between the sample implementation of the "proxy" and traditional inheritance-based polymorphism.
