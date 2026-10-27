SYNTHETIC: a real paperweight run, scored against synthetic reviewer grades; its agreement numbers are no finding about paperweight.
# Diagnostics

Provisional: Supermassive (11.17/14, close to Heavy)

Provisionally addressed: 7 of 7. Provisional points: 11.17 of 14. Unsupported quotes rejected: 20. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.17   corroborated 9.00   accumulate 12.33   max 14.00

## SUMMARY
grades: motivation 2.00  audience 1.50  prior_art 1.50  vehicle 1.50  coordination 1.50  insufficiency 1.17  implementation 2.00
sample agreement: 71 of 77 section-criterion pairs unanimous (92%)
single-sample totals would have been: 11.50 / 11.50 / 11.50   (all 3 samples: 11.17)
headings: h2 9
on threshold: audience, prior_art, vehicle, coordination, insufficiency
splits: prior_art[4] 0/2/0  prior_art[5] 0/0/2  vehicle[9] 1/0/1  coordination[9] 1/0/1
        insufficiency[2] 1/0/0  implementation[4] 2/2/1
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 11 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 Proposals  (part 1 of 2)                   2/2/2  -> 2.00
  [6] 2 Proposals  (part 2 of 2)                   0/0/0  -> 0.00
  [7] 3 Implementation Experience                  0/0/0  -> 0.00
  [8] 4 Wording Changes                            0/0/0  -> 0.00
  [9] 5 Conclusion                                 2/2/2  -> 2.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Requiring an organization to pore over all their legacy uses of `assert` to ensure that no destructive side effects occur before benefiting from a central contract-violation handler provided by C++ seems time-consuming and counterproductive.
candidate 2 (found by 2 of 33 passes): Integrating these facilities with the contract-violation handler, however, can be an incredibly useful tool for enabling a gradual migration from older facilities to the newer tools provided by the language itself.
candidate 3 (found by 2 of 33 passes): Providing the beginnings of a migration path for users of legacy assertion facilities — both `assert` and homegrown solutions — is an essential part of making early use of the Contracts facility viable for many users.
candidate 4 (found by 1 of 33 passes): Pre-existing contract-checking facilities, such as `assert`, occasionally have fundamentally different semantics and provide completely different control mechanisms for their behavior.

## audience - grade 1.50 (fired in 2 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 Proposals  (part 1 of 2)                   2/2/2  -> 2.00
  [6] 2 Proposals  (part 2 of 2)                   0/0/0  -> 0.00
  [7] 3 Implementation Experience                  0/0/0  -> 0.00
  [8] 4 Wording Changes                            0/0/0  -> 0.00
  [9] 5 Conclusion                                 1/1/1  -> 1.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Providing the beginnings of a migration path for users of legacy assertion facilities — both `assert` and homegrown solutions — is an essential part of making early use of the Contracts facility viable for many users.
candidate 2 (found by 2 of 33 passes): In our experience, the overwhelming majority of such uses of `assert` involve no side effects whatsoever.
candidate 3 (found by 1 of 33 passes): Direct use of the standard `assert` macro is commonly taught and used widely in industry for a variety of purposes. In our experience, the overwhelming majority of such uses of `assert` involve no side effects whatsoever.

## prior_art - grade 1.50 (fired in 4 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/2/0  -> 0.67
  [5] 2 Proposals  (part 1 of 2)                   0/0/2  -> 0.67
  [6] 2 Proposals  (part 2 of 2)                   0/0/0  -> 0.00
  [7] 3 Implementation Experience                  1/1/1  -> 1.00
  [8] 4 Wording Changes                            0/0/0  -> 0.00
  [9] 5 Conclusion                                 0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Pre-existing contract-checking facilities, such as `assert`, occasionally have fundamentally different semantics and provide completely different control mechanisms for their behavior.
candidate 2 (found by 3 of 33 passes): All of these changes have been implemented (but not yet made publicly available at the time of this revision) in libc++ and libstdc++, alongside the ongoing implementations of [P2900R14] in those compilers.
candidate 3 (found by 1 of 33 passes): The C++ Standard now includes a Contracts feature, first introduced in [P2900R14] and shipped in C++26. This facility is exceedingly useful for *incrementally* enhancing safety, security, and correctness in both new and legacy code.
candidate 4 (found by 1 of 33 passes): This approach achieves the goal of not allowing an exception to escape but at the cost of potentially significantly greater code-size overhead compared to a `noexcept` function that needs only to mark a stack frame as being a `noexcept` boundary.

