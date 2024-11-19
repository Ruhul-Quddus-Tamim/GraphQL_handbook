# GraphQL Handbook

### What is GraphQL?

GraphQL is a query language for APIs and a runtime for executing those queries. It allows clients to request only the data they need, making APIs more flexible and efficient.

Key Features

```
1. Strongly Typed: GraphQL has a strongly typed schema that defines the structure of data clients can request.

2. Client-Specified Queries: Clients control what data they get in a single query.

3. Single Endpoint: All queries and mutations are handled via a single endpoint.

4. Efficient Data Fetching: Fetch nested, related resources in a single request.

5. Real-Time Capabilities: Through subscriptions, GraphQL supports real-time updates.
```

### Core Concepts

__1. Schema__

The schema is the heart of a GraphQL server. It defines the data types and relationships. It includes:

> I) Types: The data shapes (e.g., User, Post).
> 
> II) Queries: For fetching data.
> 
> III) Mutations: For modifying data.
> 
> IV) Subscriptions: For real-time updates.

__2. Queries__

Queries fetch data. Clients specify the shape of the data they want.

__3. Mutations__

Mutations are for creating, updating, or deleting data.

__4. Resolvers__

Resolvers are functions that fetch the data for each field in the schema. They map queries and mutations to the actual data source.

__5. Subscriptions__

Subscriptions allow clients to listen for real-time updates.
