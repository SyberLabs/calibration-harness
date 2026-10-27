SYNTHETIC: a real paperweight run, scored against synthetic reviewer grades; its agreement numbers are no finding about paperweight.
Weight: Medium to Heavy (7/14)

The paper gives a meaningful account of why RCU matters, who may benefit from it, and how the proposal relates to prior work and alternatives. Its case is thinnest on why standardization is needed, coordination and interoperability, and why a library would not suffice; implementation experience is asserted but not substantiated.

- The paper explains RCU’s role in safe deferred reclamation and notes that such mechanisms have proved useful in other environments, even if their need often emerges only over time.
- It identifies users and deployments, including MongoDB, Facebook, and Linux, and situates the wording in earlier work and a proposed concurrency-utilities clause.
- It cites years of implementation by the authors and use in several projects, but offers little detail to substantiate that experience or explain why standardization is needed.
- It does not explain how standardization would support coordination or interoperability, or why a library would not suffice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Heavy (7.17/14, close to Medium)

Provisionally addressed: 5 of 7. Provisional points: 7.17 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.17   corroborated 6.67   accumulate 7.33   max 7.67

## SUMMARY
grades: motivation 2.00  audience 2.00  prior_art 1.67  vehicle 0.17  coordination 0.00  insufficiency 0.00  implementation 1.33
sample agreement: 58 of 63 section-criterion pairs unanimous (92%)
single-sample totals would have been: 8.50 / 6.00 / 7.00   (all 3 samples: 7.17)
headings: h2 8
on threshold: prior_art
splits: motivation[2] 2/0/2  prior_art[4] 0/1/0  prior_art[6] 2/2/0  vehicle[2] 1/0/0
        implementation[2] 2/0/2
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              2/0/2  -> 1.33
  [3] 2. History/Changes from Previous Release     0/0/0  -> 0.00
  [4] 3. Guidance to Editor                        0/0/0  -> 0.00
  [5] 4. Proposed wording                          2/2/2  -> 2.00
  [6] 5. Issues Requiring TS Implementation Exp... 2/2/2  -> 2.00
  [7] 6. Acknowledgements                          0/0/0  -> 0.00
  [8] 7. References                                0/0/0  -> 0.00
  [9] 8. Appendix                                  0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): RCU is a synchronization mechanism that can be used for linked data structures that are frequently read, but seldom updated. RCU does not provide mutual exclusion, but instead allows the user to defer specified actions to a later time.
candidate 2 (found by 3 of 27 passes): Although these have proven useful in other environments (e.g., Linux-kernel SRCU), they are rarely used and it has usually taken some years in any given environment for the need for them to arise.
candidate 3 (found by 2 of 27 passes): This is proposed wording for Read-Copy-Update [P0461], which is a technique for safe deferred resource reclamation for optimistic concurrency, useful for lock-free data structures.

## audience - grade 2.00 (fired in 2 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              2/2/2  -> 2.00
  [3] 2. History/Changes from Previous Release     0/0/0  -> 0.00
  [4] 3. Guidance to Editor                        0/0/0  -> 0.00
  [5] 4. Proposed wording                          0/0/0  -> 0.00
  [6] 5. Issues Requiring TS Implementation Exp... 2/2/2  -> 2.00
  [7] 6. Acknowledgements                          0/0/0  -> 0.00
  [8] 7. References                                0/0/0  -> 0.00
  [9] 8. Appendix                                  0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Both RCU and hazard pointers have been progressing steadily through SG1 based on years of implementation by the authors, and are in wide use in MongoDB (for Hazard Pointers), Facebook, and Linux OS (RCU).
candidate 2 (found by 3 of 27 passes): Although these have proven useful in other environments (e.g., Linux-kernel SRCU), they are rarely used and it has usually taken some years in any given environment for the need for them to arise.

## prior_art - grade 1.67 (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              2/2/2  -> 2.00
  [3] 2. History/Changes from Previous Release     0/0/0  -> 0.00
  [4] 3. Guidance to Editor                        0/1/0  -> 0.33
  [5] 4. Proposed wording                          0/0/0  -> 0.00
  [6] 5. Issues Requiring TS Implementation Exp... 2/2/0  -> 1.33
  [7] 6. Acknowledgements                          0/0/0  -> 0.00
  [8] 7. References                                0/0/0  -> 0.00
  [9] 8. Appendix                                  0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): This wording is based P0566r5, which in turn was based on that of on n4618 draft [N4618]
candidate 2 (found by 2 of 27 passes): Although these have proven useful in other environments (e.g., Linux-kernel SRCU), they are rarely used and it has usually taken some years in any given environment for the need for them to arise.
candidate 3 (found by 1 of 27 passes): As RCU (and Hazard Pointers) are related to a concurrent shared pointer, we are looking at building a new clause 33 for Concurrency Utilities Library through P0940 [P0940].

## vehicle - grade 0.17 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              1/0/0  -> 0.33
  [3] 2. History/Changes from Previous Release     0/0/0  -> 0.00
  [4] 3. Guidance to Editor                        0/0/0  -> 0.00
  [5] 4. Proposed wording                          0/0/0  -> 0.00
  [6] 5. Issues Requiring TS Implementation Exp... 0/0/0  -> 0.00
  [7] 6. Acknowledgements                          0/0/0  -> 0.00
  [8] 7. References                                0/0/0  -> 0.00
  [9] 8. Appendix                                  0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): Both RCU and hazard pointers have been progressing steadily through SG1 based on years of implementation by the authors, and are in wide use in MongoDB (for Hazard Pointers), Facebook, and Linux OS (RCU).

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

## implementation - grade 1.33  [binary: max] (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.33   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              2/0/2  -> 1.33
  [3] 2. History/Changes from Previous Release     0/0/0  -> 0.00
  [4] 3. Guidance to Editor                        0/0/0  -> 0.00
  [5] 4. Proposed wording                          0/0/0  -> 0.00
  [6] 5. Issues Requiring TS Implementation Exp... 0/0/0  -> 0.00
  [7] 6. Acknowledgements                          0/0/0  -> 0.00
  [8] 7. References                                0/0/0  -> 0.00
  [9] 8. Appendix                                  0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): Both RCU and hazard pointers have been progressing steadily through SG1 based on years of implementation by the authors, and are in wide use in MongoDB (for Hazard Pointers), Facebook, and Linux OS (RCU).

-->
