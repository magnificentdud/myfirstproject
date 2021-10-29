number, n = map(int, input().split())
ans = 0

for i in range(1, n+1):
    gugudan = number*i

    if gugudan >= 10:
        gugudan = list(str(gugudan))
        gugudan.reverse()

        newdigit = ""
        for digit in gugudan:
            newdigit += digit
        newdigit = int(newdigit)
    else:
        newdigit = gugudan
    if newdigit > ans:
        ans = newdigit
print(ans)



        