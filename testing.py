student_scores = input("Input a list of your score: ").split()
total_num_of_score = len(student_scores)

for n in range(0, total_num_of_score):
  student_scores[n] = int(student_scores[n])

total_score = 0
for score in student_scores:
  total_score += score

average_score = round(total_score / total_num_of_score)


if (average_score < 50):
  print("You do not qualify for admission")
elif (average_score >= 50) and (average_score <= 54):
  print("You are qualifed for Agricultural Science Department")
elif (average_score >= 55) and (average_score <= 60):
  print("You are qualified for either Botany or Zoology")
elif (average_score >= 61) and (average_score <= 70):
  print("You are qualified for either Computer Science, Psychology or Statistics")
elif (average_score >= 71) and (average_score <= 74):
  print("You are qualified for either Pharmacy, Physiology, Pharmacology or Nursing")
elif (average_score >= 75) and (average_score <= 79):
  print("You are qualified for either Banking and Finance, Accountancy or Insurance")
else:
  print("You are qualified for either Medicine or Law")
