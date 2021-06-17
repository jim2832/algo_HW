def available_seats(seats):
    count = 0
    seats.insert(0,0)
    seats.insert(len(seats),0)
    for i in range(len(seats) - 1):
        if seats[i] == 0 and seats[i+1] == 0:
            count = count + 1
            seats[i+1] = 1
    return count

seats = [1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0]
print(available_seats(seats))

#[1,0,0,0,0,1] > 1  
# a[3] || a[4]

#[0,1,0,0,1,0,1] > 0 
# no available

#[0,0,0,1,0,1,0,0] > 2
# a[1] || a[2] + a[8]

#[1,0,0,0,1,0,0,0,0] > 3
# a[3] + a[7] + a[9]