Candidates = []
CandidateVotes = [0, 0, 0, 0, 0]
CandidateVotesPercent = []
StudentID = [""]
Winner = ""
WinnerVotes = 0
count = 0
TutorGroup = input("Please input the name of your Tutor Group (ie. 7A): ")
while len(TutorGroup) != 2:
    TutorGroup = input("Please input a valid Tutor Group (ie. 7A): ")

Students = int(
    input("Please input the amount of students in your Tutor Group: "))
while Students < 10 or Students > 35:
    Students = int(
        input(
            "Please input a valid amount of students that are in your Tutor Group (From between 28 and 35 Students): "
        ))
        
CandidateAmount = int(
    input(
        "Please input the amount of candidates participating in the election: "
    ))
while CandidateAmount > 4:
    CandidateAmount = int(
        input(
            "Please input in a valid number of candidates who are participating in the election: "
        ))


for candidate in range(CandidateAmount):
    CandidatesChosen = input("Please input the names of the candidates: ")
    Candidates.append(CandidatesChosen)

print(
    "Hello Students, You may choose to vote for a representative or abstain your vote.\n To vote for",
    Candidates[0], ", Press 0: \n To vote for", Candidates[1],
    ", Press 1: \n To vote for", Candidates[2], ", Press 2: \n To vote for",
    Candidates[3], ", Press 3: \n And to Abstain, Press 4:")
for vote in range(Students):
    StudentIdentifier = int(
        input(
            "Hello, before we start, please input in your Student Voter Number: "
        ))
    while StudentIdentifier in StudentID:
        StudentIdentifier = int(
            input(
                "That student has already voted, please input in a Student Voter Number: "
            ))
    else:
        StudentID.append(StudentIdentifier)
        count = count + 1
        print("Vote", count, "goes towards: ")
        Votes = int(input())
        while Votes < 0 or Votes > 4:
            print("Please input a valid option (between 0 to 4): ")
            print("Vote", count, "goes towards: ")
            Votes = int(input())
        if Votes == 0:
            CandidateVotes[0] += 1
        if Votes == 1:
            CandidateVotes[1] += 1
        if Votes == 2:
            CandidateVotes[2] += 1
        if Votes == 3:
            CandidateVotes[3] += 1
        if Votes == 4:
            CandidateVotes[4] += 1
        print("TutorGroup", TutorGroup, "has submitted their votes: \n",
              Candidates[0], "has received", CandidateVotes[0], "Votes. \n",
              Candidates[1], "has received", CandidateVotes[1], "Votes. \n",
              Candidates[2], "has received", CandidateVotes[2], "Votes. \n",
              Candidates[3], "has received", CandidateVotes[3],
              "Votes. \n Finally,", CandidateVotes[4],
              "students have abstained.")

for x in range(len(Candidates)):
  if CandidateVotes[x] > WinnerVotes:
    WinnerVotes = CandidateVotes[x]
    Winner = CandidateVotes[x]
    
for x in range(len(Candidates)):

  if Winner == CandidateVotes[x]:
     WinnerName= Candidates[x]
     print("The winner of the Election is:", WinnerName, "with", WinnerVotes,"votes")

