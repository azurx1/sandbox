#!/usr/bin/python3.11
import random
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class Vote:
    id: int
    votes: list[int]
    vote_index: int = 0
    
    def get_vote(self) -> int:
        candidate_id = self.votes[self.vote_index]
        self.vote_index += 1
        return candidate_id

@dataclass(kw_only=True)
class Candidate:
    id: int
    vote_count: int = 0
    voters: list[Vote] = field(default_factory=list)

def calc_winner(candidates: dict[int, Candidate], votes: list[Vote]) -> int:
    '''
    Iterate over all votes and calculate the winner of the elections
    '''
    votes_to_count = votes
    while len(candidates) > 1:
        calc_round(candidates, votes_to_count)
        min_candidate = None
        for candidate in candidates:
            print(f'candidate {candidate} got {candidates[candidate].vote_count/len(votes)}% of the votes')
            if candidates[candidate].vote_count/len(votes) > 0.5:
                return candidate
            if min_candidate == None or candidates[candidate].vote_count < min_candidate.vote_count:
                min_candidate = candidates[candidate]
        candidates.pop(min_candidate.id)
        print('candidate with fewer number of votes is ', min_candidate.id)
        # print(f'He had {len(min_candidate.voters)} voters: ', min_candidate.voters)
        votes_to_count = min_candidate.voters

    return -1

def calc_round(candidates: dict[int, Candidate], votes: list[Vote]) -> None:
    '''
    Count all votes a candidate got
    save who voted for him to use in later round if no winner
    '''
    for vote in votes:
        while True:
            candidate_id = vote.get_vote()
            # print('vote id ', vote.id, 'voted for ', candidate_id, f'with priority {vote.vote_index - 1}')
            if candidate_id in candidates:
                candidates[candidate_id].vote_count += 1
                candidates[candidate_id].voters.append(vote)
                break

def main() -> None:
    ''' Main function '''
    # global args
    # args = parse_args()
    CANDIDATE_NUM = 8
    candidates = {id: Candidate(id=id) for id in range(CANDIDATE_NUM)}
    VOTES_NUM = 100
    votes = [Vote(id=vote, votes = random.sample(range(CANDIDATE_NUM), CANDIDATE_NUM)) for vote in range(VOTES_NUM)]

    print(f'The winner is candidate # {calc_winner(candidates, votes)}')


if __name__ == '__main__':
    main()