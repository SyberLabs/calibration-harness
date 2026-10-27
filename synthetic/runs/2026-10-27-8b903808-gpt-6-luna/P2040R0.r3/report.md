SYNTHETIC: a real paperweight run, scored against synthetic reviewer grades; its agreement numbers are no finding about paperweight.
Weight: Medium (7/14)

The paper makes a useful case that the proposed facilities could express some things that are awkward with the preprocessor, and it situates its ideas in relation to existing proposals and implementations. Its case is thinnest on who would benefit, why standardization is needed rather than relying on existing approaches, and what implementation experience supports the proposal.

- The paper explains that its examples illustrate ways to express things that are not conveniently expressed without the C preprocessor, and notes potential benefits for tooling, maintainability, and diagnostics.
- It identifies relevant prior work, including P1717, Parametric Expressions, and Abseil’s implementation, and describes how the proposal relates to them.
- It asserts that the approach could supersede macro functions and ease the use of macros, but does not establish who would use it or why standardization is necessary.
- The paper does not establish coordination with related work, why a library would not suffice, or implementation experience.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Medium (6.67/14, close to Heavy)

Provisionally addressed: 5 of 7. Provisional points: 6.67 of 14. Unsupported quotes rejected: 22. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.67   corroborated 7.00   accumulate 7.50   max 7.33

## SUMMARY
grades: motivation 2.00  audience 0.67  prior_art 2.00  vehicle 1.00  coordination 0.00  insufficiency 1.00  implementation 0.00
sample agreement: 74 of 84 section-criterion pairs unanimous (88%)
single-sample totals would have been: 6.50 / 7.00 / 7.00   (all 3 samples: 6.67)
headings: h2 11
on threshold: none
splits: motivation[5] 0/0/2  audience[2] 1/0/0  prior_art[4] 1/2/2  prior_art[9] 0/2/2
        vehicle[3] 0/0/1  vehicle[5] 1/0/0  vehicle[7] 0/2/2  vehicle[10] 0/1/1
        insufficiency[5] 1/1/0  insufficiency[6] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 7 of 12 sections, strong in 6)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Disclaimer                                   2/2/2  -> 2.00
  [4] Building blocks                              0/0/0  -> 0.00
  [5] Proposal: reflection/injection-based hygi... 0/0/2  -> 0.67
  [6] Comparison with Parametric Expressions       2/2/2  -> 2.00
  [7] Examples                                     2/2/2  -> 2.00
  [8] Expression decomposition and Unit Test fr... 2/2/2  -> 2.00
  [9] Design points                                2/2/2  -> 2.00
  [10] Comparison of this proposal, Lazy evaluat... 2/2/2  -> 2.00
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): it aims to illustrate how the reflection and code injection proposals can be leveraged to express things that can currently not be conveniently expressed without the C preprocessor.
candidate 2 (found by 3 of 36 passes): Purposefully, neither proposal supports partial statement or partial expression, which would hinder tooling, maintainability and diagnostics.
candidate 3 (found by 3 of 36 passes): It is much shorter as it does not have to deal with the idiosyncrasies of a preprocessor
candidate 4 (found by 3 of 36 passes): Unit test frameworks usually provide features which are cumbersome to use, unless making heavy use of the pre-processor.

## audience - grade 0.67 (fired in 2 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/0  -> 0.33
  [3] Disclaimer                                   0/0/0  -> 0.00
  [4] Building blocks                              0/0/0  -> 0.00
  [5] Proposal: reflection/injection-based hygi... 0/0/0  -> 0.00
  [6] Comparison with Parametric Expressions       0/0/0  -> 0.00
  [7] Examples                                     0/0/0  -> 0.00
  [8] Expression decomposition and Unit Test fr... 1/1/1  -> 1.00
  [9] Design points                                0/0/0  -> 0.00
  [10] Comparison of this proposal, Lazy evaluat... 0/0/0  -> 0.00
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Unit test frameworks usually provide features which are cumbersome to use, unless making heavy use of the pre-processor.
candidate 2 (found by 1 of 36 passes): I believe the combination of what is presented here, reflection (including reflection on attributes), reification and injection would supersede all use of macro functions.

