SYNTHETIC: a real paperweight run, scored against synthetic reviewer grades; its agreement numbers are no finding about paperweight.
Weight: Medium to Heavy (7/14)

The paper gives meaningful context for the proposal, including prior work and implementation experience, but its case for standardization is much less developed. It says little about why standardization is needed, how coordination or interoperability would be served, or why a library solution would not suffice.

- The paper identifies prior work and alternatives, including its relationship to P0566R5, the planned Safe Reclamation subclause, and feedback on the `rcu_reader` interface.
- It describes years of implementation by the authors and use of RCU and hazard pointers in Linux, Facebook, and MongoDB.
- It notes that these techniques are useful but rarely used and that their need may take years to arise, without establishing why that makes standardization important.
- The paper does not establish the need for standardization, the case for coordination and interoperability, or why a library will not suffice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Medium (6.83/14, close to Heavy)

Provisionally addressed: 4 of 7. Provisional points: 6.83 of 14. Unsupported quotes rejected: 5. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.83   corroborated 6.00   accumulate 6.83   max 8.00

## SUMMARY
grades: motivation 1.17  audience 1.67  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 59 of 63 section-criterion pairs unanimous (94%)
single-sample totals would have been: 7.00 / 7.50 / 6.00   (all 3 samples: 6.83)
headings: h2 8
on threshold: motivation, audience, implementation
splits: motivation[5] 0/1/0  audience[6] 2/2/0  prior_art[4] 2/2/0  prior_art[9] 2/0/2
## END SUMMARY

## motivation - grade 1.17 (fired in 2 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. History/Changes from Previous Release     0/0/0  -> 0.00
  [4] 3. Guidance to Editor                        0/0/0  -> 0.00
  [5] 4. Proposed wording                          0/1/0  -> 0.33
  [6] 5. Issues Requiring TS Implementation Exp... 2/2/2  -> 2.00
  [7] 6. Acknowledgements                          0/0/0  -> 0.00
  [8] 7. References                                0/0/0  -> 0.00
  [9] 8. Appendix                                  0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Although these have proven useful in other environments (e.g., Linux-kernel SRCU), they are rarely used and it has usually taken some years in any given environment for the need for them to arise.
candidate 2 (found by 1 of 27 passes): RCU is a synchronization mechanism that can be used for linked data structures that are frequently read, but seldom updated.

## audience - grade 1.67 (fired in 2 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              2/2/2  -> 2.00
  [3] 2. History/Changes from Previous Release     0/0/0  -> 0.00
  [4] 3. Guidance to Editor                        0/0/0  -> 0.00
  [5] 4. Proposed wording                          0/0/0  -> 0.00
  [6] 5. Issues Requiring TS Implementation Exp... 2/2/0  -> 1.33
  [7] 6. Acknowledgements                          0/0/0  -> 0.00
  [8] 7. References                                0/0/0  -> 0.00
  [9] 8. Appendix                                  0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Both RCU and hazard pointers have been progressing steadily through SG1 based on years of implementation by the authors, and are in wide use in MongoDB (for Hazard Pointers), Facebook, and Linux OS (RCU).
candidate 2 (found by 2 of 27 passes): Although these have proven useful in other environments (e.g., Linux-kernel SRCU), they are rarely used and it has usually taken some years in any given environment for the need for them to arise.

## prior_art - grade 2.00 (fired in 4 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              2/2/2  -> 2.00
  [3] 2. History/Changes from Previous Release     0/0/0  -> 0.00
  [4] 3. Guidance to Editor                        2/2/0  -> 1.33
  [5] 4. Proposed wording                          0/0/0  -> 0.00
  [6] 5. Issues Requiring TS Implementation Exp... 2/2/2  -> 2.00
  [7] 6. Acknowledgements                          0/0/0  -> 0.00
  [8] 7. References                                0/0/0  -> 0.00
  [9] 8. Appendix                                  2/0/2  -> 1.33
candidate 1 (found by 3 of 27 passes): This paper is a successor to the RCU portion of P0566R5, in response to LEWG’s Rapperswil 2018 request that the two techniques be split into separate papers.
candidate 2 (found by 3 of 27 passes): Although these have proven useful in other environments (e.g., Linux-kernel SRCU), they are rarely used and it has usually taken some years in any given environment for the need for them to arise.
candidate 3 (found by 2 of 27 passes): In P0940, we plan to introduce subclause on Safe Reclamation which will support RCU, Hazard Pointer, as well as a other similar features. We believe that Hazard Pointers and RCU should appear in the same section.
candidate 4 (found by 2 of 27 passes): The current definition of `rcu_domain` addresses the feedback that the `rcu_reader` class not implement RAII on its own, but rather meet the requirements of `Cpp17BasicLockable` so as to leverage `lock_guard` [thread.lock.guard] and `scoped_lock` [thread.lock.scoped].

## vehicle - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. History/Changes from Previous Release     0/0/0  -> 0.00
  [4] 3. Guidance to Editor                        0/0/0  -> 0.00
  [5] 4. Proposed wording                          0/0/0  -> 0.00
  [6] 5. Issues Requiring TS Implementation Exp... 0/0/0  -> 0.00
  [7] 6. Acknowledgements                          0/0/0  -> 0.00
  [8] 7. References                                0/0/0  -> 0.00
  [9] 8. Appendix                                  0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. History/Changes from Previous Release     0/0/0  -> 0.00
  [4] 3. Guidance to Editor                        0/0/0  -> 0.00
  [5] 4. Proposed wording                          0/0/0  -> 0.00
  [6] 5. Issues Requiring TS Implementation Exp... 0/0/0  -> 0.00
  [7] 6. Acknowledgements                          0/0/0  -> 0.00
  [8] 7. References                                0/0/0  -> 0.00
  [9] 8. Appendix                                  0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. History/Changes from Previous Release     0/0/0  -> 0.00
  [4] 3. Guidance to Editor                        0/0/0  -> 0.00
  [5] 4. Proposed wording                          0/0/0  -> 0.00
  [6] 5. Issues Requiring TS Implementation Exp... 0/0/0  -> 0.00
  [7] 6. Acknowledgements                          0/0/0  -> 0.00
  [8] 7. References                                0/0/0  -> 0.00
  [9] 8. Appendix                                  0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 1 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              2/2/2  -> 2.00
  [3] 2. History/Changes from Previous Release     0/0/0  -> 0.00
  [4] 3. Guidance to Editor                        0/0/0  -> 0.00
  [5] 4. Proposed wording                          0/0/0  -> 0.00
  [6] 5. Issues Requiring TS Implementation Exp... 0/0/0  -> 0.00
  [7] 6. Acknowledgements                          0/0/0  -> 0.00
  [8] 7. References                                0/0/0  -> 0.00
  [9] 8. Appendix                                  0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Both RCU and hazard pointers have been progressing steadily through SG1 based on years of implementation by the authors, and are in wide use in MongoDB (for Hazard Pointers), Facebook, and Linux OS (RCU).

-->
