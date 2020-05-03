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
