[<<< Back](../../readme.md)

# Comparisons in specific tests

[basic1.md](./basic1.md)

[basic2.md](./basic2.md)

[random.md](./random.md)

[game.md](./game.md)

[interleavedratio11.md](./interleavedratio11.md)

[interleavedratio12.md](./interleavedratio12.md)

[interleaved.md](./interleaved.md)

[interleavedmoreoften.md](./interleavedmoreoften.md)

[interleavedplus.md](./interleavedplus.md)

## Summary

<table border="1">
  <thead>
    <tr>
      <th>Test name</th>
      <th>Memory size</th>
      <th>Unique pages count</th>
      <th>Queue length</th>
      <th>Error count FIFO</th>
      <th>Error count LRU</th>
      <th>Error count LFU</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>basic1</td>
      <td>3</td>
      <td>4</td>
      <td>20</td>
      <td><b>7</b></td>
      <td>14</td>
      <td>9</td>
    </tr>
    <tr>
      <td>basic2</td>
      <td>3</td>
      <td>5</td>
      <td>25</td>
      <td>20</td>
      <td>19</td>
      <td><b>14</b></td>
    </tr>
    <tr>
      <td>random</td>
      <td>16</td>
      <td>32</td>
      <td>1024</td>
      <td>356</td>
      <td>356</td>
      <td><b>337</b></td>
    </tr>
    <tr>
      <td>game</td>
      <td>16</td>
      <td>32</td>
      <td>512</td>
      <td>56</td>
      <td><b>52</b></td>
      <td>120</td>
    </tr>
    <tr>
      <td>interleavedratio11</td>
      <td>16</td>
      <td>24</td>
      <td>256</td>
      <td>48</td>
      <td><b>46</b></td>
      <td>92</td>
    </tr>
    <tr>
      <td>interleavedratio12</td>
      <td>16</td>
      <td>24</td>
      <td>384</td>
      <td><b>47</b></td>
      <td><b>47</b></td>
      <td>131</td>
    </tr>
    <tr>
      <td>interleaved</td>
      <td>16</td>
      <td>24</td>
      <td>533</td>
      <td>88</td>
      <td>76</td>
      <td><b>48</b></td>
    </tr>
    <tr>
      <td>interleavedmoreoften</td>
      <td>16</td>
      <td>24</td>
      <td>554</td>
      <td>136</td>
      <td>100</td>
      <td><b>83</b></td>
    </tr>
    <tr>
      <td>interleavedplus</td>
      <td>16</td>
      <td>24</td>
      <td>690</td>
      <td>136</td>
      <td><b>126</b></td>
      <td>152</td>
    </tr>
  </tbody>
</table>

From the above table, it is not unequivocally clear which page replacement algorithm is the best - we need to consider it on a case-by-case basis.

For the random test scenario - despite a slightly better result in favor of the LFU algorithm, none of them stands out with better performance compared to the other algorithms - we need to move on to more complex situations than random accesses.

For the "game simulation" - LRU and FIFO algorithms significantly outperform the LFU algorithm. This is because when transitioning from memory pages for the game to memory pages corresponding to other applications, the memory is "clogged" by game requests, which, due to intensive usage (of the game) pages (in the LFU approach, pages have much higher usage counts than freshly used memory pages of other applications). Hence, LFU for this case is the worst possible (among the available) algorithm to choose.

For interleaved requests in ratios of 1:1 and 1:2 - Similarly to the above case, LFU performs the worst compared to the other two algorithms. The difference of about 40 errors for LFU in both test cases results from this proportion (1:1, and 1:2) - memory is always initially filled with requests from the first application, and requests from the second application continuously generate errors because they are constantly being removed due to the lowest usage counter.

For the group of the first two of three test cases from the "interleaved..." without "ratio" group - the LFU algorithm turned out to be the best. This test case is ideal for this algorithm because we mainly operate consistently on the same pages - the memory is filled, but we occasionally request other pages - and it is these that generate errors. This is evident in the difference in errors for these two tests - a difference of 30 errors, resulting from the fact that previously unused random pages were added more frequently. For the last test in this group, LFU's result is not as divergent from the rest, it loses its advantage slightly in favor of LRU.

The results of the FIFO algorithm generally do not differ significantly from the results of the LRU algorithm, but the argument for the advantage of LRU is that it removes the least recently used memory page, whereas in the case of FIFO - randomly.

Summing up all the test cases and the above argument, I believe that the best algorithm is LRU, the second one - due to randomness - is FIFO, and the worst one is LFU because it fills up the memory in most cases.

# Conclusion

Conducting simulations of FIFO, LRU, and LFU algorithms, I have concluded that the LFU algorithm was the least optimal among the tested algorithms due to its effectiveness in few, extreme cases. The other two algorithms - FIFO and LRU - proved to be significantly better than LFU, often yielding comparable results, but with a slight advantage towards LRU. This difference arises from the fact that FIFO operates somewhat blindly, whereas LRU actually removes the memory page that has been least used. In this case, contrary to CPU scheduling algorithms, my initial impression regarding the arrangement of algorithms in the hierarchy was completely different from the results obtained. Initially, I assumed that LFU and LRU would be comparable, and FIFO would be the worst due to its randomness.

The final hierarchy of algorithms obtained, from best to worst:

1. LRU - Least Recently Used
2. FIFO - First In First Out
3. LFU - Least Frequently Used
