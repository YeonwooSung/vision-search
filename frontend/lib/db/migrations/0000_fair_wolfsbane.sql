CREATE TABLE "images" (
	"id" varchar(191) PRIMARY KEY NOT NULL,
	"title" text NOT NULL,
	"description" text NOT NULL,
	"path" text NOT NULL,
	"embedding" vector(1536) NOT NULL
);
--> statement-breakpoint
CREATE INDEX "embeddingIndex" ON "images" USING hnsw ("embedding" vector_cosine_ops);