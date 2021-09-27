def solution(phone_book):
    phone_book.sort()
    
    for i in range(1, len(phone_book)):
        src = phone_book[i-1]
        if src == phone_book[i][0:len(src)]:
            return False
    return True
