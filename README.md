# dijkstra-gps-planner
Algorithm based GPS planner application

 Project structure:

  dijkstra-gps-planner/
  ├── app.py              # Full app (Dijkstra + Streamlit GUI + NetworkX
  visualization)
  ├── requirements.txt    # streamlit, networkx, matplotlib
  ├── .gitignore          # venv, pycache, etc
  └── README.md           # Full documentation with complexity analysis

  To test locally before demo:
  pip install -r requirements.txt
  streamlit run app.py
  
  The app has the GUI visualization (bonus +1 mark), algorithm step trace, and
  highlighted route map
