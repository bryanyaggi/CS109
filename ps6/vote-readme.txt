Task:
Your task is to predict the party identification of members of Congress, based on their votes on a number of issues.

Values:
Each entry is one U.S. Representative from the 98th Congress, 2nd session (1984), with their party identification and votes on 16 key issues.

There are 9 different types of votes: voted for, paired for, and announced for (these three simplified to yea = 1), voted against, paired against, and announced against (these three simplified to nay = 0), voted present, voted present to avoid conflict of interest, and did not vote or otherwise make a position known (candidates with any of of these votes have been excluded from the dataset).

Column meaning:
Column index, Issue
1. handicapped-infants
2. water-project-cost-sharing
3. adoption-of-the-budget-resolution
4. physician-fee-freeze
5. el-salvador-aid
6. religious-groups-in-schools
7. anti-satellite-test-ban
8. aid-to-nicaraguan-contras
9. mx-missile
10. immigration
11. synfuels-corporation-cutback
12. education-spending
13. superfund-right-to-sue
14. crime
15. duty-free-exports
16. export-administration-act-south-africa

Prediction:
The variable you are predicting is the party identification of the U.S. Representative: 0 = democrat, 1 = republican.

Credit:
This dataset was collected by J.C. Schlimmer and is hosted by the UCI Machine Learning Repository:
http://archive.ics.uci.edu/ml/datasets/Congressional+Voting+Records

