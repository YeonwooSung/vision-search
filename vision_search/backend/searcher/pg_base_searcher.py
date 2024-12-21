from pgvector.psycopg import register_vector
import psycopg
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

import ssl

# custom modules
from backend.utils.singleton import Singleton


# turning off SSL verification for custom certificates
ssl._create_default_https_context = ssl._create_unverified_context


class PostgresBaseSearcher(metaclass=Singleton):
    def __init__(self, use_async: bool = False):
        if use_async:
            self.engine = create_async_engine("postgresql+asyncpg://postgres:password@localhost:5432/postgres")
        else:
            self.engine = create_engine("postgresql+psycopg2://postgres:password@localhost:5432/postgres")
        self.use_async = use_async

        # register the vector type
        register_vector(self.engine)

    def _get_session(self):
        return AsyncSession(self.engine) if self.use_async else self.engine.connect()


    def create_index(self, create_table: bool = True):
        session = self._get_session()
        try:
            if create_table:
                session.execute('DROP TABLE IF EXISTS images')
                session.execute('CREATE TABLE images (id bigserial PRIMARY KEY, embedding vector(512))')

            session.execute('CREATE INDEX idx_images_embedding ON images USING ivfflat(embedding)')
            session.commit()

        except Exception as e:
            print(f"Error creating index: {e}")
        finally:
            session.close()


    def bulk_ingest(self, generate_data, chunk_size=128):
        pass

    def knn_search(self, query_features, k=10):
        pass
