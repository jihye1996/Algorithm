from collections import defaultdict
def solution(genres, plays):
    answer = []
    genres_dict = defaultdict(list)
    play_total = defaultdict(int)
    for i in range(len(genres)):
        genres_dict[genres[i]].append((i, plays[i]))
        play_total[genres[i]] += plays[i]

    for genre, play in sorted(play_total.items(), key=lambda x: x[1], reverse=True):
        for order in sorted(genres_dict[genre], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(order[0])                               

    return answer
