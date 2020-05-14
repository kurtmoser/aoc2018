# Advent of Code 2018 solutions in Python

## Notes

### Day 5

Initial idea was to build single regex of aA|Aa|bB|...|Zz and use it to remove suitable pairs until polymer cannot be reduced any further. Somewhat surprisingly such regular expression is noticeably slower than performing 56 separate re.sub's with aA to Zz. In the end I chose just str.replace over regex to keep things simpler.

After reading discussions it turns out the optimal way to perform reducing the polymer is by using stack. Going through polymer step by step we check if current unit reacts with the last one in stack. If it does not then just add unit to stack. If it does then pop last unit from stack and move to the next unit in polymer. This allows reduction with a single walkthrough.

### Day 6

To detect points with infinite areas first find min/max x and y values over all the points. Then go around rectangle (min_x, min_y)(max_x, max_y) and find point each coordinate there belongs to - all points represented there have infinite areas (reaching edge of rectangle means this area cannot be "caught" by other areas any more and is expanding further to infinity).

After that we can work within rectangle (min_x, min_y)(max_x, max_y) to figure out (noninfinite) points each coordinate belongs to. Note that for part 2 working within rectangle is not enough once input distance is large.

See also: Voronoi diagram, numpy.meshgrid

### Day 7

Order for completing can be decided by building dependency list. For each step we create list of steps that it directly depends on. After that we can start construction by finding which steps don't currently depend on any other steps, complete them and remove them from other steps' dependencies.

For part 2 create new dict of workers with key representing step and value time when task gets finished. Assigns tasks to as many workers as possible at each iteration, then find which worker finishes next and reduce deps_list by its task.

Note: When we want to keep original deps of instance then self.deps_list.copy() is not enough. This creates shallow copy and all the lists in deps_list are copied by reference. Use copy module's deepcopy instead.

See also: Topological sorting, networkx.lexicographical_topological_sort, networkx.DiGraph

### Day 8

For each node the we know only starting position of its first child (or of metadata if node has no children). To get starting position of the second node we need to first recursively build all child nodes of that first child. After first child node has been built we know the exact length of it and can calculate starting position for the next one to repeat the process with it.

Metadata sums can be precalculated once during initial tree construction, but for now they have been left into their own methods doing these calculations runtime.

Thing to note about other people solutions is that several of them use input data as (reversed) stack and keep popping/discarding data from it while building nodes. There really is little point of keeping initial data list intact and this provides for some nice clean solutions.

### Day 9

Initial idea was to solve for first couple of hundred marbles using naive list building approach to see if there is any pattern in scoring (more specifically in the marbles positioned 7 spots ahead of active one during scroring round). Apparently there was none.

But naive approach using a list proved to be fast enough to solve part 1. Once part 2 increased iteration count by 100 it was clear naive approach is not enough and next idea was to replace it with linked lists. This proved to be not only fast enough to solve part 2 but also the approach that was apparently intended as majority of other people's solutions used linked lists also (some Python solvers used more specifically collections.deque)

See also: collections.deque

### Day 10

Question may be how to detect the right time moment when stars are aligned. A good candidate for this moment is when stars are closest to each-other. So lets keep moving stars forward until we reach point when area covered by stars is at its minimum.

It is likely that algorithm can be optimized by tracking single axis length change instead of area or by tracking only couple of points at the extremes.

### Day 11

Part 1 can be solved using brute force and calculating each 3x3 square's power on runtime. Due to large amount of operations part 2 requires some optimization. I took the approach of precalculating powers (with height of square size) of separate columns, this way moving from left to right we only need single addition and subtraction of column to calculate power of the next square.

Looking at other people's solutions there are even better ways to solve part 2 using partial sums etc.

Note: To initialize 2-dimensional list we cannot use *grid = [[0] * x] * y]*. Inner list will be created only once and used by reference so changing value in one row changes it in all the others also. Use *grid = [[0 for i in range(x)] for j in range(y)]* instead.

See also: Partial sums, summed-area table

### Day 12

This task is at its core just string building with the help of hashmap. Note that we cannot replace values in-place as each value depends on the ones preceding and following it and we don't want to tamper value at position i if it is being later used by i+1 and i+2. So at each iteration lets build a new plants string from scratch. As plants may spread beyond initial string boundaries we need to keep also track of evolving string's starting position (at the beginning it is 0) so that we can later calculate checksum based on plants positions correctly.

Part 2 can be solved by evolving string up to a point where we start noticing definite pattern in checksum change. After that it is a matter of simple multiplication.

### Day 13

Split carts from tracks so that we have a clean map of tracks not cluttered by carts and separate list of tracks with their x,y coords, moving speeds and state for where to turn at the next intersection.

Order by which the carts are being moved is important because when 2 carts move towards eachother and are separated by no units then the first cart to move causes collision at the position of the second cart (and not vice-versa). This also means that collisions need to be checked after every single cart move and not only once all the carts have been moved.

An interesting approach presented in solutions megathread is using complex numbers to represent positions and velocities on x,y grid. Also take note how turning becomes a simple multiplication of velocity by +1j or -1j in that case.

Note: To iterate over list indexes and values use *for i, v in enumerate(list)*

### Day 14

