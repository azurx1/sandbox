#!/usr/bin/python3.11

from voting import calc_winner, Candidate, Vote

def test_1():
    CANDIDATE_NUM = 4
    candidates = {id: Candidate(id=id) for id in range(CANDIDATE_NUM)}
    votes = [
        Vote(id=0, votes = [0,1,2,3]),
        Vote(id=1, votes = [0,1,2,3]),
        Vote(id=2, votes = [0,1,2,3]),
        Vote(id=3, votes = [0,1,2,3]),
        Vote(id=4, votes = [0,1,2,3]),
        Vote(id=5, votes = [0,1,2,3]),
        Vote(id=6, votes = [1,0,2,3]),
        Vote(id=7, votes = [1,0,2,3]),
        Vote(id=8, votes = [1,0,2,3]),
        Vote(id=9, votes = [1,0,2,3])
    ]
    assert calc_winner(candidates, votes) == 0

def test_2():
    CANDIDATE_NUM = 4
    candidates = {id: Candidate(id=id) for id in range(CANDIDATE_NUM)}
    votes = [
        Vote(id=0, votes = [0,1,2,3]),
        Vote(id=1, votes = [0,1,2,3]),
        Vote(id=2, votes = [0,1,2,3]),
        Vote(id=3, votes = [0,1,2,3]),
        Vote(id=4, votes = [2,1,0,3]),
        Vote(id=5, votes = [3,1,2,0]),
        Vote(id=6, votes = [1,0,2,3]),
        Vote(id=7, votes = [1,0,2,3]),
        Vote(id=8, votes = [1,0,2,3]),
        Vote(id=9, votes = [1,0,2,3])
    ]
    assert calc_winner(candidates, votes) == 1

def test_3():
    CANDIDATE_NUM = 4
    candidates = {id: Candidate(id=id) for id in range(CANDIDATE_NUM)}
    votes = [
        Vote(id=0, votes = [0,1,2,3]),
        Vote(id=1, votes = [0,1,2,3]),
        Vote(id=2, votes = [0,1,2,3]),
        Vote(id=3, votes = [3,1,2,0]),
        Vote(id=4, votes = [2,1,0,3]),
        Vote(id=5, votes = [3,0,2,1]),
        Vote(id=6, votes = [3,0,2,1]),
        Vote(id=7, votes = [1,0,2,3]),
        Vote(id=8, votes = [1,0,2,3]),
        Vote(id=9, votes = [1,0,2,3])
    ]
    assert calc_winner(candidates, votes) == 1