## prior_art - grade 2.00 (fired in 7 of 12 sections, strong in 6)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Disclaimer                                   0/0/0  -> 0.00
  [4] Building blocks                              1/2/2  -> 1.67
  [5] Proposal: reflection/injection-based hygi... 2/2/2  -> 2.00
  [6] Comparison with Parametric Expressions       2/2/2  -> 2.00
  [7] Examples                                     2/2/2  -> 2.00
  [8] Expression decomposition and Unit Test fr... 2/2/2  -> 2.00
  [9] Design points                                0/2/2  -> 1.33
  [10] Comparison of this proposal, Lazy evaluat... 2/2/2  -> 2.00
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The ideas presented in this paper rely heavily on [P1717] [5]
candidate 2 (found by 3 of 36 passes): The facilities presented here are very similar to the Parametric Expression proposal [3], with two exceptions: - They are composed of features otherwise offered by reflection, reification and code injection - Both expressions and complete statements can be injected.
candidate 3 (found by 3 of 36 passes): This implementation is incomplete compared to Abseil’s. Regardless: - It is much shorter as it does not have to deal with the idiosyncrasies of a preprocessor
candidate 4 (found by 3 of 36 passes): Unit test frameworks usually provide features which are cumbersome to use, unless making heavy use of the pre-processor.

## vehicle - grade 1.00 (fired in 4 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Disclaimer                                   0/0/1  -> 0.33
  [4] Building blocks                              0/0/0  -> 0.00
  [5] Proposal: reflection/injection-based hygi... 1/0/0  -> 0.33
  [6] Comparison with Parametric Expressions       0/0/0  -> 0.00
  [7] Examples                                     0/2/2  -> 1.33
  [8] Expression decomposition and Unit Test fr... 0/0/0  -> 0.00
  [9] Design points                                0/0/0  -> 0.00
  [10] Comparison of this proposal, Lazy evaluat... 0/1/1  -> 0.67
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): It does not present a DSL: this is regular c++ for which it is easy to provide completion and other tooling.
candidate 2 (found by 2 of 36 passes): Code Injection is not yet a mature proposal and represents a rather large body of work, that may not be standardized any time soon.
candidate 3 (found by 1 of 36 passes): it aims to illustrate how the reflection and code injection proposals can be leveraged to express things that can currently not be conveniently expressed without the C preprocessor.
candidate 4 (found by 1 of 36 passes): Both proposal alleviate the use of a macro.

## coordination - grade 0.00 (fired in 0 of 12 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Disclaimer                                   0/0/0  -> 0.00
  [4] Building blocks                              0/0/0  -> 0.00
  [5] Proposal: reflection/injection-based hygi... 0/0/0  -> 0.00
  [6] Comparison with Parametric Expressions       0/0/0  -> 0.00
  [7] Examples                                     0/0/0  -> 0.00
  [8] Expression decomposition and Unit Test fr... 0/0/0  -> 0.00
  [9] Design points                                0/0/0  -> 0.00
  [10] Comparison of this proposal, Lazy evaluat... 0/0/0  -> 0.00
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 1.00 (fired in 4 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Disclaimer                                   1/1/1  -> 1.00
  [4] Building blocks                              0/0/0  -> 0.00
  [5] Proposal: reflection/injection-based hygi... 1/1/0  -> 0.67
  [6] Comparison with Parametric Expressions       0/0/1  -> 0.33
  [7] Examples                                     0/0/0  -> 0.00
  [8] Expression decomposition and Unit Test fr... 1/1/1  -> 1.00
  [9] Design points                                0/0/0  -> 0.00
  [10] Comparison of this proposal, Lazy evaluat... 0/0/0  -> 0.00
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): it aims to illustrate how the reflection and code injection proposals can be leveraged to express things that can currently not be conveniently expressed without the C preprocessor.
candidate 2 (found by 3 of 36 passes): Unit test frameworks usually provide features which are cumbersome to use, unless making heavy use of the pre-processor.
candidate 3 (found by 1 of 36 passes): And, unlike processor macros, this reflection-based solution
candidate 4 (found by 1 of 36 passes): Both proposal alleviate the use of a macro.

## implementation - grade 0.00  [binary: max] (fired in 0 of 12 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Disclaimer                                   0/0/0  -> 0.00
  [4] Building blocks                              0/0/0  -> 0.00
  [5] Proposal: reflection/injection-based hygi... 0/0/0  -> 0.00
  [6] Comparison with Parametric Expressions       0/0/0  -> 0.00
  [7] Examples                                     0/0/0  -> 0.00
  [8] Expression decomposition and Unit Test fr... 0/0/0  -> 0.00
  [9] Design points                                0/0/0  -> 0.00
  [10] Comparison of this proposal, Lazy evaluat... 0/0/0  -> 0.00
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidates: (none validated)

-->
