"""
CinOpSys - Movie Recommendation Dashboard (Simplified Version)
Ultra-simple version without custom HTML/CSS to ensure rendering works
"""

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import time

# Page config
st.set_page_config(
    page_title="CinOpSys - Movie Recommender",
    page_icon=None,
    layout="wide"
)

# Load data
@st.cache_resource
def load_data():
    try:
        embeddings = np.load('movie_embeddings.npy')
        metadata = pd.read_csv('movies_clean.csv')
        return embeddings, metadata
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None, None

# Initialize
embeddings, metadata = load_data()

if embeddings is None or metadata is None:
    st.stop()

# Create lookup
title_to_idx = {title.lower(): idx for idx, title in enumerate(metadata['title'])}

# Header
st.title("CinOpSys")
st.markdown("Content-Based Movie Recommendation System")
st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("Settings")
    top_k = st.slider("Number of Recommendations", 1, 50, 10)
    min_sim = st.slider("Minimum Similarity", 0.0, 1.0, 0.0, 0.05)
    synopsis_len = st.slider("Synopsis Length", 100, 500, 300, 50)
    
    st.markdown("---")
    st.metric("Total Movies", f"{len(metadata):,}")

# Search
st.header("Search Movie")
col1, col2 = st.columns([3, 1])

with col1:
    query = st.text_input("Enter movie title", placeholder="e.g., Matrix, Inception...")

with col2:
    search_btn = st.button("Search", type="primary", use_container_width=True)

# Process search
if query:
    matches = metadata[metadata['title'].str.contains(query, case=False, na=False)]
    
    if len(matches) > 0:
        st.success(f"Found {len(matches)} movie(s)")
        
        selected = st.selectbox("Select a movie:", matches['title'].tolist())
        
        if selected:
            movie_idx = title_to_idx.get(selected.lower())
            
            if movie_idx is not None:
                movie_info = metadata.iloc[movie_idx]
                
                st.markdown("---")
                
                st.subheader("Selected Movie")
                st.write(f"**{movie_info['title']}**")
                st.write("Synopsis:")
                st.write(movie_info['plot_synopsis'][:synopsis_len] + "...")
                
                st.markdown("---")
                
                with st.spinner("Finding similar movies..."):
                    start = time.time()
                    
                    target_vec = embeddings[movie_idx].reshape(1, -1)
                    sim_scores = cosine_similarity(target_vec, embeddings).flatten()
                    
                    sorted_idx = sim_scores.argsort()[::-1]
                    
                    recs = []
                    for idx in sorted_idx:
                        if idx == movie_idx:
                            continue
                        if sim_scores[idx] < min_sim:
                            break
                        
                        recs.append({
                            'title': metadata.iloc[idx]['title'],
                            'score': sim_scores[idx],
                            'pct': sim_scores[idx] * 100,
                            'synopsis': metadata.iloc[idx]['plot_synopsis']
                        })
                        
                        if len(recs) >= top_k:
                            break
                    
                    elapsed = time.time() - start
                
                st.subheader("Recommendations")
                st.caption(f"Generated in {elapsed:.3f} seconds")
                
                if recs:
                    for i, rec in enumerate(recs, 1):
                        with st.container():
                            col_a, col_b = st.columns([4, 1])
                            
                            with col_a:
                                st.write(f"**#{i}. {rec['title']}**")
                                st.caption("Synopsis:")
                                st.write(rec['synopsis'][:synopsis_len] + "...")
                            
                            with col_b:
                                st.metric("Similarity", f"{rec['score']:.3f}", f"{rec['pct']:.1f}%")
                            
                            st.markdown("---")
                    
                    st.subheader("Export")
                    df_export = pd.DataFrame(recs)[['title', 'score', 'pct']]
                    csv = df_export.to_csv(index=False)
                    
                    st.download_button(
                        "Download CSV",
                        csv,
                        f"recommendations_{selected.replace(' ', '_')}.csv",
                        "text/csv"
                    )
                else:
                    st.warning("No recommendations found. Try lowering the similarity threshold.")
    else:
        st.warning(f"No movies found matching '{query}'")

else:
    st.info("Use the search box above to find a movie.")
    
    st.subheader("Sample Movies")
    st.caption("Try searching for these:")
    
    sample = metadata.sample(min(12, len(metadata)))
    
    cols = st.columns(4)
    for i, (_, row) in enumerate(sample.iterrows()):
        with cols[i % 4]:
            with st.container():
                st.write(f"**{row['title']}**")
