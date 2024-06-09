# Complexity Task

A strongly biconnected directed graph G=(V,E) is 2-vertex strongly biconnected[5] if G has at least three

vertices and G\{w} is strongly biconnected for all vertices w in G.

## Task

### Step - 1 -

An implementation of the Cheriyan-Mehlhorn-Gabow algorithm[1,2,3] for finding strongly connected components of a directed graph in linear time.

### Step - 2 -

An implementation of Jens Schmidt's algorihm [4] for testing whether an undirected graph is 2-connected (That means it has no articulation points) in linear time

### Step - 3 -

Testing whether a directed graph is 2-vertex strongly biconnected or not

in time O(n(n+m)).

## References

1. Martin Dietzfelbinger, Kurt Mehlhorn, Peter Sanders: Algorithmen und Datenstrukturen - die Grundwerkzeuge. examen.press, Springer 2014, ISBN 978-3-642-05471-6, pp. I-XII, 1-380

2. Kurt Mehlhorn, Stefan Näher, Peter Sanders: Engineering DFS-Based Graph Algorithms. CoRR abs/1703.10023 (2017)

3. Harold N. Gabow: Path-based depth-first search for strong and biconnected components. Inf. Process. Lett. 74(3-4): 107-114 (2000)

4. J. M. Schmidt, A simple test on 2-vertex- and 2-edge-connectivity, Inform. Process. Lett. 113
   (2013) 241-244.

5. Raed Jaberi, Minimum 2-Vertex Strongly Biconnected Spanning Directed Subgraph Problem Discrete Mathematics Letters, 40-43, Volume 7(2021) DOI: 10.47443/dml.2021.0024

6. Stanford Large Network Dataset Collection, https://snap.stanford.edu/data/index.html

## Testing Results

| Graph Description                                | Type       | Nodes     | Edges     | is2Connected -Time- | isStronglyConnected -Time- | isStronglyBiconnected -Time- | is2VertexStronglyBiconnected -Time- |
| ------------------------------------------------ | ---------- | --------- | --------- | ------------------- | -------------------------- | ---------------------------- | ----------------------------------- |
| Amazon product network                           | Undirected | 334,863   | 925,872   | true -30.381ms-     | false                      | false                        | false                               |
|ego-Facebook facebook_combined                     | Undirected | 4,039 | 88,234 | false -35.9072ms-     | false                      | false                        | false 2.960ms                              |
| Email communication network from Enron           | Undirected | 36,692    | 183,831   | false -34.616ms-    | false                      | false                        | false                               |
| Arxiv High Energy Physics paper citation network | Directed   | 34,546    | 421,578   | false               | false -25.081ms-           | false -16.142ms-             | false -22.726ms-                    |
| Email network from a EU research institution     | Directed   | 265,214   | 420,045   | false               | false -8.643ms-            | false -2.157ms-              | false -5.4ms-                       |
| Wikipedia who-votes-on-whom network              | Directed   | 7,115     | 03,689    | false 47.1772ms      | false -7.2803ms-           | false - 8.589ms-             | false -2.6928ms-                    |

## Students

- بشار نبيل فضه 3657 (اعادة عملي)
- رند احمد شعبان 6172
- رغد كارم محمد 6181
- سالي محمد ابراهيم 6225 
- رهف رفيق الحكيم 6458
- حنين رمضان احمد 6351
- 6137 حنين نزيه بدور 
