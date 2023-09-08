#!/usr/bin/python3.11

class SnakeGame:

    def __init__(self, width: int, height: int, food: list[list[int]]):
        self.snake_loc = [(0,0)]
        self.width = width
        self.height = height
        self.food = food
        self.directions_map = {'R': (0,1), 'D': (1,0), 'L': (0, -1), 'U': (-1, 0)}

    def is_new_loc_valid(self, new_head_loc):
        if new_head_loc in self.snake_loc[:-1] or \
           new_head_loc[0] < 0 or new_head_loc[0] >= self.height or \
           new_head_loc[1] < 0 or new_head_loc[1] >= self.width:
            return False
        return True

    def move(self, direction: str) -> int:
        score = len(self.snake_loc) - 1
        new_head_loc = (self.snake_loc[0][0] + self.directions_map[direction][0], 
                        self.snake_loc[0][1] + self.directions_map[direction][1])

        if not self.is_new_loc_valid(new_head_loc):
            return -1

        if score < len(self.food) and new_head_loc[0] == self.food[score][0] and new_head_loc[1] == self.food[score][1]:
            # eating the food
            self.snake_loc.insert(0, new_head_loc)
            score += 1
        else:
            # regular move no food
            self.snake_loc.insert(0, new_head_loc)
            self.snake_loc.pop(score + 1)
        
        return score

def main() -> None:
    ''' Main function '''
    game = SnakeGame(2,2,[[0,1]])
    res = []
    # ["R"],["D"],["R"],["U"],["L"],["U"]
    res.append(game.move('R'))
    res.append(game.move('D'))
    # res.append(game.move('R'))
    # res.append(game.move('U'))
    # res.append(game.move('L'))
    # res.append(game.move('U'))
    print(res)


if __name__ == '__main__':
    main()



# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)