Both parts can be (or rather are intended to be) solved by brute force. Pay attention that at each step we add either one or two new recipes to the list (recipe sums range from 0+0=0 to 9+9=18). This means that for part 2 when growing recipes list we cannot assume that pattern we are looking for occurs exactly at the end of recipes list - if two recipes were added then pattern may also be shifted one to the left (i.e. we need to check for sublist at 2 different positions).

Slight optimization can be added by tracking whether we added one or two recipes on last iteration and avoiding second sublist check unless indeed necessary (this accounted for ~16s -> ~14s speed bump for part 2 on test machine but was left uncommited).

### Day 16

Part 1 is straightforward execution of all possible operations over each sample instruction input and comparing received output with expected one. For part 2 gather possible decoded opcode candidates for encoded opcodes over all the samples. One encoded opcode will have exactly one decoded opcode candidate. Remove this decoded opcode from every other candidates list. Another encoded opcode will now have a single candidate. Repeat until all encoded opcodes has single decoded counterpart. Now we can translate encoded opcodes of input program to decoded ones and run program. Method deduct_opcodes itself is a bit out of place for Computer class, but lets keep it there for now.

### Day 17

We need to simulate two things here: water flowing down and water spreading sideways. For first we use top-bottom approach so any water in the air expands until it reaches bucket. For second we use bottom-top approach so any water at the bottom of the buckets fills it row by row up to the top (+ one additional row of flowing water above it). Repeat these operations until nothing changes any more when water is flowing downwards - this means that we have reached bottom of our grid.

For spreading water sideways track separately towards left and right and for each side check whether we reach a wall or a bottom disappears under the water. Also if bottom disappears then mark this row of water as flowing (we differentiate between still water '~' and flowing water '|').

After initally solving using 2-dimensional list for grid, I experimented by replacing it with defaultdict but that caused program to run more than twice as slow.

### Day 18

Part 1 is implementing variation of Conway's Game of Life over small number of iterations. An interesting note from discussions was that since each state can evolve only into single next one then by using letters to indicate cell type ('o' - open ground, 't' - trees, 'l' - lumberyard) we can perform evolution in-place by swapping case for cells that are going to change. Once evolution for all cells has been calculated we move over grid and replace the ones containing uppercase values with their new states.

Since iteration count for part 2 is large, it seems reasonable to attempt to find some kind of a cycle/pattern in evolving resource values. This cycle reveals itself after ~400-500 iterations allowing us to calculate it's length. Then we can simply use modulus to figure out which value in the cycle corresponds to the 1000000000th iteration.

See also: Conway's Game of Life, Floyd's Tortoise and Hare

### Day 19

Part 1 runs in meaningful time giving us answer without problems. Part 2 is very time-consuming so solution is to decode and understand what program is doing, then calculate result via another means if possible. Inspecting part 1 we can see that it returns sum of all the prime factors of a value stored in register 2. So for part 2 figure out what is the value in register 2 and find sum of its prime factors.

### Day 21

Challenge states that we are allowed to change only register 0. This gives us a hint to observe where in the program this register is being used. It turns out it happens in a single spot where value in register 0 is compared to value in register 2. If values are equal then instruction pointer will be set to point outside program (i.e. cause program to halt). So we need to keep track of values in register 2 at the time of this comparison. First such value will be result for part 1. For part 2 lets assume that values in register 2 will start to repeat at some point and return the last value before the first repeating one.

Note: before decoding program for part 2 I ran into some performance issues and found out about PyPy project - a faster alternative to standard CPython (former uses JIT while latter is interpreter).

See also: PyPy3

### Day 22

Part 1 is straightforward - first calculate erosion level for borders, then calculate erosion levels for inner grid line by line. After that risk level is just sum erosion level mods over matrix.

Part 2 took some time to figure out what is the best approach to perform breadth first search where some steps take longer time than others (due to gear change). So for each coordinate I stored path how I got there (as a string of single char directions), but if the next move required gear change then I added to the new path not only new direction but also 7 additional characters for gear change. When simple breadth first search has new paths in queue already in shortest first order then now I needed to sort queue paths by length before picking next one.

There was another issue in part 2 I struggled with - although algorithm worked (accidentally) correctly on sample data it gave close but incorrect result on real input. Finally figured out the reason was that we cannot consider position visited simply based on coordinates. Instead we need to take into account also gear we are currently equipped with. Arriving at (x,y) with climbing gear generates different optimal path forward than arriving with torch or neither. Thus we need to rather keep track whether (x,y,gear) state has been visited and not just (x,y) position.

See also: Dijkstra's algorithm, A* search algorithm, networkx.dijkstra_path_length

### Day 24

We mostly need to be just careful to implement all the rules and calculations correctly for choosing right attackers and targets. I used single list for groups that I kept sorting to allow picking attackers in the correct order. Groups were never removed from taht list but rather ignored once their units count reached 0.

For part 2 there are couple of tricky situations that may cause the battle to remain in loop and never end: 1) last remaining groups of opposite type may be immune to each other's damage; 2) last remaining groups may have too low attack damage to cause any change in target group's units count. If these situations are being handled correctly then finding minimum necessary immune system boost is just a matter of looping the simulation with increasing boost until immune system wins.