## vehicle - grade 1.50 (fired in 3 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 Proposals  (part 1 of 2)                   2/2/2  -> 2.00
  [6] 2 Proposals  (part 2 of 2)                   0/0/0  -> 0.00
  [7] 3 Implementation Experience                  0/0/0  -> 0.00
  [8] 4 Wording Changes                            0/0/0  -> 0.00
  [9] 5 Conclusion                                 1/0/1  -> 0.67
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): Integrating these facilities with the contract-violation handler, however, can be an incredibly useful tool for enabling a gradual migration from older facilities to the newer tools provided by the language itself.
candidate 2 (found by 2 of 33 passes): One of the primary purposes of adopting a Contracts facility into the Standard in lieu of continuing to use bespoke solutions is to centralize the management, response, and mitigation approach to detected bugs in large-scale software.
candidate 3 (found by 2 of 33 passes): Providing the beginnings of a migration path for users of legacy assertion facilities — both `assert` and homegrown solutions — is an essential part of making early use of the Contracts facility viable for many users.
candidate 4 (found by 1 of 33 passes): This paper proposes both a library API to perform that integration and changes to the `assert` macro to enable its interoperability.

## coordination - grade 1.50 (fired in 3 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 Proposals  (part 1 of 2)                   2/2/2  -> 2.00
  [6] 2 Proposals  (part 2 of 2)                   0/0/0  -> 0.00
  [7] 3 Implementation Experience                  0/0/0  -> 0.00
  [8] 4 Wording Changes                            0/0/0  -> 0.00
  [9] 5 Conclusion                                 1/0/1  -> 0.67
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): This paper proposes both a library API to perform that integration and changes to the `assert` macro to enable its interoperability.
candidate 2 (found by 3 of 33 passes): By having a central and user-selectable contract-violation handler, those who assemble large programs can avoid having distinct libraries producing different bug responses that do not fit into a single and consistent diagnostic and mitigation strategy.
candidate 3 (found by 2 of 33 passes): The hooks proposed in this paper allow for such legacy facilities to live side-by-side with C++ contracts, require no major changes to legacy facilities’ existing semantics, and open the door to integration with Contracts as soon as they are available.

## insufficiency - grade 1.17 (fired in 2 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/0  -> 0.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 Proposals  (part 1 of 2)                   2/2/2  -> 2.00
  [6] 2 Proposals  (part 2 of 2)                   0/0/0  -> 0.00
  [7] 3 Implementation Experience                  0/0/0  -> 0.00
  [8] 4 Wording Changes                            0/0/0  -> 0.00
  [9] 5 Conclusion                                 0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): This approach achieves the goal of not allowing an exception to escape but at the cost of potentially significantly greater code-size overhead compared to a `noexcept` function that needs only to mark a stack frame as being a `noexcept` boundary.
candidate 2 (found by 1 of 33 passes): Pre-existing contract-checking facilities, such as `assert`, occasionally have fundamentally different semantics and provide completely different control mechanisms for their behavior.

## implementation - grade 2.00  [binary: max] (fired in 3 of 11 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               2/2/1  -> 1.67
  [5] 2 Proposals  (part 1 of 2)                   2/2/2  -> 2.00
  [6] 2 Proposals  (part 2 of 2)                   0/0/0  -> 0.00
  [7] 3 Implementation Experience                  1/1/1  -> 1.00
  [8] 4 Wording Changes                            0/0/0  -> 0.00
  [9] 5 Conclusion                                 0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Implementations have been performed in both libc++ and libstdc++, although they have not yet been updated and upstreamed as the updates to the shared Itanium ABI that those implementations will call into are still in progress.
candidate 2 (found by 3 of 33 passes): In our experience, the overwhelming majority of such uses of `assert` involve no side effects whatsoever.
candidate 3 (found by 3 of 33 passes): All of these changes have been implemented (but not yet made publicly available at the time of this revision) in libc++ and libstdc++, alongside the ongoing implementations of [P2900R14] in those compilers.
