vote_num = 0


def vote():
    print("投票します")
    global vote_num
    vote_num += 1


def reset_box():
    global vote_num
    print("箱を空にします")
    vote_num = 0


def check_box():
    global vote_num
    print("票の数は{}です".format(vote_num))


vote()  # E: undefined name 'vote'
check_box()  # E: undefined name 'check_box'
vote()  # E: undefined name 'vote'
check_box()  # E: undefined name 'check_box'
for i in range(3):
    vote()  # E: undefined name 'vote'
check_box()  # E: undefined name 'check_box'
reset_box()  # E: undefined name 'reset_box'
check_box()
