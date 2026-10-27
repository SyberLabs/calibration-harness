SYNTHETIC: a real paperweight run, scored against synthetic reviewer grades; its agreement numbers are no finding about paperweight.
# Diagnostics

Provisional: Medium (6.33/14, close to Heavy)

Provisionally addressed: 5 of 7. Provisional points: 6.33 of 14. Unsupported quotes rejected: 24. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.33   corroborated 6.67   accumulate 6.83   max 7.00

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 2.00  vehicle 1.00  coordination 0.00  insufficiency 0.83  implementation 0.00
sample agreement: 73 of 84 section-criterion pairs unanimous (87%)
single-sample totals would have been: 6.50 / 7.00 / 6.50   (all 3 samples: 6.33)
headings: h2 11
on threshold: none
splits: audience[3] 0/1/0  audience[8] 0/1/1  prior_art[3] 1/0/1  prior_art[8] 1/2/1
        prior_art[9] 0/0/2  vehicle[3] 1/0/0  vehicle[5] 0/0/2  vehicle[7] 2/2/0
        vehicle[10] 0/0/1  insufficiency[2] 1/1/0  insufficiency[8] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 7 of 12 sections, strong in 7)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Disclaimer                                   2/2/2  -> 2.00
  [4] Building blocks                              0/0/0  -> 0.00
  [5] Proposal: reflection/injection-based hygi... 2/2/2  -> 2.00
  [6] Comparison with Parametric Expressions       2/2/2  -> 2.00
  [7] Examples                                     2/2/2  -> 2.00
  [8] Expression decomposition and Unit Test fr... 2/2/2  -> 2.00
  [9] Design points                                2/2/2  -> 2.00
  [10] Comparison of this proposal, Lazy evaluat... 2/2/2  -> 2.00
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): it aims to illustrate how the reflection and code injection proposals can be leveraged to express things that can currently not be conveniently expressed without the C preprocessor.
candidate 2 (found by 3 of 36 passes): Purposefully, neither proposal supports partial statement or partial expression, which would hinder tooling, maintainability and diagnostics.
candidate 3 (found by 3 of 36 passes): Unit test frameworks usually provide features which are cumbersome to use, unless making heavy use of the pre-processor.
candidate 4 (found by 3 of 36 passes): In general code, injection behaves very differently than a simple call and would benefit from being visible **at call** site.

## audience - grade 0.50 (fired in 2 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.50   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Disclaimer                                   0/1/0  -> 0.33
  [4] Building blocks                              0/0/0  -> 0.00
  [5] Proposal: reflection/injection-based hygi... 0/0/0  -> 0.00
  [6] Comparison with Parametric Expressions       0/0/0  -> 0.00
  [7] Examples                                     0/0/0  -> 0.00
  [8] Expression decomposition and Unit Test fr... 0/1/1  -> 0.67
  [9] Design points                                0/0/0  -> 0.00
  [10] Comparison of this proposal, Lazy evaluat... 0/0/0  -> 0.00
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): Unit test frameworks usually provide features which are cumbersome to use, unless making heavy use of the pre-processor.
candidate 2 (found by 1 of 36 passes): it aims to illustrate how the reflection and code injection proposals can be leveraged to express things that can currently not be conveniently expressed without the C preprocessor.

## prior_art - grade 2.00 (fired in 8 of 12 sections, strong in 5)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Disclaimer                                   1/0/1  -> 0.67
  [4] Building blocks                              2/2/2  -> 2.00
  [5] Proposal: reflection/injection-based hygi... 2/2/2  -> 2.00
  [6] Comparison with Parametric Expressions       2/2/2  -> 2.00
  [7] Examples                                     2/2/2  -> 2.00
  [8] Expression decomposition and Unit Test fr... 1/2/1  -> 1.33
  [9] Design points                                0/0/2  -> 0.67
  [10] Comparison of this proposal, Lazy evaluat... 2/2/2  -> 2.00
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The ideas presented in this paper rely heavily on [P1717] [5]
candidate 2 (found by 3 of 36 passes): This implementation is incomplete compared to Abseil’s. Regardless: - It is much shorter as it does not have to deal with the idiosyncrasies of a preprocessor
candidate 3 (found by 3 of 36 passes): Unit test frameworks usually provide features which are cumbersome to use, unless making heavy use of the pre-processor.
candidate 4 (found by 3 of 36 passes): Lazy Evaluation creates an object for every expression and might perform a call. On the other hand, a function taking a lazily evaluated parameter can be defined in a separate translation unit and may generate less code.

## vehicle - grade 1.00 (fired in 4 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Disclaimer                                   1/0/0  -> 0.33
  [4] Building blocks                              0/0/0  -> 0.00
  [5] Proposal: reflection/injection-based hygi... 0/0/2  -> 0.67
  [6] Comparison with Parametric Expressions       0/0/0  -> 0.00
  [7] Examples                                     2/2/0  -> 1.33
  [8] Expression decomposition and Unit Test fr... 0/0/0  -> 0.00
  [9] Design points                                0/0/0  -> 0.00
  [10] Comparison of this proposal, Lazy evaluat... 0/0/1  -> 0.33
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): it aims to illustrate how the reflection and code injection proposals can be leveraged to express things that can currently not be conveniently expressed without the C preprocessor.
candidate 2 (found by 1 of 36 passes): And, unlike processor macros, this reflection-based solution - Obeys the name lookup rules of C++ - Obeys the scoping rules of C++ and can be declared inside a namespace or a class
candidate 3 (found by 1 of 36 passes): This alleviates the need for making it a magic function or to introduce a new language syntax.
candidate 4 (found by 1 of 36 passes): It does not present a DSL: this is regular c++ for which it is easy to provide completion and other tooling.

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

## insufficiency - grade 0.83 (fired in 3 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/0  -> 0.67
  [3] Disclaimer                                   0/0/0  -> 0.00
  [4] Building blocks                              0/0/0  -> 0.00
  [5] Proposal: reflection/injection-based hygi... 1/1/1  -> 1.00
  [6] Comparison with Parametric Expressions       0/0/0  -> 0.00
  [7] Examples                                     0/0/0  -> 0.00
  [8] Expression decomposition and Unit Test fr... 0/1/0  -> 0.33
  [9] Design points                                0/0/0  -> 0.00
  [10] Comparison of this proposal, Lazy evaluat... 0/0/0  -> 0.00
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Both proposal alleviate the use of a macro.
candidate 2 (found by 2 of 36 passes): I believe the combination of what is presented here, reflection (including reflection on attributes), reification and injection would supersede all use of macro functions.
candidate 3 (found by 1 of 36 passes): Unit test frameworks usually provide features which are cumbersome to use, unless making heavy use of the pre-processor.

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
