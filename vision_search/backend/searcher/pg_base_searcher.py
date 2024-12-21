from pgvector.psycopg import register_vector
import psycopg

import ssl

# turning off SSL verification for custom certificates
ssl._create_default_https_context = ssl._create_unverified_context


class PostgresBaseSearcher:
    def __init__(self):
        pass

    def create_index(self):
        pass

    def bulk_ingest(self, generate_data, chunk_size=128):
        pass

    def knn_search(self, query_features, k=10):
        pass
