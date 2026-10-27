SYNTHETIC: a real paperweight run, scored against synthetic reviewer grades; its agreement numbers are no finding about paperweight.
Weight: Heavy (8/14)

The paper gives a meaningful account of the problem it wants to address and situates its approach among related work and alternatives. Its case is thinnest on who would benefit, why standardization is needed rather than another route, and what implementation experience supports the idea.

- It explains that some useful patterns are cumbersome to express without the preprocessor and that making injection visible at the call site can aid understanding.
- It relates the approach to prior proposals, describing both its reliance on P1717 and differences from lazy evaluation and parametric expressions.
- It argues that the approach follows C++ name lookup rules and supports ordinary tooling, but does not establish why those qualities require standardization.
- It mentions a library’s macro-based flags API and the difficulty of some testing-framework features, but does not establish a need for coordination or show implementation experience; the paper says the idea has not been implemented or refined.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Heavy (8.00/14)

Provisionally addressed: 7 of 7. Provisional points: 8.00 of 14. Unsupported quotes rejected: 22. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.00   corroborated 8.67   accumulate 8.83   max 10.00

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 2.00  vehicle 1.00  coordination 1.00  insufficiency 0.83  implementation 0.67
sample agreement: 73 of 84 section-criterion pairs unanimous (87%)
single-sample totals would have been: 8.50 / 8.50 / 8.50   (all 3 samples: 8.00)
headings: h2 11
on threshold: coordination
splits: motivation[5] 2/0/0  prior_art[3] 1/0/0  prior_art[8] 2/1/2  vehicle[3] 0/1/0
        vehicle[5] 0/2/2  vehicle[7] 2/0/0  vehicle[10] 0/0/2  insufficiency[3] 1/0/1
        insufficiency[7] 1/0/0  insufficiency[8] 1/0/0  implementation[3] 1/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 7 of 12 sections, strong in 6)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Disclaimer                                   2/2/2  -> 2.00
  [4] Building blocks                              0/0/0  -> 0.00
  [5] Proposal: reflection/injection-based hygi... 2/0/0  -> 0.67
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

## audience - grade 0.50 (fired in 1 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
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

## prior_art - grade 2.00 (fired in 7 of 12 sections, strong in 6)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Disclaimer                                   1/0/0  -> 0.33
  [4] Building blocks                              2/2/2  -> 2.00
  [5] Proposal: reflection/injection-based hygi... 2/2/2  -> 2.00
  [6] Comparison with Parametric Expressions       2/2/2  -> 2.00
  [7] Examples                                     2/2/2  -> 2.00
  [8] Expression decomposition and Unit Test fr... 2/1/2  -> 1.67
  [9] Design points                                0/0/0  -> 0.00
  [10] Comparison of this proposal, Lazy evaluat... 2/2/2  -> 2.00
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The ideas presented in this paper rely heavily on [P1717] [5]
candidate 2 (found by 3 of 36 passes): Lazy Evaluation creates an object for every expression and might perform a call. On the other hand, a function taking a lazily evaluated parameter can be defined in a separate translation unit and may generate less code.
candidate 3 (found by 2 of 36 passes): As such, using reflection and code injection in that way can enable a form of lazy evaluation. However, `log` is expended more than it is called, which differs from [P0927][1].
candidate 4 (found by 2 of 36 passes): The facilities presented here are very similar to the Parametric Expression proposal [3], with two exceptions:

## vehicle - grade 1.00 (fired in 4 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.50   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Disclaimer                                   0/1/0  -> 0.33
  [4] Building blocks                              0/0/0  -> 0.00
  [5] Proposal: reflection/injection-based hygi... 0/2/2  -> 1.33
  [6] Comparison with Parametric Expressions       0/0/0  -> 0.00
  [7] Examples                                     2/0/0  -> 0.67
  [8] Expression decomposition and Unit Test fr... 0/0/0  -> 0.00
  [9] Design points                                0/0/0  -> 0.00
  [10] Comparison of this proposal, Lazy evaluat... 0/0/2  -> 0.67
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): Obeys the name lookup rules of C++
candidate 2 (found by 1 of 36 passes): it aims to illustrate how the reflection and code injection proposals can be leveraged to express things that can currently not be conveniently expressed without the C preprocessor.
candidate 3 (found by 1 of 36 passes): It does not present a DSL: this is regular c++ for which it is easy to provide completion and other tooling.
candidate 4 (found by 1 of 36 passes): Code Injection is not yet a mature proposal and represents a rather large body of work, that may not be standardized any time soon.

## coordination - grade 1.00 (fired in 1 of 12 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Disclaimer                                   0/0/0  -> 0.00
  [4] Building blocks                              0/0/0  -> 0.00
  [5] Proposal: reflection/injection-based hygi... 0/0/0  -> 0.00
  [6] Comparison with Parametric Expressions       0/0/0  -> 0.00
  [7] Examples                                     2/2/2  -> 2.00
  [8] Expression decomposition and Unit Test fr... 0/0/0  -> 0.00
  [9] Design points                                0/0/0  -> 0.00
  [10] Comparison of this proposal, Lazy evaluat... 0/0/0  -> 0.00
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The Abseil library has a command-line flags feature whose primary API is the `ABSL_FLAG` macro.

## insufficiency - grade 0.83 (fired in 4 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 1.17   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Disclaimer                                   1/0/1  -> 0.67
  [4] Building blocks                              0/0/0  -> 0.00
  [5] Proposal: reflection/injection-based hygi... 1/1/1  -> 1.00
  [6] Comparison with Parametric Expressions       0/0/0  -> 0.00
  [7] Examples                                     1/0/0  -> 0.33
  [8] Expression decomposition and Unit Test fr... 1/0/0  -> 0.33
  [9] Design points                                0/0/0  -> 0.00
  [10] Comparison of this proposal, Lazy evaluat... 0/0/0  -> 0.00
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Both proposal alleviate the use of a macro.
candidate 2 (found by 2 of 36 passes): it aims to illustrate how the reflection and code injection proposals can be leveraged to express things that can currently not be conveniently expressed without the C preprocessor.
candidate 3 (found by 1 of 36 passes): It does not present a DSL: this is regular c++ for which it is easy to provide completion and other tooling.
candidate 4 (found by 1 of 36 passes): Unit test frameworks usually provide features which are cumbersome to use, unless making heavy use of the pre-processor.

## implementation - grade 0.67  [binary: max] (fired in 1 of 12 sections, strong in 0)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.67   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Disclaimer                                   1/1/0  -> 0.67
  [4] Building blocks                              0/0/0  -> 0.00
  [5] Proposal: reflection/injection-based hygi... 0/0/0  -> 0.00
  [6] Comparison with Parametric Expressions       0/0/0  -> 0.00
  [7] Examples                                     0/0/0  -> 0.00
  [8] Expression decomposition and Unit Test fr... 0/0/0  -> 0.00
  [9] Design points                                0/0/0  -> 0.00
  [10] Comparison of this proposal, Lazy evaluat... 0/0/0  -> 0.00
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): it has not been implemented nor refined.
candidate 2 (found by 1 of 36 passes): This paper intends to present an idea that I had for a while so that it is on the table and can be considered along already proposed alternatives.

-->
