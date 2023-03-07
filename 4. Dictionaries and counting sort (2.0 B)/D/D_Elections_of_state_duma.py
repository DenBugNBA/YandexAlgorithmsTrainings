if __name__ == "__main__":
    seats_in_parliament = 450

    with open("input.txt") as f:
        lines = f.readlines()

    parties = {}
    sum_votes = 0

    for line in lines:
        party_name, votes = line.rsplit(maxsplit=1)
        votes = int(votes)
        parties[party_name] = [votes, 0, 0]
        sum_votes += votes

    # первое избирательное частное - количество голосов избирателей,
    # которое необходимо набрать для получения одного места в парламенте
    first_quotient = sum_votes / seats_in_parliament

    sum_seats_given = 0

    for party_name, party_data in parties.items():
        seats_to_party = int(party_data[0] / first_quotient)
        remainder = party_data[0] % first_quotient

        parties[party_name][1] = seats_to_party
        parties[party_name][2] = remainder
        sum_seats_given += seats_to_party

    if sum_seats_given < seats_in_parliament:
        all_seats_given_flag = False
        while not all_seats_given_flag:
            for party_name, party_data in sorted(
                parties.items(), key=lambda x: (-x[1][2], x[1][0])
            ):
                parties[party_name][1] += 1
                sum_seats_given += 1
                if sum_seats_given == seats_in_parliament:
                    all_seats_given_flag = True
                    break

    for party_name, party_data in parties.items():
        print(f"{party_name} {party_data[1]}")
