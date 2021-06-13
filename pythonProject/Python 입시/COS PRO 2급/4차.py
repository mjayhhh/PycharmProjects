#######################################################################################################################
# 1번
def solution(schedule):
    answer = []
    for idx, i in enumerate(schedule):
        if i == "X":
            answer.append(idx + 1)
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
schedule = ["O", "X", "X", "O", "O", "O", "X", "O", "X", "X"]
ret = solution(schedule)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

# #######################################################################################################################
# # 2번
# def func_a(passed, non_passed):
#     return ( passed > 1 and non_passed ==0 )
#
# def func_b(scores):
#     answer = 0
#     if scores[0] < 40:
#         answer += 1
#     if scores[1] < 44:
#         answer += 1
#     if scores[2] < 35:
#         answer += 1
#     return answer
#
# def func_c(scores):
#     answer = 0
#     if scores[0] >= 80:
#         answer += 1
#     if scores[1] >= 88:
#         answer += 1
#     if scores[2] >= 70:
#         answer += 1
#     return answer
#
# def solution(scores):
#     answer = 0
#     for my_score in scores:
#         passed = func_@@@(@@@)
#         non_passed = func_@@@(@@@)
#         answer += func_@@@(@@@, @@@)
#     return answer
#
# #아래는 테스트케이스 출력을 해보기 위한 코드입니다.
# scores1 = [[30, 40, 100], [97, 88, 95]]
# ret1 = solution(scores1)
#
# #[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
# print("solution 함수의 반환 값은", ret1, "입니다.")
#
# scores2 = [[90, 88, 70], [85, 90, 90], [100, 100, 70], [30, 90, 80], [40, 10, 20], [83, 88, 80]]
# ret2 = solution(scores2)
#
# #[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
# print("solution 함수의 반환 값은", ret2, "입니다.")
#
# #######################################################################################################################
# # 3번
# def func_a(bundle, start):
#     return bundle[start::2]
#
# def func_b(score1, score2):
#     if score1 > score2:
#         return [1, score1]
#     elif score2 > score1:
#         return [2, score2]
#     else:
#         return [0, score1]
#
# def func_c(bundle):
#     answer = 0
#     score_per_cards = {
#         'a': 1,
#         'b': 2,
#         'c': 3,
#         'd': 4,
#         'e': 5
#     }
#     for card in bundle:
#         answer += score_per_cards[card]
#     return answer
#
# def solution(n, bundle):
#     a_cards = func_a( @ @ @,
#
#     @ @ @
#
#     )[: n]
#     b_cards = func_a( @ @ @,
#
#     @ @ @
#
#     )[: n]
#     a_score = func_c( @ @ @)
#     b_score = func_c( @ @ @)
#     return func_b( @ @ @,
#
#     @ @ @
#
#     )
#
#     # 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
#     n = 4
#     bundle = "cacdbdedccbb"
#     ret = solution(n, bundle)
#
#     # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
#     print("solution 함수의 반환 값은", ret, "입니다.")
#
# #######################################################################################################################
# # 4번
# def solution(classes, m):
#     answer = 0
#     for students in classes:
#         answer += students @@@ m
#         if students @@@ m != 0:
#             answer += 1
#     return answer
#
# # 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
# classes = [80, 45, 33, 20]
# m = 30
# ret = solution(classes, m)
#
# # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
# print("solution 함수의 반환 값은", ret, "입니다.")
#
# #######################################################################################################################
# # 5번
# def solution(calorie):
#     min_cal = 0
#     answer = 0
#     for cal in calorie:
#         if cal > min_cal:
#             answer += cal - min_cal
#         min_cal = min(min_cal, cal)
#     return answer
#
# # 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니, 위의 코드만 수정하세요.
# calorie = [713, 665, 873, 500, 751]
# ret = solution(calorie)
#
# # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
# print("solution 함수의 반환 값은", ret, "입니다.")
#
# #######################################################################################################################
# # 6번
# def solution(point):
#     if point < 1000:
#         return 0
#     return point * 100 // 100
#
# # 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니, 위의 코드만 수정하세요.
# point = 2323
# ret = solution(point)
#
# # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
# print("solution 함수의 반환 값은", ret, "입니다.")
#
# #######################################################################################################################
# # 7번
# def func_a(scores1, scores2):
#     answer = 0
#     for score1, score2 in zip(scores1, scores2):
#         answer = max(answer, score2 - score1)
#     return answer
#
#
# def func_b(scores1, scores2):
#     answer = 0
#     for score1, score2 in zip(scores1, scores2):
#         answer = min(answer, score1 - score2)
#     return answer
#
#
# def solution(mid_scores, final_scores):
#     up = func_a(mid_scores, final_scores)
#     down = func_b(mid_scores, final_scores)
#     answer = [up, down]
#     return answer
#
#
# # 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니, 위의 코드만 수정하세요.
# mid_scores = [20, 50, 40]
# final_scores = [10, 50, 70]
# ret = solution(mid_scores, final_scores)
#
# # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
# print("solution 함수의 반환 값은", ret, "입니다.")
#
# #######################################################################################################################
# # 8번
# def solution(n, votes):
#     arr = [0] * (n + 1)
#     for vote in votes:
#         arr[vote] += 1
#
#     for i in range(1, n+1):
#         if arr[i] > n/2:
#             return i
#     return -1
#
# # 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니, 위의 코드만 수정하세요.
# n1 = 3
# votes1 = [1, 2, 1, 3, 1, 2, 1]
# ret1 = solution(n1, votes1)
#
# # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
# print("solution 함수의 반환 값은 ", ret1, " 입니다.")
#
# n2 = 2
# votes2 = [2, 1, 2, 1, 2, 2, 1]
# ret2 = solution(n2, votes2)
#
# # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
# print("solution 함수의 반환 값은 ", ret2, " 입니다.")
# #######################################################################################################################
# # 9번
# #다음과 같이 import를 사용할 수 있습니다.
# #import math
#
# def solution(height):
#     #여기에 코드를 작성해주세요.
#     count = 0
#     return count
#
# #아래는 테스트케이스 출력을 해보기 위한 코드입니다.
# height = [[3, 6, 2, 8], [7, 3, 4, 2], [8, 6, 7, 3], [5, 3, 2, 9]]
# ret = solution(height)
#
# #[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
# print("solution 함수의 반환 값은", ret, "입니다.")
# #######################################################################################################################
# # 10번
# # 다음과 같이 import를 사용할 수 있습니다.
# # import math
#
# def solution(scores, cutline):
#     # 여기에 코드를 작성해주세요.
#     answer = 0
#     return answer
#
# # 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
# scores = [80, 90, 55, 60, 59]
# cutline = 60
# ret = solution(scores, cutline)
#
# #[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
# print("solution 함수의 반환 값은", ret, "입니다.")