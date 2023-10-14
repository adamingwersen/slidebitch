type QueryMetadata = {
  title: string;
  description: string;
  link: string;
};
type QueryResult = {
  distance: number;
  metadata: QueryMetadata;
  id: string;
};

type QueryPayload = {
  queryString: string;
  queryResults: QueryResult[];
};
