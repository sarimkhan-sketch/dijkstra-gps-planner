# 🗺️ Jaipur GPS Route Planner — Dijkstra's Algorithm

A real-life implementation of **Dijkstra's Shortest Path Algorithm** applied to GPS route planning in Jaipur city.

> **DAA Assignment** | Manipal University Jaipur

## What It Does

This application models Jaipur's road network as a weighted graph (15 landmarks, 17 bidirectional roads) and uses Dijkstra's algorithm to find the shortest route between any two locations.

**Features:**
- Interactive Streamlit GUI for selecting source/destination
- Real-time shortest path computation using a min-heap (binary heap)
- Graph visualization with the shortest path highlighted in red
- Step-by-step algorithm execution trace
- Distance displayed in kilometers

## Algorithm

**Dijkstra's Algorithm** finds the shortest path from a source vertex to all other vertices in a graph with non-negative edge weights.

- **Time Complexity:** O((V + E) log V) with binary heap
- **Space Complexity:** O(V + E)
- **Approach:** Greedy (always processes the closest unvisited vertex)

### Why Dijkstra for GPS?

Road distances are always positive → Dijkstra's correctness is guaranteed. It's the foundational algorithm behind Google Maps, Apple Maps, and all navigation systems.

## City Graph

```
Nodes (15): Mansarovar, Vaishali Nagar, Jhotwara, Malviya Nagar,
            C-Scheme, MI Road, Hawa Mahal, City Palace, Amer Fort,
            Nahargarh Fort, Jagatpura, Sitapura, Sanganer Airport,
            Railway Station, Sindhi Camp

Edges: Weighted by actual approximate road distances (km)
```

## How to Run

### Prerequisites
- Python 3.9+

### Setup

```bash
# Clone the repo
git clone https://github.com/sarimkhan-sketch/dijkstra-gps-planner.git
cd dijkstra-gps-planner

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

The app will open at `http://localhost:8501`.

### Usage

1. Select a **Start Location** from the dropdown
2. Select a **Destination** from the dropdown
3. Click **"Find Shortest Route"**
4. View the shortest distance, route, algorithm steps, and graph visualization

## Example Output

```
Source: Mansarovar → Destination: Amer Fort

Shortest Distance: 22.0 km
Route: Mansarovar → Jhotwara → Amer Fort (via direct road: 6 + 12 = 18 km — if shorter)
       OR via Vaishali Nagar → Jhotwara → Amer Fort (5 + 4 + 12 = 21 km)
       Algorithm picks: Mansarovar → Jhotwara → Amer Fort = 18 km
```

## Project Structure

```
dijkstra-gps-planner/
├── app.py              # Main application (Dijkstra + Streamlit UI + Visualization)
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## Tech Stack

| Technology | Purpose |
|-----------|---------|
| Python 3 | Core implementation |
| Streamlit | Web-based GUI |
| NetworkX | Graph data structure & visualization |
| Matplotlib | Rendering the route map |
| heapq | Min-heap priority queue for Dijkstra |

## Complexity Analysis

| Metric | Value | Explanation |
|--------|-------|-------------|
| Time (Binary Heap) | O((V+E) log V) | Each of E relaxations does a heap push in O(log V) |
| Time (This graph) | O(49 × 4) ≈ ~200 ops | V=15, E=34, log₂(15)≈4 |
| Space | O(V + E) | Adjacency list + dist/prev arrays |

### Comparison

| Algorithm | Time | Negative Weights? | Best For |
|-----------|------|-------------------|----------|
| **Dijkstra** ✓ | O((V+E) log V) | No | GPS (positive distances) |
| Bellman-Ford | O(VE) | Yes | Currency arbitrage |
| Floyd-Warshall | O(V³) | Yes | All-pairs (small graphs) |
| A* | O((V+E) log V) | No | GPS with heuristic |

## Author

**Sarim Khan**
- Course: B.Tech CSE, VI Semester
- University: Manipal University Jaipur
- Guide: Prof. Abhay Bisht

  
 
