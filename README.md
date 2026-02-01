# CinOpSys - Movie Recommendation Dashboard

Dashboard interaktif berbasis Streamlit untuk sistem rekomendasi film menggunakan Content-Based Filtering dengan Universal Sentence Encoder.

## Features

### Core Functionality
- **Smart Movie Search**: Pencarian film dengan partial match dan case-insensitive
- **Semantic Recommendations**: Rekomendasi berbasis semantic similarity dari plot synopsis
- **Interactive Controls**: Slider untuk mengatur jumlah rekomendasi dan similarity threshold
- **Real-time Analytics**: Visualisasi distribusi similarity dan ranking

### User Interface
- **Clean & Modern Design**: UI yang profesional dengan custom CSS
- **Responsive Layout**: Adaptive layout untuk berbagai ukuran layar
- **Interactive Charts**: Plotly charts untuk data visualization
- **Export Functionality**: Download hasil rekomendasi dalam format CSV/JSON

### Performance
- **Caching**: Streamlit cache untuk loading data yang efficient
- **Fast Search**: Optimized search dengan dictionary lookup
- **Lazy Loading**: Analytics hanya di-render ketika diperlukan

## Installation

### Prerequisites
- Python 3.10 atau lebih baru
- pip package manager

### Setup

1. **Install dependencies**:
```bash
pip install -r requirements.txt
```

2. **Prepare data files**:
Pastikan file-file berikut ada di direktori yang sama dengan `app.py`:
- `movie_embeddings.npy` - Embeddings matrix dari notebook
- `movies_clean.csv` - Metadata film yang sudah di-clean

File-file ini dihasilkan dari notebook `cinopsys_improved.ipynb`.

## Usage

### Running the Dashboard

```bash
streamlit run app.py
```

Dashboard akan terbuka di browser pada `http://localhost:8501`

### Basic Workflow

1. **Search Movie**: Ketik judul film di search box
2. **Select Movie**: Pilih film dari hasil pencarian
3. **View Recommendations**: Lihat film-film yang mirip berdasarkan plot
4. **Adjust Settings**: Gunakan sidebar untuk:
   - Mengatur jumlah rekomendasi (1-50)
   - Set minimum similarity threshold (0.0-1.0)
   - Adjust panjang synopsis preview
5. **Analyze Results**: Lihat visualisasi di Analytics section
6. **Export Data**: Download hasil dalam format CSV atau JSON

## Architecture

### File Structure
```
.
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── movie_embeddings.npy      # Pre-computed embeddings (from notebook)
├── movies_clean.csv          # Movie metadata (from notebook)
└── README.md                # This file
```

### Code Organization

```python
# Main Components:
- Config: Configuration class untuk settings
- load_data(): Data loading dengan caching
- MovieRecommender: Core recommendation engine
- render_*(): UI rendering functions
- main(): Application entry point
```

### Key Classes

**Config**
- Manages file paths and default parameters
- Centralized configuration

**MovieRecommender**
- `search_movies()`: Search functionality
- `get_recommendations()`: Generate recommendations
- `get_similarity_distribution()`: Analytics data

## Configuration

### Customization Options

Edit `Config` class di `app.py`:

```python
class Config:
    EMBEDDINGS_FILE = 'movie_embeddings.npy'
    METADATA_FILE = 'movies_clean.csv'
    MAX_SYNOPSIS_LENGTH = 300
    DEFAULT_TOP_K = 10
    MIN_SIMILARITY = 0.0
    CACHE_TTL = 3600  # Cache time-to-live (seconds)
```

### UI Customization

Modify CSS di bagian `st.markdown()`:
- Colors: Change `#E50914` (Netflix red) ke brand color Anda
- Fonts: Update font-size dan font-weight
- Layout: Adjust padding dan margins

## Performance Optimization

### Data Loading
- Menggunakan `@st.cache_resource` untuk cache embeddings
- Cache TTL default: 1 hour

### Search Optimization
- Dictionary-based lookup: O(1) untuk exact match
- Pandas vectorized operations untuk partial match

### Memory Management
- Similarity calculation on-demand
- Sampling untuk analytics (1000 samples)

## Troubleshooting

### Common Issues

**Error: File not found**
```
Solution: Pastikan movie_embeddings.npy dan movies_clean.csv 
ada di direktori yang sama dengan app.py
```

**Slow performance**
```
Solution: 
1. Reduce CACHE_TTL jika memory terbatas
2. Reduce num_samples di get_similarity_distribution()
3. Gunakan subset data untuk testing
```

**Port already in use**
```bash
# Run on different port
streamlit run app.py --server.port 8502
```

## Development

### Adding New Features

**1. Add new metric:**
```python
def calculate_diversity_score(recommendations):
    # Your implementation
    pass
```

**2. Add new visualization:**
```python
def render_new_chart(data):
    fig = go.Figure()
    # Your plotly code
    st.plotly_chart(fig)
```

**3. Add new filter:**
```python
# In sidebar
genre_filter = st.sidebar.multiselect("Filter by Genre", options=genres)
```

## Deployment

### Local Network
```bash
streamlit run app.py --server.address 0.0.0.0
```

### Streamlit Cloud
1. Push code to GitHub
2. Connect repo di share.streamlit.io
3. Add secrets jika diperlukan
4. Deploy

### Docker (Optional)
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
```

## Best Practices

### Code Quality
- Type hints di semua functions
- Docstrings dengan clear descriptions
- Proper error handling
- Logging untuk debugging

### User Experience
- Clear error messages
- Loading spinners untuk long operations
- Helpful tooltips
- Responsive design

### Performance
- Cache expensive operations
- Lazy loading untuk analytics
- Optimize data structures
- Profile memory usage

## Future Enhancements

### Planned Features
- [ ] Multi-movie input untuk hybrid recommendations
- [ ] Genre/tag filtering
- [ ] Advanced analytics (diversity, novelty)
- [ ] User preference learning
- [ ] Comparison mode (side-by-side)
- [ ] Movie details page dengan poster
- [ ] Watchlist functionality
- [ ] API endpoint untuk external integration

### Technical Improvements
- [ ] Add unit tests
- [ ] Add integration tests
- [ ] Implement CI/CD
- [ ] Add monitoring/logging
- [ ] Database integration
- [ ] User authentication
- [ ] Rate limiting

---

**Built with ❤️ for movie lovers**
