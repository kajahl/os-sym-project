[<<< Back](../../readme.md)

# Comparisons in specific tests

[basic1.md](./basic1.md)

[basic2.md](./basic2.md)

[shortlong.md](./shortlong.md)

[longshort.md](./longshort.md)

[fiftyfifty.md](./fiftyfifty.md)

[divergentae.md](./divergentae.md)

[accumulatedae.md](./accumulatedae.md)

## Summary

<table border="1">
  <thead>
    <tr>
      <th rowspan="2">No.</th>
      <th rowspan="2">Test name</th>
      <th colspan="3">Execution time</th>
      <th colspan="3">Arrival time</th>
      <th colspan="3">Average waiting time</th>
    </tr>
    <tr>
      <th>Min</th>
      <th>Avg</th>
      <th>Max</th>
      <th>Min</th>
      <th>Avg</th>
      <th>Max</th>
      <th>FCFS</th>
      <th>LCFS</th>
      <th>SJF</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>basic1</td>
      <td>1</td>
      <td>3.00</td>
      <td>5</td>
      <td rowspan="7">0</td>
      <td>3.20</td>
      <td>8</td>
      <td><u>4.40</u></td>
      <td>4.60</td>
      <td><b>3.00</b></td>
    </tr>
    <tr>
      <td>2</td>
      <td>basic2</td>
      <td>2</td>
      <td>5.39</td>
      <td>9</td>
      <td>34.55</td>
      <td>69</td>
      <td><u>45.19</u></td>
      <td>47.35</td>
      <td><b>31.03</b></td>
    </tr>
    <tr>
      <td>3</td>
      <td>shortlong</td>
      <td>3</td>
      <td>9.66</td>
      <td>20</td>
      <td>15.82</td>
      <td>30</td>
      <td>288.98</td>
      <td><u>161.94</u></td>
      <td><b>150.52</b></td>
    </tr>
    <tr>
      <td>4</td>
      <td>longshort</td>
      <td>1</td>
      <td>7.18</td>
      <td>15</td>
      <td>11.12</td>
      <td>28</td>
      <td><u>101.76</u></td>
      <td>203.58</td>
      <td><b>95.08</b></td>
    </tr>
    <tr>
      <td>5</td>
      <td>fiftyfifty</td>
      <td>3</td>
      <td>8.52</td>
      <td>15</td>
      <td>12.24</td>
      <td>29</td>
      <td>206.96</td>
      <td><u>190.42</u></td>
      <td><b>136.14</b></td>
    </tr>
    <tr>
      <td>6</td>
      <td>divergentae</td>
      <td>3</td>
      <td>8.82</td>
      <td>15</td>
      <td>14.71</td>
      <td>30</td>
      <td><u>175.33</u></td>
      <td>191.53</td>
      <td><b>124.33</b></td>
    </tr>
    <tr>
      <td>7</td>
      <td>accumulatedae</td>
      <td>3</td>
      <td>4.38</td>
      <td>6</td>
      <td>13.20</td>
      <td>30</td>
      <td><u>93.68</u></td>
      <td>94.90</td>
      <td><b>84.20</b></td>
    </tr>
  </tbody>
</table>

From the above table, it is evident that the SJF algorithm is the best for all datasets generated for simulation. The other two algorithms performed either better or worse in all cases. For tests containing short execution time tasks first (test no. 4), the FCFS algorithm significantly outperformed, whereas for tests containing long execution time tasks first (test no. 3), the LCFS algorithm performed significantly better. For test sets where processes had a diverse spread of long execution time processes (short execution time processes interleaved with longer execution time processes), both algorithms yield comparable results, but generally, the FCFS algorithm gives slightly better results. Summarizing the above conclusions - a hierarchy of algorithms can be established - from best to worst: SJF, FCFS, LCFS.

# Conclusion

While conducting simulations of FCFS, LCFS, and SJF algorithms, I have come to the conclusion that the most optimal algorithm in the majority of cases is the SJF algorithm. The other two algorithms were comparable, but FCFS was slightly better. Comparing my initial impressions regarding the arrangement of algorithms in the hierarchy, they align with the obtained results. The final hierarchy of algorithms obtained, from best to worst, is as follows:

1. SJF – Shortest Job First
2. FCFS – First Come First Serve
3. LCFS – Last Come First Serve
