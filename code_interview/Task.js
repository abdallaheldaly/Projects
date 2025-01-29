 
 /*
Please modify the sections indicated in this file to implement the methods described below. You may add your own methods if needed, but the final solution must work within the designated methods.

Implement the following methods:

  * sumOfDigits(n): This function calculates the sum of the digits of a given number n.
    For example, sumOfDigits(123) returns 6 because 1 + 2 + 3 = 6.

  * countPrimeFactors(n): This function determines the number of distinct prime factors of a given number n.
    For example, countPrimeFactors(24) returns 2 because 24 has 2 distinct prime factors, which are 2 and 3.

  * findShortestPath(graph, startNode, endNode): This function finds the shortest path in a graph based on custom edge weights. It uses a modified version of Dijkstra's algorithm.
    The input graph is represented as an object where each key represents a node, and the corresponding value is an array of neighbors with the format { node: <neighborNode>, weight: <originalWeight> }.
    The startNode parameter specifies the starting node, and the endNode parameter specifies the target node. The function returns the weight of the shortest path from the startNode to the endNode.
    If no path exists, it returns -1.

    The edge weight to used in the algorithm is the originalWeight + the sum of digits of the original weight * the count of prime factors for the original weight.
    The provided method calculateEdgeWeight can be used in your findShortestPath implementation.

    For example, for the following graph:

    const graph1 = {
      A: [{ node: 'B', weight: 26 }, { node: 'C', weight: 38 }],
      B: [{ node: 'A', weight: 26 }, { node: 'D', weight: 14 }],
      C: [{ node: 'A', weight: 38 }, { node: 'D', weight: 45 }],
      D: [{ node: 'B', weight: 14 }, { node: 'C', weight: 45 }]
    };

    findShortestPath(graph1, 'A', 'D') should return 66 since the shortest path is A->B->D.

    Please do not use AI or copy answers from the internet directly into this file. You may use the internet for research, but the implementation must be your own.
    Failure to follow this rule will result in your disqualification.
*/



/////////////////////////////////////////////////////////



  // Calculate the edge weight based on the originally provided weight, use this in your implementation of findShortestPath.
  function calculateEdgeWeight(weight){
    return weight + sumOfDigits(weight) * countPrimeFactors(weight);
  }
 
 // Determine the sum of the digits of a number.
  function sumOfDigits(n) {
    // TODO: Your answer goes here.
  }

  // Determine the number of distinct prime factors of a number.
  function countPrimeFactors(n) {
    // TODO: Your answer goes here.
  }

  // Find the shortest path based on the custom edge weights.
  function findShortestPath(graph, startNode, endNode) {
    // TODO: Your answer goes here.
  }

  module.exports = { sumOfDigits, countPrimeFactors, findShortestPath };




// Calculate the edge weight based on the original weight
function calculateEdgeWeight(weight) {
  return weight + sumOfDigits(weight) * countPrimeFactors(weight);
}

// Calculate the sum of digits of a number
function sumOfDigits(n) {
  return n.toString().split('').reduce((sum, digit) => sum + parseInt(digit), 0);
}

// Count the number of distinct prime factors of a number
function countPrimeFactors(n) {
  const primeFactors = new Set();
  for (let i = 2; i * i <= n; i++) {
    while (n % i === 0) {
      primeFactors.add(i);
      n /= i;
    }
  }
  if (n > 1) primeFactors.add(n);
  return primeFactors.size;
}

// Find the shortest path based on custom edge weights
function findShortestPath(graph, startNode, endNode) {
  const distances = new Map();
  const priorityQueue = new MinHeap();
  const visited = new Set();

  // Initialize distances
  Object.keys(graph).forEach(node => distances.set(node, Infinity));
  distances.set(startNode, 0);

  priorityQueue.insert({ node: startNode, distance: 0 });

  while (!priorityQueue.isEmpty()) {
    const { node: currentNode, distance: currentDistance } = priorityQueue.extractMin();

    if (visited.has(currentNode)) continue;
    visited.add(currentNode);

    for (const neighbor of graph[currentNode]) {
      const { node: neighborNode, weight } = neighbor;
      const edgeWeight = calculateEdgeWeight(weight);
      const newDistance = currentDistance + edgeWeight;

      if (newDistance < distances.get(neighborNode)) {
        distances.set(neighborNode, newDistance);
        priorityQueue.insert({ node: neighborNode, distance: newDistance });
      }
    }
  }

  return distances.get(endNode) === Infinity ? -1 : distances.get(endNode);
}

// MinHeap class for priority queue
class MinHeap {
  constructor() {
    this.heap = [];
  }

  insert(element) {
    this.heap.push(element);
    this._heapifyUp();
  }

  extractMin() {
    if (this.isEmpty()) return null;
    if (this.heap.length === 1) return this.heap.pop();

    const min = this.heap[0];
    this.heap[0] = this.heap.pop();
    this._heapifyDown();
    return min;
  }

  isEmpty() {
    return this.heap.length === 0;
  }

  _heapifyUp() {
    let index = this.heap.length - 1;
    while (index > 0) {
      const parentIndex = Math.floor((index - 1) / 2);
      if (this.heap[index].distance >= this.heap[parentIndex].distance) break;
      [this.heap[index], this.heap[parentIndex]] = [this.heap[parentIndex], this.heap[index]];
      index = parentIndex;
    }
  }

  _heapifyDown() {
    let index = 0;
    const length = this.heap.length;

    while (true) {
      const leftChildIndex = 2 * index + 1;
      const rightChildIndex = 2 * index + 2;
      let smallest = index;

      if (leftChildIndex < length && this.heap[leftChildIndex].distance < this.heap[smallest].distance) {
        smallest = leftChildIndex;
      }
      if (rightChildIndex < length && this.heap[rightChildIndex].distance < this.heap[smallest].distance) {
        smallest = rightChildIndex;
      }
      if (smallest === index) break;

      [this.heap[index], this.heap[smallest]] = [this.heap[smallest], this.heap[index]];
      index = smallest;
    }
  }
}

module.exports = { sumOfDigits, countPrimeFactors, findShortestPath };


const graph1 = {
  A: [{ node: 'B', weight: 26 }, { node: 'C', weight: 38 }],
  B: [{ node: 'A', weight: 26 }, { node: 'D', weight: 14 }],
  C: [{ node: 'A', weight: 38 }, { node: 'D', weight: 45 }],
  D: [{ node: 'B', weight: 14 }, { node: 'C', weight: 45 }]
};

console.log(findShortestPath(graph1, 'A', 'D'));


// Run the code using Node.js
// $ node Task.js