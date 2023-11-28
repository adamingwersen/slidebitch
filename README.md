# Slidebitch

### TODOs:

- [x] Build out vectordb
- [x] Expand searchable text
- [x] Build simple API
- [x] Similarity on article-level
- [x] Demo in web-app
- [ ] Text summarisation
- [ ] Extract relevant sub-elements / key points
- [ ] Better data storage
- [ ] Similarity on sub-elements
- [ ] Choose mode in web-app

## Running code locally:

### 1. Fetch data

To run the scrapers in `/python/scrape`:

```.sh
python3 get_links.py && python3 get_page.py
python3 assert_correctness.py
```

### 2. Build vectordb

Go to `/python/vectordb`
Ensure that you set `.env` vars: `[COLLECTION_NAME, PERSIST_DIR]`
Build a vector database using `chromadb`:

```.sh
python3 build.py
```

### 3. Run API as backend

We now need to serve this to a webapp, we do this using `FastAPI`:

```.sh
uvicorn api:app --reload
```

### 4. Run webapp

Go to `/webapp`.
Run:

```.sh
npm run dev
```
