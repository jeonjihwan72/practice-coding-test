# 3650. Minimum Cost Path with Edge Reversals

### 원문

- You are given a directed, weighted graph with `n` nodes labeled from 0 to `n-1`, and an array `edges` where `edges[i] = [u<sub>i</sub>, v<sub>i</sub>, w<sub>i</sub>]` represents a directed edge from node `u<sub>i</sub>` to node `v<sub>i</sub>` with cost `w<sub>i</sub>`

- Each node `u<sub>i</sub>`, has a switch that can be used at most once: when you arrive at `u<sub>i</sub>` and have not yet used its switch, you may activate it on one of its incoming edges `v<sub>i</sub> -> u<sub>i</sub>` reverse that edge to `u<sub>i</sub> -> v<sub>i</sub>` and immediately traverse it.

- The reversal is only valid for that single move, and using a reversed edge costs `2 * w<sub>i</sub>`.

- Return the minimum total cost to travel from node 0 to node `n-1`. If it is not possible, return -1.

### 국문

- `n` 노드가 0에서 `n-1`로 라벨이 붙은 방향 가중치 그래프와 `u<sub>i</sub>` 노드에서 `v<sub>i</sub>` 노드로 가는 방향 간선을 의미하는 배열 `edges[i] = [u<sub>i</sub>, v<sub>i</sub>, w<sub>i</sub>]` 가 주어집니다. 비용은 `w<sub>i</sub>` 입니다.

- 각 노드 `u_i`에는 최대 한 번만 사용할 수 있는 스위치가 있습니다. 당신이 노드 `u_i`에 도착했을 때 아직 해당 노드의 스위치를 사용하지 않았다면, 그 노드로 들어오는 간선(edge) 중 하나인 `v_i \to u_i`를 선택해 스위치를 활성화할 수 있습니다. 스위치를 사용하면 해당 간선은 `u_i \to v_i` 방향으로 역전되며, 당신은 그 즉시 역전된 간선을 따라 이동해야 합니다.

- 간선의 역전은 해당 이동(move) 시에만 유효하며, 역전된 간선을 사용하는 데에는 기존 가중치의 두 배인 `2 * w_i`의 비용이 발생합니다.

- 노드 0에서 노드 `n-1`까지 이동하는 데 드는 최소 전체 비용을 반환하세요. 만약 이동이 불가능하다면 -1을 반환하세요.

### 입출력 형식

- example 1.
  - Input: squares = [[0, 0, 1], [2, 2, 1]]
  - Output: 1.00000
  - Explanation:
    ![example01.png](./examples/example01.png)
    - Any horizontal line between and will have 1 square unit above it and 1 square unit below it. The lowest option is 1. `y=1` `y=2`
- example 1.
  - Input: squares = [[0, 0, 2], [1, 1, 1]]
  - Output: 1.16667
  - Explanation:
    ![example01.png](./examples/example02.png)
    - The areas are:
      - Below the line: `7/6 * 2 (Red) + 1/6 (Blue) = 15/6 = 2.5`
      - Above the line: `5/6 * 2 (Red) + 5/6 (Blue) = 15/6 = 2.5`
    - Since the areas above and below the line are equal, the output is `7/6 = 1.16667`
