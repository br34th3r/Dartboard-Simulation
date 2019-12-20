import Dartboard, Shot

def main():
    results = []
    for i in range(1000):
        iterations = 0
        board = Dartboard.Dartboard()
        while True:
            iterations += 1
            shot = Shot.Shot(board)
            if board.isIn(shot):
                board.shrinkBoard(shot)
            else:
                break
        results.append(iterations)
    total = 0
    for val in results:
        total += val
    avg = total / len(results)
    print(avg)

if __name__ == "__main__":
    main()
