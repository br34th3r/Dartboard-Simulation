# Dartboard Simulation

A really interesting problem appeared to me in the form of a YouTube video a few weeks ago and I have been thinking about how to tackle it programmatically since.

Imagine you take a dartboard that is just one large bullseye. You then throw a dart at the bullseye, if it misses, you end the game, however if it hits, you take the line from the centre of the board and you draw a perpendicular chord from it, passing through the dart point, until it reaches the edge of the board, you take that chord and make the length of it the new diameter of the bullseye, and you keep going until you miss.

My goal with this project was to simulate this, and deduce the average number of shots used in a random game, assuming the overall boundaries for the shot remain the same (assuming a bounding box of the initial diameter of the board).

The video discussed is shown here: [Darts in Higher Dimensions (with 3blue1brown) - Numberphile](https://www.youtube.com/watch?v=6_yU9eJ0NxA&t=1057s)

It is definitely worth a watch, and simulating this was an interesting challenge. Please feel free to look through the code and use it to inspire you to write some of your own simulations!

(Coming soon: 3D and 4D versions of the program!)
