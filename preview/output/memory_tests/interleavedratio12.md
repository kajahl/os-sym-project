[Back to summary](./readme.md)

# Test Interleaved programs - Ratio 1:2
## Test description
Programs running simultaneously in rotation with 12 unique pages each, process queue 64 : 128 (A single program cannot fill the entire memory 12/16) [Memory size: 16, Unique pages: 24, Queue length: 384]
## Input data
- Memory size: 16
- Number of unique pages: 24
- Queue: [9, 9, 11, 2, 2, 10, 7, 4, 3, 9, 1, 7, 2, 5, 11, 3, 7, 1, 7, 10, 12, 9, 9, 12, 9, 10, 2, 10, 11, 10, 5, 5, 1, 11, 6, 2, 10, 2, 7, 1, 7, 4, 4, 5, 12, 11, 10, 9, 5, 1, 7, 12, 10, 7, 4, 2, 1, 12, 10, 12, 12, 6, 12, 9, 15, 19, 24, 20, 16, 15, 24, 21, 14, 14, 15, 19, 20, 17, 20, 17, 13, 19, 18, 20, 14, 17, 21, 23, 15, 16, 24, 19, 19, 14, 19, 13, 18, 17, 15, 19, 19, 16, 21, 20, 21, 16, 13, 17, 22, 17, 16, 15, 16, 15, 23, 23, 23, 22, 23, 23, 14, 13, 19, 23, 21, 17, 19, 21, 15, 20, 18, 18, 23, 19, 13, 14, 19, 24, 23, 20, 21, 16, 16, 16, 15, 16, 19, 19, 23, 18, 13, 13, 14, 16, 20, 16, 20, 15, 22, 19, 15, 24, 23, 16, 21, 17, 17, 24, 16, 16, 22, 16, 16, 16, 15, 13, 24, 17, 22, 21, 15, 21, 21, 19, 22, 23, 24, 18, 14, 18, 13, 13, 4, 10, 4, 3, 11, 11, 8, 4, 8, 1, 5, 10, 5, 10, 5, 4, 10, 10, 8, 7, 1, 12, 10, 5, 9, 3, 3, 6, 5, 2, 1, 10, 10, 10, 11, 8, 10, 12, 2, 10, 9, 3, 10, 11, 11, 1, 10, 6, 6, 8, 4, 6, 11, 11, 6, 11, 8, 10, 5, 8, 2, 12, 8, 8, 15, 15, 19, 20, 23, 18, 18, 18, 19, 15, 22, 23, 20, 22, 14, 21, 22, 17, 16, 15, 19, 21, 20, 15, 24, 22, 22, 24, 21, 14, 20, 14, 13, 22, 13, 22, 15, 16, 18, 20, 17, 15, 22, 23, 22, 13, 15, 21, 19, 16, 14, 17, 21, 17, 18, 21, 21, 13, 19, 15, 22, 18, 21, 15, 15, 15, 16, 17, 18, 14, 20, 24, 23, 15, 23, 24, 16, 19, 24, 16, 13, 19, 18, 22, 20, 13, 23, 14, 21, 24, 14, 18, 24, 24, 16, 19, 17, 19, 22, 18, 15, 16, 20, 23, 23, 22, 21, 16, 23, 16, 13, 24, 13, 21, 23, 14, 23, 20, 13, 24, 13, 21, 17, 23, 19, 15, 17, 17]

## Algorithm FIFO
- Number of errors: 47
![Graph FIFO](FIFO_interleavedratio12.png)

## Algorithm LFU
- Number of errors: 131
![Graph LFU](LFU_interleavedratio12.png)

## Algorithm LRU
- Number of errors: 47
![Graph LRU](LRU_interleavedratio12.png)

## Summary

=== REPLACE THIS WITH SUMMARY ===
