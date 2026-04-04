| Operation      | Array/List | String (immutable) |
|----------------|------------|--------------------|
| random access  | O(1)*      | O(1)               |
| append to end  | O(1)       | O(n) new string    |
| pop from end   | O(1)       | O(n) new string    |
| insert at      | O(n)       | O(n) new string    |
| delete at      | O(n)       | O(n) new string    |
| update element | O(n)       | O(n) new string    |
| search element | O(n)       | O(n)               |
| merge          | O(n)       | O(n) new string    |   
| reverse        | O(n)       | O(n) to list       |
| sort           | O(n log n) | O(n log n) to list |