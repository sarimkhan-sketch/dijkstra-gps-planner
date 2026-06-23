import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import heapq

st.set_page_config(page_title="Jaipur GPS Route Planner", layout="wide")
st.title("🗺️ Jaipur GPS Route Planner — Dijkstra's Algorithm")
st.markdown("**DAA Assignment-2** | Real-Life Application of Dijkstra's Shortest Path Algorithm")
st.markdown("---")

# Jaipur City Road Network
# Nodes: Key landmarks | Edges: Roads | Weights: Distance in km
jaipur_graph = {
    "Mansarovar": {"Vaishali Nagar": 5, "Malviya Nagar": 7, "Jhotwara": 6},
    "Vaishali Nagar": {"Mansarovar": 5, "Jhotwara": 4, "C-Scheme": 8},
    "Jhotwara": {"Vaishali Nagar": 4, "Mansarovar": 6, "Amer Fort": 12},
    "Malviya Nagar": {"Mansarovar": 7, "Jagatpura": 5, "C-Scheme": 6},
    "C-Scheme": {"Vaishali Nagar": 8, "Malviya Nagar": 6, "Hawa Mahal": 3, "MI Road": 2},
    "MI Road": {"C-Scheme": 2, "Hawa Mahal": 1.5, "Railway Station": 3},
    "Hawa Mahal": {"C-Scheme": 3, "MI Road": 1.5, "City Palace": 1, "Amer Fort": 11},
    "City Palace": {"Hawa Mahal": 1, "Nahargarh Fort": 6, "Amer Fort": 10},
    "Amer Fort": {"Jhotwara": 12, "Hawa Mahal": 11, "City Palace": 10, "Nahargarh Fort": 5},
    "Nahargarh Fort": {"City Palace": 6, "Amer Fort": 5},
    "Jagatpura": {"Malviya Nagar": 5, "Sitapura": 4, "Railway Station": 8},
    "Sitapura": {"Jagatpura": 4, "Sanganer Airport": 6},
    "Sanganer Airport": {"Sitapura": 6, "Mansarovar": 9},
    "Railway Station": {"MI Road": 3, "Jagatpura": 8, "Sindhi Camp": 2},
    "Sindhi Camp": {"Railway Station": 2, "C-Scheme": 3},
}


def dijkstra(graph, source, destination):
    """
    Dijkstra's algorithm for shortest path using a binary min-heap.

    Parameters:
        graph: dict of dict {node: {neighbor: weight, ...}, ...}
        source: starting node
        destination: target node

    Returns:
        (shortest_distance, path_list, steps_log)
    """
    dist = {node: float('infinity') for node in graph}
    dist[source] = 0
    prev = {node: None for node in graph}
    visited = set()
    steps = []

    pq = [(0, source)]

    while pq:
        current_dist, u = heapq.heappop(pq)

        if u in visited:
            continue
        visited.add(u)

        steps.append(f"Visit **{u}** (distance = {current_dist} km)")

        if u == destination:
            break

        for v, weight in graph[u].items():
            if v not in visited:
                alt = current_dist + weight
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
                    heapq.heappush(pq, (alt, v))
                    steps.append(f"  ↳ Relax {u} → {v}: {current_dist} + {weight} = {alt} km")

    path = []
    current = destination
    while current is not None:
        path.append(current)
        current = prev[current]
    path.reverse()

    if dist[destination] == float('infinity'):
        return -1, [], steps

    return dist[destination], path, steps


# --- UI ---
st.subheader("Select Route")

col1, col2 = st.columns(2)
with col1:
    source = st.selectbox("📍 Start Location", sorted(jaipur_graph.keys()), index=sorted(jaipur_graph.keys()).index("Mansarovar"))
with col2:
    dest_options = sorted(jaipur_graph.keys())
    destination = st.selectbox("🏁 Destination", dest_options, index=dest_options.index("Hawa Mahal"))

if source == destination:
    st.warning("Source and destination are the same. Please select different locations.")
elif st.button("🚗 Find Shortest Route", type="primary"):
    distance, path, steps = dijkstra(jaipur_graph, source, destination)

    if distance == -1:
        st.error("❌ No route found between the selected locations!")
    else:
        st.markdown("---")

        # Results
        res_col1, res_col2 = st.columns(2)
        with res_col1:
            st.metric("Shortest Distance", f"{distance} km")
        with res_col2:
            st.metric("Stops", f"{len(path)} locations")

        st.success(f"**Route:** {' → '.join(path)}")

        # Algorithm Steps
        with st.expander("📋 Algorithm Execution Steps (Click to expand)"):
            for step in steps:
                st.markdown(step)

        # Graph Visualization
        st.markdown("---")
        st.subheader("🗺️ Route Visualization")

        G = nx.Graph()
        for node, neighbors in jaipur_graph.items():
            for neighbor, weight in neighbors.items():
                G.add_edge(node, neighbor, weight=weight)

        fig, ax = plt.subplots(1, 1, figsize=(14, 9))
        pos = nx.spring_layout(G, seed=42, k=2)

        # Draw base graph (grey)
        nx.draw_networkx_edges(G, pos, ax=ax, edge_color='#CCCCCC', width=1.5)
        nx.draw_networkx_nodes(G, pos, ax=ax, node_color='#AED6F1', node_size=900, edgecolors='#2C3E50', linewidths=1.5)
        nx.draw_networkx_labels(G, pos, ax=ax, font_size=7, font_weight='bold')

        # Draw edge weights
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=6, ax=ax, font_color='#555555')

        # Highlight shortest path
        path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='#E74C3C', width=4, ax=ax)

        # Highlight path nodes
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='#E74C3C', node_size=1100, edgecolors='#922B21', linewidths=2, ax=ax)

        # Highlight source and destination specially
        nx.draw_networkx_nodes(G, pos, nodelist=[source], node_color='#27AE60', node_size=1300, edgecolors='#1E8449', linewidths=2.5, ax=ax)
        nx.draw_networkx_nodes(G, pos, nodelist=[destination], node_color='#F39C12', node_size=1300, edgecolors='#D68910', linewidths=2.5, ax=ax)

        ax.set_title(f"Shortest Path: {source} → {destination} ({distance} km)", fontsize=14, fontweight='bold')
        ax.legend(['', '', '', '', 'Shortest Path', 'Path Nodes', f'Source: {source}', f'Dest: {destination}'],
                  loc='upper left', fontsize=8)
        ax.axis('off')
        plt.tight_layout()
        st.pyplot(fig)

        # Legend
        st.markdown("""
        **Legend:**
        - 🟢 Green = Source | 🟠 Orange = Destination | 🔴 Red = Shortest Path
        - Grey edges = all roads | Numbers on edges = distance in km
        """)
