c1 = int(input())
b1 = int(input())

torches = c1
burnt = c1

if b1 != 1:
    while burnt > b1 - 1:
        new_torches = burnt // b1  # количество новых бенгальских огней
        torches += new_torches
        burnt_ost = burnt % b1  # сожженный остаток, из которого не сделали новые палочки
        burnt = new_torches + burnt_ost  # сожженные огни

    hours = torches * 2
    print(hours)
else:
    print(float('inf'))
