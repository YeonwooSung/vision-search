## Setup

### Creating a KV Database Instance

Follow the steps outlined in the [quick start guide](https://vercel.com/docs/storage/vercel-kv/quickstart#create-a-kv-database) provided by Vercel. This guide will assist you in creating and configuring your KV database instance on Vercel, enabling your application to interact with it.

Remember to update your environment variables (`KV_URL`, `KV_REST_API_URL`, `KV_REST_API_TOKEN`, `KV_REST_API_READ_ONLY_TOKEN`) in the `.env` file with the appropriate credentials provided during the KV database setup.

### Creating a Postgres Database Instance

Follow the steps outlined in the [quick start guide](https://vercel.com/docs/storage/vercel-postgres/quickstart) provided by Vercel. This guide will assist you in creating and configuring your Postgres database instance on Vercel, enabling your application to interact with it.

Once you have instantiated your Vercel Postgres instance, run the following code to enable `pgvector`:
```bash
CREATE EXTENSION vector;
```

Remember to update your environment variables (`POSTGRES_URL`, `POSTGRES_PRISMA_URL`, `POSTGRES_URL_NON_POOLING`, `POSTGRES_USER`, `POSTGRES_HOST`, `POSTGRES_PASSWORD`, `POSTGRES_DATABASE`) in the `.env` file with the appropriate credentials provided during the Postgres database setup.

### Creating a Blob Instance

Follow the steps outlined in the [quick start guide](https://vercel.com/docs/storage/vercel-blob) provided by Vercel. This guide will assist you in creating and configuring your Blob instance on Vercel, enabling your application to interact with it.

Remember to update your environment variable (`BLOB_READ_WRITE_TOKEN`) in the `.env` file with the appropriate credentials provided during the Blob setup.

## Running locally

0. Set up the .env file with the necessary environment variables. You can use the `.env.example` file as a template.
1. Download your environment variables: `vercel env pull`

```bash
pnpm install
```

## Add OpenAI API Key
Be sure to add your OpenAI API Key to your `.env`.

## Database Setup
To push your schema changes to your Vercel Postgres database, run the following command.
```bash
pnpm run db:generate
pnpm run db:push
```

## Prepare your Images (Indexing Step)
To get your application ready for Semantic search, you will have to complete three steps.
1. Upload Images to storage
2. Send Images to a Large Language Model to generate metadata (title, description)
3. Iterate over each image, embed the metadata, and then save to the database

### Upload Images
Put the images you want to upload in the `images-to-index` directory (.jpg format) at the root of your application. Run the following command.
```bash
pnpm run upload
```
This script will upload the images to your Vercel Blob store.
Depending on how many photos you are uploading, this step could take a while.

### Generate Metadata
Run the following command.
```bash
pnpm run generate-metadata
```
This script will generate metadata for each of the images you uploaded in the previous step.
Depending on how many photos you are uploading, this step could take a while.

### Embed Metadata and Save to Database
Run the following command.
```bash
pnpm run embed-and-save
```
Depending on how many photos you are uploading, this step could take a while. This script will embed the descriptions generated in the previous step and save them to your Vercel Postgres instance.

## Starting the Server
Run the following command
```bash
pnpm run dev
```
Your app template should now be running on [localhost:3000](http://localhost:3000/).
